all:
	sudo DOCKER_BUILDKIT=0 docker-compose -f docker-compose.yml up -d --build

clean:
	sudo docker-compose -f docker-compose.yml down
	sudo docker system prune -a --force --volumes --all
	
re: clean all
