#!/usr/bin/env python2
# -*- coding:utf-8 -*-
import commands,sys
from optparse import OptionParser

parser = OptionParser(usage="%prog -w <warning threshold> -c <critical threshold> [ -h ]\n\n",version="%prog ")
parser.add_option("-s", "--service",action="store", type="string",dest="service", help="service name")
parser.add_option("-w", "--waring",action="store", type="int",dest="waring", help="Thrift connect waring line")
parser.add_option("-c", "--critical",action="store", type="int",dest="critical", help="Thrift connect critical line")
(options, args) = parser.parse_args()

def serstatu( sername , warings = 800 , criticals = 1000 ):

  thepid = str(commands.getoutput("sudo jps -l | grep %s | grep -v grep | grep -v check_local_service.py | awk '{print $1}'" %sername))
  if thepid == "":
    print("ERROR,the %s service is down" %sername)
    sys.exit(2)
  else:
    thecon = int(commands.getoutput("sudo netstat -antp | grep -v grep | grep -v LISTEN | grep %s | wc -l" %thepid))
    if 0 <= thecon < warings:
      print("OK , the %s pid:%s connect:%d | thecon=%d;%d;%d;0" %(sername,thepid,thecon,thecon,warings,criticals))
      sys.exit(0)
    elif warings <= thecon < criticals:
      print("WARING , the %s pid:%s connect:%d | thecon=%d;%d;%d;0" %(sername,thepid,thecon,thecon,warings,criticals))
      sys.exit(1)
    elif thecon >= criticals:
      print("CRITICAL , the %s pid:%s connect:%d | thecon=%d;%d;%d;0" %(sername,thepid,thecon,thecon,warings,criticals))
      sys.exit(2)
    else:
      print('UNKNOWN STATUS')
      sys.exit(3)
serstatu(options.service)
