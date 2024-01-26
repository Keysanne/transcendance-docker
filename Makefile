all:
	docker-compose up -d --build

clean:
	docker-compose -f docker-compose.yml down
	docker system prune -a --force --volumes --all

ip:
	chmod +x get_ip.sh
	./get_ip.sh

fclean: clean
	docker volume rm transcendance-docker_postgres

re: clean all
