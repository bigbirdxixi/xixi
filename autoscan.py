#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import os,commands,sqlite3
#获取服务名
s = commands.getoutput(r"jps -l | grep -v grep | grep com. | awk '{print $2}'").split('\n')
try:
  con = sqlite3.connect(r'./wsf.db')
  cur = con.cursor()
#  cur.execute(r'drop table service')
  cur.execute(r'create table if not exists service (sername txt primary key)')
  for n in s:
    oldser = cur.execute(r'select sername from service where sername = ?',(n,)).fetchone()
    if oldser == None:
      cur.execute(r"insert into service (sername) values (?)",(n,))
      os.system(r"echo 'command[%s]=/usr/local/nagios/libexec/check_local_service.py -s %s' >> ./wsf.txt" %(n,n))
finally:
  con.commit()
  cur.close()
  con.close()
