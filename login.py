#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import sqlite3,hashlib
pwd = input(r"please input the god's password:")
#pwd = 'hevenwashell'
hspwd = hashlib.md5()
hspwd.update(pwd.encode('utf-8'))

#打开数据库连接
try:
	dbconnect = sqlite3.connect(r'./wsf.db')
	dbcursor = dbconnect.cursor()
	dbcursor.execute(r'select password from user where id = ? ' , ('0000000' ,))
	valu = dbcursor.fetchone()
	#登录判断
	if hspwd.hexdigest() in valu:
		print('mygod,wellcome!!')
finally:
	#关闭数据库连接
	dbcursor.close()
	dbconnect.commit()
	dbconnect.close()