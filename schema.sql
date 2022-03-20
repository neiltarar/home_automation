CREATE TABLE IF NOT EXISTS 
    weather (id SERIAL PRIMARY KEY,
            date TEXT,
            time TEXT,
            temp FLOAT,
            hum FLOAT);