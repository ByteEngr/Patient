CREATE TABLE IF NOT EXISTS patients (
    id SERIAL PRIMARY KEY,
    age INT,
    gender VARCHAR(10),
    city VARCHAR(50),
    fever_temp FLOAT,
    cough_severity INT,
    has_covid BOOLEAN
);
