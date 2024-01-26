CREATE TABLE IF NOT EXISTS events (
    id UUID,
    user_id VARCHAR,
    value INTEGER,
    event_time DATETIME,
    event_type VARCHAR(100)
);