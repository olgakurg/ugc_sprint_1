CREATE TABLE IF NOT EXISTS events (
    id UUID,
    relation_uuid UUID,
    user_uuid UUID,
    content VARCHAR,
    timestamp INTEGER,
    bject_type VARCHAR(100)
);
