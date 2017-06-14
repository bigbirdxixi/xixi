#!/bin/bash
thepid=`ps -ef | grep -v grep | grep cfgsync.sh | awk '{print $2}'`

if [ -z "$thepid" ];then
    echo "cfgsync not start"
else
    echo "kill cfgsync old $thepid"
    kill -9 $thepid
fi

sh /opt/cfgsync/rsync-start.sh
