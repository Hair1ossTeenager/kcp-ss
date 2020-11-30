#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys

def start_kcp_server():
    cmd = "docker run -d --restart always --name kcp-server -p 8443:8443 -p 8443:8443/udp xtaci/kcptun server -t 127.0.0.1:443 -l :8443 -mode fast2"
    print(cmd)
    os.system(cmd)

def start_ss_server(mode, password):
    cmd = "docker run -d -u root --restart always --name ss-server --net=container:kcp-server liaohuqiu/ss ss-server -s 0.0.0.0 -p 443 -m %s -k %s -u --plugin obfs-server --plugin-opts 'obfs=tls'" % (mode, password)
    print(cmd)
    os.system(cmd)

def start_server(mode, password):
    start_kcp_server()
    start_ss_server(mode, password)

if __name__=='__main__':
    mode = 'rc4-md5'
    password = '123466'
    argv = sys.argv[1:]
    if len(argv) == 2:
        mode = argv[0]
        password = argv[1]
    start_server(mode, password)
