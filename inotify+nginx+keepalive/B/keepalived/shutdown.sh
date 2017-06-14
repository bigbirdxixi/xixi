#!/bin/bash
sh /opt/cfgsync/stop-monitor.sh && kill `cat /var/run/keepalived.pid`
