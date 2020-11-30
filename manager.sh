#!/usr/bin/bash

current_dir=`cd $(dirname $0);pwd -P`
server_ip=$1
mode=$2
password=$3

function start_server() {
    python $current_dir/server/server.py $mode $password
}

function start_client() {
    python $current_dir/client/client.py $server_ip
}

start_server
start_client
