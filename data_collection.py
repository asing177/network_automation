#!/usr/bin/python3 

import time
import paramiko


def send_cmd(conn , command):
    conn.send(command+"\n")
    time.sleep(10)


def get_output():
    return conn.recv(65535).decode("utf-8")



def main():
    device_list = {
        "r1" : "ls",
        "r2" : "ls -a"
    }

    for host , command in device_list.items():
        conn_params = paramiko.SSHCLient()
        conn_params.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        conn_params.connect(
            host=host, 
            username=user, 
            port=22,
            look_for_keys=False,
            allow_agent=False)

