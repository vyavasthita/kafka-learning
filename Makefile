all: stop up

stop:
	docker compose stop

clean:
	docker compose stop
	docker container prune -f
	docker image prune -f

up:
	docker compose up -d --build --remove-orphans

test:
	docker exec backend pytest -v

cov:
	docker exec backend pytest --cov
