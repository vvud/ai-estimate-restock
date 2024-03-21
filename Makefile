#!make
# show some help
help:
	@echo
	@echo 'Usage:'
	@echo '  make <target>'
	@echo
	@echo 'Most used Targets:'
	@echo '  build:                 Build the application in docker'
	@echo '  up:                    Start the application in docker'
	@echo '  down:                  Stop the application'
	@echo '  dv:                    Stop the application and delete volumes'
	@echo '  restart:               Restart the application'
	@echo

build:
	docker-compose build --no-cache

up:
	docker-compose up -d

down:
	docker-compose down

dv:
	docker compose down

restart: 
	docker-compose restart

