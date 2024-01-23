build:
	docker-compose up -d --build 

up:
	docker-compose up -d

down:
	docker-compose down --remove-orphans

stop:
	docker-compose stop

db:
	docker exec -it mongocfg1 bash -c "mongosh < "scripts/init_config_server1.js" 
	docker exec -it mongors1n1 bash -c "mongosh < "scripts/init_shard_1.js" 
	docker exec -it mongors1n1 bash -c "mongosh < "scripts/init_shard_2.js" 
	docker exec -it mongors1n1 bash -c "mongosh < "scripts/init_router.js" 
	docker exec -it mongors1n1 bash -c "mongosh < "scripts/init_db.js" 

