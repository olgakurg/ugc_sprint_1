CREATE DATABASE replica;


CREATE TABLE IF NOT EXISTS replica.movies_progress (
    id UUID,
    user_uuid UUID,
    film_uuid UUID,
    movie_progress Int64,
    event_time DateTime
) 
Engine=ReplicatedMergeTree('/clickhouse/tables/shard2/movies_progress', 'replica_2')
PARTITION BY film_uuid ORDER BY event_time;




