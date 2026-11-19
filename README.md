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

## notepad++ 运行python脚本
```bash
cmd /k cd /d "$(CURRENT_DIRECTORY)" & python "$(FULL_CURRENT_PATH)" & echo. & pause & exit
```

## 代码推送与镜像同步说明

本项目的代码推送流程如下：

```text
本地代码 → AtomGit → 自动镜像同步 → 腾讯云 CNB / GitHub / Gitee
```

## 请我喝杯咖啡

|     微信赞赏码     |       支付宝        |       支付宝红包        |
| :----------------: | :-----------------: | :-----------------: |
| <img src="images/wx.jpg" alt="赞赏码" width="200"> | <img src="images/zfb.jpg" alt="支付宝" width="200">| <img src="images/zfb_hb.jpg" alt="支付宝红包" width="200">|

## 你可以在这些地方找到我 (Find Me Here)

<p align="center">
  <a href="https://gitcode.com/techtest/navicat-connection-parser.git" target="_blank" rel="noopener">
    <img src="images/favicon_gitcode.ico" width="18" height="18" alt="GitCode">&nbsp;GitCode
  </a>
  <span style="color: #999;">&nbsp;/&nbsp;</span>
  <a href="https://atomgit.com/techtest/navicat-connection-parser.git" target="_blank" rel="noopener">&nbsp;AtomGit
  </a>
  &nbsp;&nbsp;
  <a href="https://cnb.cool/iaoexl/techtest/navicat-connection-parser.git" target="_blank" rel="noopener">
    <img src="images/favicon_cnb.ico" width="18" height="18" alt="腾讯云 CNB">&nbsp;腾讯云 CNB
  </a>
  &nbsp;&nbsp;
  <a href="https://github.com/iaoexl/navicat-connection-parser.git" target="_blank" rel="noopener">
    <img src="images/favicon_github.png" width="18" height="18" alt="GitHub">&nbsp;GitHub
  </a>
  &nbsp;&nbsp;
  <a href="https://gitee.com/techtest/navicat-connection-parser.git" target="_blank" rel="noopener">
    <img src="images/favicon_gitee.ico" width="18" height="18" alt="Gitee">&nbsp;Gitee
  </a>
</p>