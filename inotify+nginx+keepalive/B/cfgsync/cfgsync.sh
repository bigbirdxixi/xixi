#!/bin/bash
BASEDIR=/opt/nginx/conf
DESTIP=192.168.0.231
inotifywait -mr --timefmt '%Y-%m-%d %T' --format '%T %Xe %w %f' --exclude "swp|4913|\~" -e create,modify,attrib,move,delete $BASEDIR | while read date time dir file
do
    EVENTS=`echo $dir | awk -F '/' '{print $1}'`
    if [ -n $EVENTS ] ; then
        rsync -avz --delete --password-file=./rsyncd.secrets $BASEDIR/ nginx@$DESTIP::nginxconf/
    fi  
done
