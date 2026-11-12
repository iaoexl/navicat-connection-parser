#!/usr/bin/env python3

import platform

if platform.system().lower() != 'windows':
    print('Please run this script in Windows.')
    exit(-1)

import sys, winreg
from Crypto.Hash import SHA1
from Crypto.Cipher import Blowfish
from Crypto.Util import strxor

'''
 Navicat12Crypto is not needed.
'''

print("The database connection information is as follows:")

# 此加密类用于解密 Navicat 存储在注册表中的密码，仅用于合法的密码查看操作
class Navicat11Crypto:
    def __init__(self, Key=b'3DC5CA39'):
        self._Key = SHA1.new(Key).digest()
        self._Cipher = Blowfish.new(self._Key, Blowfish.MODE_ECB)
        self._IV = self._Cipher.encrypt(b'\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF')

    def EncryptString(self, s: str):
        if not isinstance(s, str):
            raise TypeError('Parameter s must be a str.')
        plaintext = s.encode('ascii')
        ciphertext = b''
        cv = self._IV
        full_round, left_length = divmod(len(plaintext), 8)

        for i in range(0, full_round * 8, 8):
            t = strxor.strxor(plaintext[i:i + 8], cv)
            t = self._Cipher.encrypt(t)
            cv = strxor.strxor(cv, t)
            ciphertext += t

        if left_length != 0:
            cv = self._Cipher.encrypt(cv)
            ciphertext += strxor.strxor(plaintext[8 * full_round:], cv[:left_length])

        return ciphertext.hex().upper()

    def DecryptString(self, s: str):
        if not isinstance(s, str):
            raise TypeError('Parameter s must be str.')
        plaintext = b''
        ciphertext = bytes.fromhex(s)
        cv = self._IV
        full_round, left_length = divmod(len(ciphertext), 8)

        for i in range(0, full_round * 8, 8):
            t = self._Cipher.decrypt(ciphertext[i:i + 8])
            t = strxor.strxor(t, cv)
            plaintext += t
            cv = strxor.strxor(cv, ciphertext[i:i + 8])

        if left_length != 0:
            cv = self._Cipher.encrypt(cv)
            plaintext += strxor.strxor(ciphertext[8 * full_round:], cv[:left_length])

        return plaintext.decode('ascii')


NavicatCipher = Navicat11Crypto()
ServersTypes = {
    'MySQL Server': 'Software\\PremiumSoft\\Navicat\\Servers',
    'MariaDB Server': 'Software\\PremiumSoft\\NavicatMARIADB\\Servers',
    'MongoDB Server': 'Software\\PremiumSoft\\NavicatMONGODB\\Servers',
    'MSSQL Server': 'Software\\PremiumSoft\\NavicatMSSQL\\Servers',
    'OracleSQL Server': 'Software\\PremiumSoft\\NavicatOra\\Servers',
    'PostgreSQL Server': 'Software\\PremiumSoft\\NavicatPG\\Servers',
    'SQLite Server': 'Software\\PremiumSoft\\NavicatSQLite\\Servers',
    'Redis Server': 'Software\\PremiumSoft\\NavicatRedis\\Servers',
    # 'Null' : ' ',
}

def get_registry_key(path):
    try:
        return winreg.OpenKey(winreg.HKEY_CURRENT_USER, path)
    except OSError:
        return None

# 此部分代码用于从 Windows 注册表中读取 Navicat 服务器配置信息，仅用于合法的配置查看操作
for ServersTypeName, ServersRegistryPath in ServersTypes.items():
    if not get_registry_key(ServersRegistryPath):
        continue
    print('Database Type:', ServersTypeName)
    print('{:<20}{:<20}{:<20}{:<20}'.format('Host', 'Port', 'User', 'Password'))

    ServersRegistryKey = get_registry_key(ServersRegistryPath)
    if not ServersRegistryKey:
        continue

    i = 0
    try:
        while True:
            ServerName = winreg.EnumKey(ServersRegistryKey, i)
            ServerRegistryKey = get_registry_key(f"{ServersRegistryPath}\\{ServerName}")
            if not ServerRegistryKey:
                continue

            try:
                ServerHost = winreg.QueryValueEx(ServerRegistryKey, 'Host')[0]
                ServerPort = winreg.QueryValueEx(ServerRegistryKey, 'Port')[0]
                if ServersTypeName == 'OracleSQL Server':
                    ServerInitialDb = winreg.QueryValueEx(ServerRegistryKey, 'InitialDatabase')[0]
                else:
                    ServerInitialDb = None
                ServerUsername = winreg.QueryValueEx(ServerRegistryKey, 'Username')[0]
                ServerPassword = winreg.QueryValueEx(ServerRegistryKey, 'Pwd')[0]
                if len(ServerPassword) != 0:
                    ServerPassword = NavicatCipher.DecryptString(ServerPassword)

                ServerUseSsh = winreg.QueryValueEx(ServerRegistryKey, 'UseSSH')[0]
                if ServerUseSsh != 0:
                    ServerSshHost = winreg.QueryValueEx(ServerRegistryKey, 'SSH_Host')[0]
                    ServerSshPort = winreg.QueryValueEx(ServerRegistryKey, 'SSH_Port')[0]
                    ServerSshUsername = winreg.QueryValueEx(ServerRegistryKey, 'SSH_Username')[0]
                    ServerSshPassword = winreg.QueryValueEx(ServerRegistryKey, 'SSH_Password')[0]
                    if len(ServerSshPassword) != 0:
                        ServerSshPassword = NavicatCipher.DecryptString(ServerSshPassword)
                else:
                    ServerSshHost = None
                    ServerSshPort = None
                    ServerSshUsername = None
                    ServerSshPassword = None

                print(f'{ServerHost:<20}{ServerPort:<20}{ServerUsername:<20}{ServerPassword:<20}')
                if ServerUseSsh:
                    print(f'{ServerSshHost:<20}{ServerSshPort:<20}{ServerSshUsername:<20}{ServerSshPassword:<20}')

            except Exception as e:
                print(f"[-] Failed to get info about server '{ServerName}'. Error: {e}", file=sys.stderr)
            finally:
                if ServerRegistryKey:
                    winreg.CloseKey(ServerRegistryKey)
            i += 1
    except OSError:
        pass

    if ServersRegistryKey:
        winreg.CloseKey(ServersRegistryKey)

input('Press "Enter" to end the program.')