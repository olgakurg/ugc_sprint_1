CREATE DATABASE replica;

CREATE TABLE IF NOT EXISTS replica.events (
    id UUID,
    relation_uuid UUID,
    user_uuid UUID,
    content VARCHAR,
    timestamp INTEGER,
    object_type String(100)
) 
Engine=ReplicatedMergeTree('/clickhouse/tables/shard1/events', 'replica_2')
PARTITION BY object_type ORDER BY timestamp;




