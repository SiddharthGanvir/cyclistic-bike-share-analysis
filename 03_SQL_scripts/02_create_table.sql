--=====================================
-- Cyclistic Bike Share Analysis
-- Create Main Table
--=====================================

CREATE TABLE bike_trips(
ride_id TEXT PRIMARY KEY,
rideable_type TEXT NOT NULL,

started_at TIMESTAMP NOT NULL,
ended_at TIMESTAMP NOT NULL,

start_station_name TEXT,
start_station_id TEXT,

end_station_name TEXT,
end_station_id TEXT,

start_lat DOUBLE PRECISION,
start_lng DOUBLE PRECISION,

end_lat DOUBLE PRECISION,
end_lng DOUBLE PRECISION,

member_casual TEXT NOT NULL
);