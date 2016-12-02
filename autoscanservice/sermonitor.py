#!/usr/bin/env python2
# -*- coding:utf-8 -*-
import os,re,socket,commands
def ipmaps(clientip,monitorpath):
  '取出监控配置文件路径,生成路径与IP对照字典ip_map并返回对应路径字符串'
  ip_map = {}
  for r,ds,fs in os.walk(monitorpath):
    for f in fs:
      if f.startswith('172') or f.startswith('10'):
        fn = os.path.join(r,f)
        mp = re.findall('\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}',fn)
        hostname = commands.getoutput("grep -i 'host_name' %s | awk '{print $2}' | sort -u" %fn)
        sertpl = commands.getoutput("grep -i '\-service' %s | awk '{print $2}' | sort -u" %fn)
        ip_map[mp[0]] = {'filpath':fn,'hostname':hostname,'sertpl':sertpl}
  return ip_map[clientip]

host = ''
port = 4420
s = socket.socket()
s.bind((host,port))
s.listen(500)
print('server is listing...')
while True:
  conn, addr = s.accept()
  print('connected from %s port %d' %(addr[0],addr[1]))
  data = conn.recv(1024)
  print('add service %s' %data)
  if data != None:
    conn.send('True')
    filepath = ipmaps(addr[0],r'/usr/local/nagios/etc/objects/')
    print(filepath)
    os.system('echo "define service{\n  use %s\n  host_name %s\n  service_description %s\n  check_command check_nrpe!%s\n}" >> %s' %(filepath['sertpl'],filepath['hostname'],data,data,filepath['filpath']))
  else:
    conn.send('False')

  os.system(r"/etc/init.d/nagios reload")
  conn.close()

