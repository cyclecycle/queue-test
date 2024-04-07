CREATE TABLE IF NOT EXISTS documents (
    id SERIAL PRIMARY KEY,
    query TEXT,
    fetched_data JSONB,
    processed_data JSONB,
    processed BOOLEAN DEFAULT FALSE
);
