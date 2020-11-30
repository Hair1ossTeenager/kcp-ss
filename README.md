### 简介
kcp + ss

### 安装环境
- docker 环境
- 服务端开放 8443 端口
- 客户端开放 443 端口

### 服务端
```
#$mode 为 ss 加密方式，默认为 rc4-md5
#$password 为 ss 密码，默认为 123466
python server/server.py $mode $password
```

### 客户端
```
#$server_ip 为服务端公务 ip
python client/client.py $server_ip
```
