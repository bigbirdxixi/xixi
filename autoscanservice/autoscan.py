#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import os,commands,sqlite3,socket


def registser(host,port,sername):
  '注册服务名，返回成功或失败True/False'
  s = socket.socket()
  s.connect((host,port))
  s.send(sername)
  rel = s.recv(1024)
  return bool(rel)

#获取服务名
s = commands.getoutput(r"sudo jps -l | grep -v grep | grep com. | awk '{print $2}'").split('\n')
try:
  con = sqlite3.connect(r'./wsf.db')
  cur = con.cursor()
#  cur.execute(r'drop table service')
  cur.execute(r'create table if not exists service (sername txt primary key)')
  for n in s:
    oldser = cur.execute(r'select sername from service where sername = ?',(n,)).fetchone()
    if oldser == None:
      cur.execute(r"insert into service (sername) values (?)",(n,))
      os.system(r"echo 'command[%s]=/usr/local/nagios/libexec/check_local_service.py -s %s' >> /usr/local/nagios/etc/nrpe.cfg" %(n,n))
      registser('172.31.6.109',4420,n)
      os.system(r"kill -9 `ps -ef | grep -v grep | grep nrpe | awk '{print $2}'` && /usr/local/nagios/bin/nrpe -c /usr/local/nagios/etc/nrpe.cfg -d")
finally:
  con.commit()
  cur.close()
  con.close()
