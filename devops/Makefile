
.PHONY: install_dependencies status install_dependencies start_postgres create_network start_storage stop_storage start_batch stop_batch start_ingestion stop_ingestion

status: ## Status dos containers
	docker ps

install_dependencies: ## Instala dependências para o projeto
	@make create_network
	docker compose -f docker-compose.yaml pull
	docker compose -f docker-compose.yaml up airflow-init
	docker compose -f docker-compose-minio.yml pull
	docker compose -f docker-compose-ingestion.yml build

create_network: ## Cria rede entre os serviços
	docker network create serasa || true

start_postgres: ## Inicia Postgres
	docker compose -f docker-compose.yaml up -d postgres


start_storage: ## Inicia serviços
	@echo 'Start Storage'
	docker compose -f docker-compose-minio.yaml up -d


stop_storage: ## Inicia serviços
	@echo 'Start Storage'
	docker compose -f docker-compose-minio.yaml down

start_batch: ## Inicia serviços
	@echo 'Start Ingestion'
	docker compose -f docker-compose.yaml up -d

stop_batch: ## Desliga serviços
	$(info Make: Stop docker )
	docker compose -f docker-compose.yaml down

start_ingestion: ## Inicia serviços
	@echo 'Start Ingestion'
	docker compose -f docker-compose-ingestion.yaml up -d

stop_ingestion: ## Desliga serviços
	$(info Make: Stop docker )
	docker compose -f docker-compose-ingestion.yaml down

#################################################################################
# Self Documenting Commands                                                     #
#################################################################################

.DEFAULT_GOAL := help

# Inspired by <http://marmelab.com/blog/2016/02/29/auto-documented-makefile.html>
# sed script explained:
# /^##/:
# 	* save line in hold space
# 	* purge line
# 	* Loop:
# 		* append newline + line to hold space
# 		* go to next line
# 		* if line starts with doc comment, strip comment character off and loop
# 	* remove target prerequisites
# 	* append hold space (+ newline) to line
# 	* replace newline plus comments by `---`
# 	* print line
# Separate expressions are necessary because labels cannot be delimited by
# semicolon; see <http://stackoverflow.com/a/11799865/1968>
.PHONY: help

help:
	@echo Twitter - Data Project
	@echo Comandos disponíveis
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'