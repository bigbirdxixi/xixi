#!/bin/bash
if [ -f /var/run/rsyncd.pid ]
  then
  thepid=`cat /var/run/rsyncd.pid`
  echo "kill rsync old $thepid"
  kill $thepid && sleep 2
  if [ -f /var/run/rsyncd.pid ]
    then
    rm -f /var/run/rsyncd.pid
  else
    rsync --daemon --config=/etc/rsyncd/rsyncd.conf
  fi
else
  rsync --daemon --config=/etc/rsyncd/rsyncd.conf
fi

newpid=`cat /var/run/rsyncd.pid`

echo "rsync new pid is $newpid"
