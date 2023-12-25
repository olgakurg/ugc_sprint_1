CREATE DATABASE shard;

CREATE TABLE IF NOT EXISTS shard.movies_progress (
    id UUID,
    user_uuid UUID,
    film_uuid UUID,
    movie_progress Int64,
    event_time DateTime
) 
Engine=ReplicatedMergeTree('/clickhouse/tables/shard2/movies_progress', 'replica_1')
PARTITION BY film_uuid ORDER BY event_time;

CREATE TABLE IF NOT EXISTS default.movies_progress (
    id UUID,
    user_uuid UUID,
    film_uuid UUID,
    movie_progress Int64,
    event_time DateTime
) 
ENGINE = Distributed('company_cluster', '', movies_progress, rand());