------------------------------------------------------
-------- Feature Engineering ------------
---- Objective :
---- Create an analysis-ready dataset by generating
---- derived features from the cleaned data.
--
-- Source Table:
-- bike_trips_clean
--
-- Output Table:
-- bike_trips_features
------------------------------------------------------

CREATE TABLE bike_trips_features AS
SELECT *,

	ROUND(
		EXTRACT(EPOCH FROM (ended_at - started_at)) / 60,
		2
	) AS ride_length_minutes,

	DATE(started_at) AS ride_date,
	EXTRACT(MONTH FROM started_at) :: INT AS month_number,
	EXTRACT(ISODOW FROM started_at) :: INT AS day_of_week_number,
	EXTRACT(HOUR FROM started_at)  :: INT AS hour_of_day,

	CASE
		WHEN EXTRACT(ISODOW FROM started_at) IN (6,7)
		THEN TRUE
		ELSE FALSE
	END AS is_weekend

FROM bike_trips_clean;

------ Validating the dataset ---------

------ Record Count ------
SELECT COUNT(*) AS total_records
FROM bike_trips_features;

------ Ride Duration -------
SELECT
	started_at,
	ended_at,
	ride_length_minutes
FROM bike_trips_features
LIMIT 10;

------ Month Distribution ------
SELECT
    month_number,
    COUNT(*) AS total_rides
FROM bike_trips_features
GROUP BY month_number
ORDER BY month_number;

------ Day of week -------
SELECT
    day_of_week_number,
    COUNT(*) AS total_rides
FROM bike_trips_features
GROUP BY day_of_week_number
ORDER BY day_of_week_number;

------ Hour of the day ------
SELECT
    hour_of_day,
    COUNT(*) AS total_rides
FROM bike_trips_features
GROUP BY hour_of_day
ORDER BY hour_of_day;

------ Weekend Flag -------
SELECT
    is_weekend,
    COUNT(*) AS total_rides
FROM bike_trips_features
GROUP BY is_weekend;
