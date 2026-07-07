------ Cyclistic Bike Share Analysis -------
------ Data Cleaning and validation  -------


------Total Count ---------
SELECT COUNT(*) FROM bike_trips;

------ Check for Duplicate Records -------

SELECT
    ride_id,
    COUNT(*) AS duplicate_count
FROM bike_trips
GROUP BY ride_id
HAVING COUNT(*) > 1;

---- Checking for missing values ------
SELECT
    COUNT(*) AS total_records,

    COUNT(*) - COUNT(start_station_name) AS missing_start_station_name,
    COUNT(*) - COUNT(start_station_id) AS missing_start_station_id,

    COUNT(*) - COUNT(end_station_name) AS missing_end_station_name,
    COUNT(*) - COUNT(end_station_id) AS missing_end_station_id,

    COUNT(*) - COUNT(start_lat) AS missing_start_lat,
    COUNT(*) - COUNT(start_lng) AS missing_start_lng,

    COUNT(*) - COUNT(end_lat) AS missing_end_lat,
    COUNT(*) - COUNT(end_lng) AS missing_end_lng

FROM bike_trips;

------Ride Duration Validation --------
SELECT
    COUNT(*) AS invalid_rides
FROM bike_trips
WHERE ended_at < started_at;

-----Invalid Ride Records------
SELECT
    ride_id,
    started_at,
    ended_at,
    member_casual,
    rideable_type
FROM bike_trips
WHERE ended_at < started_at;

---- Identifying Rideable Types --------
SELECT
    rideable_type,
    COUNT(*) AS total_rides
FROM bike_trips
GROUP BY rideable_type
ORDER BY total_rides DESC;

------- Identifying Member Types -------
SELECT
    member_casual,
    COUNT(*) AS total_rides
FROM bike_trips
GROUP BY member_casual
ORDER BY total_rides DESC;

------- Date Range Validation -------
SELECT
    MIN(started_at) AS first_ride,
    MAX(started_at) AS last_ride,
    MIN(ended_at) AS first_ride_end,
    MAX(ended_at) AS last_ride_end
FROM bike_trips;

------- Riding Duration Distribution ------
SELECT
    MIN(ended_at - started_at) AS minimum_duration,
    MAX(ended_at - started_at) AS maximum_duration
FROM bike_trips;

---------------------------------------------
------- Create Cleaned Dataset ---------
---------------------------------------------

CREATE TABLE bike_trips_clean AS
SELECT*
FROM bike_trips
WHERE
	end_lat IS NOT NULL
	AND end_lng IS NOT NULL
	AND ended_at >= started_at;
------------------------------------------------------------
-------- Validating Data of the cleaned dataset --------
------------------------------------------------------------

------ Verifying Total Number of Records --------
SELECT COUNT(*) AS total_records
FROM bike_trips_clean;

------- Missing Data Verification ----------
SELECT
	COUNT(*) AS missing_end_coordinates
FROM bike_trips_clean
WHERE end_lat IS NULL
 OR end_lng IS NULL;

--------- No Negative Ride Durations ---------
SELECT
	COUNT(*) AS invalid_durations
FROM bike_trips_clean
WHERE ended_at < started_at;

---------- Data Review Summary ------------
SELECT
    (SELECT COUNT(*) FROM bike_trips) AS raw_records,
    (SELECT COUNT(*) FROM bike_trips_clean) AS cleaned_records,
    (SELECT COUNT(*) FROM bike_trips) -
    (SELECT COUNT(*) FROM bike_trips_clean) AS records_removed;
