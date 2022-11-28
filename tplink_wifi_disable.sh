#!/bin/sh

HOST='10.0.0.200 2323'
USER='TPG@telnet'
PASSWD='TPG@tp-link_2017'
CMD='wlctl set 2g --switch off'

(
echo open "$HOST"
sleep 2
echo "$USER"
sleep 2
echo "$PASSWD"
sleep 2
echo "$CMD"
sleep 2
echo "exit"
) | telnet
