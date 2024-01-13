CREATE DATABASE shard;

CREATE TABLE IF NOT EXISTS shard.events (
    id UUID,
    user_id String,
    value Map(String, String),
    event_time DateTime,
    event_type String(100)
) 
Engine=ReplicatedMergeTree('/clickhouse/tables/shard2/events', 'replica_1')
PARTITION BY event_type ORDER BY event_time;

CREATE TABLE IF NOT EXISTS default.events (
    id UUID,
    user_id String,
    value Map(String, String),
    event_time DateTime,
    event_type String(100)
) 
ENGINE = Distributed('company_cluster', '', events, rand());