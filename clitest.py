#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import socket
host = '54.223.47.244'
port = 4420
s = socket.socket()
s.connect((host,port))
s.send(b'i am py3')
print(s.recv(1024))

