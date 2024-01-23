CREATE DATABASE shard;

CREATE TABLE IF NOT EXISTS shard.events (
    id UUID,
    relation_uuid UUID,
    user_uuid UUID,
    content VARCHAR,
    timestamp INTEGER,
    object_type String(100)
) 
Engine=ReplicatedMergeTree('/clickhouse/tables/shard1/events', 'replica_1') 
PARTITION BY object_type ORDER BY timestamp;


CREATE TABLE IF NOT EXISTS default.events (
    id UUID,
    relation_uuid UUID,
    user_uuid UUID,
    content VARCHAR,
    timestamp INTEGER,
    object_type String(100)
) 
ENGINE = Distributed('company_cluster', '', events, rand());


