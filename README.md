# Navicat 连接配置解析工具(navicat-connection-parser)

> ⚠️ **法律免责声明**
> 
> 本工具**仅限在本人拥有完全操作权限的 Windows 本机上使用**，仅用于找回自己遗忘的 Navicat 数据库连接密码。
> 
> 未经授权读取、获取他人计算机上的数据库账号密码属于违法行为，使用本工具产生的全部安全风险与法律责任均由使用者自行承担。

## 代码来源说明
> 本项目脚本基于互联网开源社区、公开论坛公开的代码片段进行整理、修复与改造。
> 
> 仅做技术学习演示使用，不代表原作者立场。
> 
> [main.py](src/main.py)  脚本在Windows环境中运行、测试，适配 [python-3.10](https://www.python.org/ftp/python/3.10.0/python-3.10.0rc2-amd64.exe) 程序。

## 📋项目简介
Python脚本，读取Windows注册表中Navicat保存的数据库连接配置，基于Blowfish算法解密加密存储的密码。
无需手动导出配置文件，脚本直接读取系统注册表。

### ✅支持解析的数据库类型
- MySQL Server
- MariaDB Server
- MongoDB Server
- MSSQL Server
- OracleSQL Server
- PostgreSQL Server
- SQLite Server
- Redis Server

额外支持读取并解密连接的 **SSH隧道账号、密码**。

### ⚠️版本与系统限制
- 仅支持 Windows 系统，依赖 Windows 注册表接口，Linux / macOS 无法运行
- 适配 Navicat 11 的加密算法；更高版本Navicat加密逻辑发生变更时，解密可能失效


## 需要安装以下Python库
``` bash
 pip install crypto
 pip install pycrypto
 pip install pycryptodome
 pip install pycryptodomex
```

## 打包为可执行程序
> 安装 `pyinstaller`

``` bash
pip install pywin32
pip install pyinstaller
```

> 参数函数

- -F 表示生成单个可执行文件
	
- -w 表示去掉控制台窗口，这在GUI界面时非常有用。不过如果是命令行程序的话那就把这个选项删除吧！
	
- -p 表示你自己自定义需要加载的类路径，一般情况下用不到
	
- -i 表示可执行文件的图标

> 打包举例

``` bash
# 打包为 exe 可执行文件
	pyinstaller -F main.py
# 加载 logo
	pyinstaller -F -i `icon\logo.ico` main.py
# 完整打包案例
	pyinstaller -F --clean --noconfirm --hidden-import=navicat-connection-parser --name navicat-connection-parser main.py
```

## notepad++ 运行python脚本
```bash
cmd /k cd /d "$(CURRENT_DIRECTORY)" & python "$(FULL_CURRENT_PATH)" & echo. & pause & exit
```