#!/bin/bash
thepid=`ps -ef | grep -v grep | grep cfgsync.sh | awk '{print $2}'`

if [ -z "$thepid" ];then
    nohup /opt/cfgsync/cfgsync.sh 1>> /dev/null 2>&1 &
    thepid=`ps -ef | grep -v grep | grep cfgsync.sh | awk '{print $2}'`
    echo "cfgsync new pid is $thepid"
else
    echo "kill cfgsync old $thepid"
    kill -9 $thepid
    nohup /opt/cfgsync/cfgsync.sh 1>> /dev/null 2>&1 &
    thepid=`ps -ef | grep -v grep | grep cfgsync.sh | awk '{print $2}'`
    echo "cfgsync new pid is $thepid"
fi

sh /opt/cfgsync/rsync-stop.sh
