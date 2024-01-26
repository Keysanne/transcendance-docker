all:
	docker-compose up -d --build

clean:
	docker-compose -f docker-compose.yml down
	docker system prune -a --force --volumes --all

ip:
	echo -n "VITE_URL_BASE=https://" > images/vuejs/front/.env
	ifconfig | grep -w "inet 10.*.*.*" | head -c 23 | tail -c 10 >> images/vuejs/front/.env
	echo "/" >> images/vuejs/front/.env

fclean: clean
	docker volume rm transcendance-docker_postgres

re: clean all
