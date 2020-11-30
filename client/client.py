#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys

def start_haproxy():
    path = os.path.abspath('.')
    cmd = "docker run -u root -d --restart always --name haproxy -p 443:443 -v %s/client/haproxy/haproxy.cfg:/usr/local/etc/haproxy/haproxy.cfg haproxy:1.7" % (path)
    print(cmd)
    os.system(cmd)

def start_kcp_client(server_ip):
    cmd = "docker run -d --restart always --name kcp-client --net=container:haproxy xtaci/kcptun client -r %s:8443 -l :8443 -mode fast2" % (server_ip)
    print(cmd)
    os.system(cmd)

def start_client(server_ip):
    start_haproxy()
    start_kcp_client(server_ip)

if __name__=='__main__':
    server_ip = sys.argv[1]
    start_client(server_ip)
