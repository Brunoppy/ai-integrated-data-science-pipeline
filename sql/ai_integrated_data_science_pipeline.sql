-- Create a PostgreSQL table for processed analytics results
CREATE TABLE IF NOT EXISTS analytics_results (
    id SERIAL PRIMARY KEY,
    dataset_name VARCHAR(255),
    metric_name VARCHAR(255),
    metric_value FLOAT,
    processed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
