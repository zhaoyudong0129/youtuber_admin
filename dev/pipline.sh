#!/usr/bin/env bash
echo "***start git pull***"
git pull
echo "***start pip install ***"
pip install -r requirements.txt
echo "***start migrate ***"
python manage.py migrate
echo "***start collectstatic***"
python manage.py collectstatic
echo "***restart youtuber***"
supervisorctl -c dev/supervisord.conf restart youtuber
echo "***restart nginx***"
cp dev/nginx.conf /etc/nginx/nginx.conf
nginx -s reload