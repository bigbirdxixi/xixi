#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import sqlite3,hashlib
pwd = input(r"please input the god's password:")
hspwd = hashlib.md5()
hspwd.update(pwd.encode('utf-8'))
dbconnect = sqlite3.connect(r'./wsf.db')
dbcursor = dbconnect.cursor()
dbcursor.execute(r'select password from user where id = ? ' , ('0000000' ,))
valu = dbcursor.fetchone()
if hspwd.hexdigest() in valu:
  print('valu')
dbcursor.close()
dbconnect.commit()
dbconnect.close()