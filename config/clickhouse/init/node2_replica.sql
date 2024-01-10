CREATE DATABASE replica;

CREATE TABLE IF NOT EXISTS replica.events (
    id UUID,
    user_id String,
    value Map(String, String),
    event_time DateTime,
    event_type String(100)
) 
Engine=ReplicatedMergeTree('/clickhouse/tables/shard1/events', 'replica_2')
PARTITION BY user_id ORDER BY event_time;




