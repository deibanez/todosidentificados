.DEFAULT_GOAL := help
.PHONY: help

include .env
export

# taken from https://container-solutions.com/tagging-docker-images-the-right-way/

help: ## Print this help
	@grep -E '^[a-zA-Z_-\.]+:.*?## .*$$' Makefile | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

ps: ## docker-compose ps
	docker-compose ps

up: ## docker-compose up -d
	docker-compose up -d

from-scratch: ## docker-compose up -d --build
	docker-compose up -d --build

down: ## docker-compose down
	docker-compose down

users.logs: ## Show container logs for <users> service
	docker-compose logs --follow --tail 10 users

users.flake8: ## Run flake8 on <users>
	docker-compose exec users flake8 project

users.sh: ## Get shell access to <users> container
	@docker-compose exec users sh

users.test: ## Run <users> application tests
	@docker-compose exec users python manage.py test

users.repl: ## Get access to a python REPL within the application context in <users> container
	@docker-compose exec users python manage.py shell

users.db.recreate: ## Drops database in <db> and recreates it from scratch
	@docker-compose exec users python manage.py recreate_db

users.db.seed: ## Seed database in <db>
	@docker-compose exec users python manage.py seed_db

users.db.regenerate: users.db.recreate users.db.seed ## Recreates and seeds database in <db>

users.db.current: ## Displays the current database migration
	@docker-compose exec users python manage.py db current

users.db.history: ## Displays the migration revision history
	@docker-compose exec users python manage.py db history

users.db.upgrade: ## Upgrade the database in <db> using migration scripts
	@docker-compose exec users python manage.py db upgrade

users.db.downgrade: ## Downgrade the database in <db> using migration scripts
	@docker-compose exec users python manage.py db downgrade

users.coverage: ## Run tests with code coverage
	@docker-compose exec users python manage.py cov

db.psql: ## Launchs a psql instance on the <db> container
	@docker-compose exec users-db psql -U postgres

client.test: ## Run "npm test" from the <client> service
	@docker-compose exec client npm test

bump.major: ## Updates CHANGELOG and bumps to next major VERSION (i.e. VERSION.y.z)
	@PART=major sh ./bump_version.sh 

bump.minor: ## Updates CHANGELOG and bumps to next minor VERSION (i.e. x.VERSION.z)
	@PART=minor sh ./bump_version.sh 

bump.patch: ## Updates CHANGELOG and bumps to next patch VERSION (i.e. x.y.VERSION)
	@PART=patch sh ./bump_version.sh 

bump.changelog: ## Updates CHANGELOG
	@sh ./bump_changelog

bump.undo: ## Goes back one commit, i.e. reverts changes on files from last version bump (experimental)
	@sh ./undo_bump_version.sh

