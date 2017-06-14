#!/bin/bash
if [ -f /var/run/rsyncd.pid ]
  then
  thepid=`cat /var/run/rsyncd.pid`
  echo "kill rsync old $thepid"
  kill $thepid && sleep 2
  if [ -f /var/run/rsyncd.pid ]
    then
    rm -f /var/run/rsyncd.pid
  fi
else
  echo "rsync not start"
fi
