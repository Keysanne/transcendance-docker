all:
	sudo docker-compose up -d --build

clean:
	sudo docker-compose -f docker-compose.yml down
	sudo docker system prune -a --force --volumes --all
	
re: clean all
