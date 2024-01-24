all:
	docker-compose up -d --build

clean:
	docker-compose -f docker-compose.yml down
	docker system prune -a --force --volumes --all
	#docker volume rm transcendance-docker_postgres

fclean: clean
	docker volume rm transcendance-docker_postgres

re: clean all
