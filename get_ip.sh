#!/bin/bash
already_done=$(grep IP_FRONT .env)
ip=$(ifconfig | grep -w "inet 10.*.*.*" | head -c 23 | tail -c 10 |  sed -e " s/\ //g")
if [ $already_done = "" ]; then
	echo -n "VITE_URL_BASE=https://$ip:8000/" > images/vuejs/front/.env
	echo -n "IP_FRONT=$ip" >> .env
else
	echo "IP already configured"
fi
