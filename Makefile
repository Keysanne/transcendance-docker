all:
	docker-compose up -d --build

clean:
	docker-compose -f docker-compose.yml down
	docker system prune -a --force --volumes --all

ip:
	chmod +x get_ip.sh
	./get_ip.sh
	echo -n "VITE_IP=" >> images/vuejs/front/.env
	ifconfig | grep -w "inet 10.*.*.*" | head -c 23 | tail -c 10 >> images/vuejs/front/.env

fclean: clean
	docker volume rm transcendance-docker_postgres

re: clean all
