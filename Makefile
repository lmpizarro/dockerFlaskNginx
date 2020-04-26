.DEFAULT_GOAL := default


default:
	sudo docker-compose down -v --remove-orphans
	sudo docker-compose up -d --build

run-daemon:
	sudo docker-compose up -d


run:
	sudo docker-compose up

build-dev:
	sudo docker-compose --build

logs:
	sudo docker-compose logs -f

ps:
	sudo docker-compose ps

clean:
	sudo docker-compose down -v --remove-orphans
