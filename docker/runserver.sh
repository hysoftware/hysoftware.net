#!/usr/bin/sh
source ${repo}/../bin/activate
secret=$(mkpasswd -l 40 -s 4 -C 12 -c 12 -d 12) \
  uwsgi --lazy-apps -y /home/hysoft/venv/webapp/etc/uwsgi.yml
