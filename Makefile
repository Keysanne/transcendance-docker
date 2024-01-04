all:
	docker-compose up -d --build

clean:
	docker-compose -f docker-compose.yml down
	docker system prune -a --force --volumes --all
	
re: clean all
