all: stop up

stop:
	docker compose stop

down:
	clear
	docker compose down

clean:
	clear
	docker compose stop
	docker compose down
	docker container prune -f
	docker image prune -f
	docker network prune -f
	docker volume prune -f

	sudo rm -rf kafka-data/kafka-1/data
	sudo rm -rf kafka-data/kafka-2/data
	sudo rm -rf kafka-data/kafka-3/data

	sudo rm -rf zk-data/zk-1/data
	sudo rm -rf zk-data/zk-2/data
	sudo rm -rf zk-data/zk-3/data

	sudo rm -rf zk-log/zk-1/log
	sudo rm -rf zk-log/zk-2/log
	sudo rm -rf zk-log/zk-3/log

ps:
	docker compose ps -a

up:
	clear
	docker compose up -d --build --remove-orphans
	docker compose ps -a



