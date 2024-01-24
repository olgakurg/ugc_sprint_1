build:
	docker-compose -f ./docker-compose-ugc2.yml up -d --build 

up:
	docker-compose -f ./docker-compose-ugc2.yml up -d

down:
	docker-compose -f ./docker-compose-ugc2.yml down --remove-orphans

stop:
	docker-compose -f ./docker-compose-ugc2.yml stop

db:
	docker exec -it mongocfg1 bash -c 'mongosh < /scripts/init_config_server.js'
	docker exec -it mongors1n1 bash -c 'mongosh < /scripts/init_shard_1.js'
	docker exec -it mongors2n1 bash -c 'mongosh < /scripts/init_shard_2.js' 
	docker exec -it mongos1 bash -c 'mongosh < /scripts/init_router.js' 
	docker exec -it mongos1 bash -c 'mongosh < /scripts/init_db.js'

