all: stop up

stop:
	docker compose stop

down:
	docker compose down

clean:
	docker compose stop
	docker compose down
	docker container prune -f
	docker image prune -f

up:
	docker compose up -d --build --remove-orphans

ps:
	docker compose ps -a