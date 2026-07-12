-- ============================================
-- Module 4: Exploratory Data Analysis (EDA)
-- ============================================
-- Objective:
-- Explore the cleaned and feature-engineered
-- dataset to identify patterns, trends, and
-- relationships that support business insights.
--
-- Source Table:
-- bike_trips_features
-- ============================================

------- Total Rides -------
SELECT COUNT(*) AS total_rides
FROM bike_trips_features;

------- Counting rides for members vs casual riders ------
SELECT
    member_casual,
    COUNT(*) AS total_rides
FROM bike_trips_features
GROUP BY member_casual
ORDER BY total_rides DESC;



------- Percentage contribution from each group --------
SELECT
	member_casual,
	COUNT(*) AS total_rides,
	ROUND(
		(COUNT(*)*100.0) /
		(
			SELECT COUNT(*)
			FROM bike_trips_features
		),
		2
		
) AS ride_percentage

FROM bike_trips_features
GROUP BY member_casual
ORDER BY total_rides DESC;

------- Getting insights about rideable types ------
SELECT
    rideable_type,
    COUNT(*) AS total_rides,
    ROUND(
        (COUNT(*) * 100.0) /
        (
            SELECT COUNT(*)
            FROM bike_trips_features
        ),
        2
    ) AS ride_percentage
FROM bike_trips_features
GROUP BY rideable_type
ORDER BY total_rides DESC;

------- Count of user types based on rideable types -----
SELECT
	member_casual,
	rideable_type,
	COUNT(*) AS total_rides
FROM bike_trips_features
GROUP BY 
member_casual,
rideable_type
ORDER BY total_rides DESC;

------- Percentage contribution of each rideable type by member type --------
SELECT
    outer_table.member_casual,
    outer_table.rideable_type,
    COUNT(*) AS total_rides,

    ROUND(
        (COUNT(*) * 100.0) /
        (
            SELECT COUNT(*)
            FROM bike_trips_features AS inner_table
            WHERE inner_table.member_casual =
                  outer_table.member_casual
        ),
        2
    ) AS ride_percentage

FROM bike_trips_features AS outer_table

GROUP BY
    outer_table.member_casual,
    outer_table.rideable_type

ORDER BY
    outer_table.member_casual,
    total_rides DESC;

------- Average ride durations by member type -------
SELECT
    member_casual,
    ROUND(AVG(ride_length_minutes), 2) AS avg_ride_duration_minutes
FROM bike_trips_features
GROUP BY member_casual
ORDER BY avg_ride_duration_minutes DESC;

------- Monthly Ride Trends ---------
SELECT
    month_number,
    COUNT(*) AS total_rides,
    ROUND(
        (COUNT(*) * 100.0) /
        (
            SELECT COUNT(*)
            FROM bike_trips_features
        ),
        2
    ) AS ride_percentage
FROM bike_trips_features
GROUP BY month_number
ORDER BY month_number;

-------- Monthly ride trends between members and casual riders ------
SELECT
    month_number,
    member_casual,
    COUNT(*) AS total_rides
FROM bike_trips_features
GROUP BY
    month_number,
    member_casual
ORDER BY
    month_number,
    member_casual;

------- Day of week trend analysis --------
SELECT
    day_of_week_number,
    COUNT(*) AS total_rides,
    ROUND(
        (COUNT(*) * 100.0) /
        (
            SELECT COUNT(*)
            FROM bike_trips_features
        ),
        2
    ) AS ride_percentage
FROM bike_trips_features
GROUP BY day_of_week_number
ORDER BY day_of_week_number;

-------- Members vs casual riders day analysis -------
SELECT
    day_of_week_number,
    member_casual,
    COUNT(*) AS total_rides
FROM bike_trips_features
GROUP BY
    day_of_week_number,
    member_casual
ORDER BY
    day_of_week_number,
    member_casual;

-------- Hour of week analysis -------
SELECT
    hour_of_day,
    COUNT(*) AS total_rides,
    ROUND(
        (COUNT(*) * 100.0) /
        (
            SELECT COUNT(*)
            FROM bike_trips_features
        ),
        2
    ) AS ride_percentage
FROM bike_trips_features
GROUP BY hour_of_day
ORDER BY hour_of_day;

------ Hour of week analysis by member type -------
SELECT
    hour_of_day,
    member_casual,
    COUNT(*) AS total_rides
FROM bike_trips_features
GROUP BY
    hour_of_day,
    member_casual
ORDER BY
    hour_of_day,
    member_casual;

-------- Weekday vs Weekend Analysis --------
SELECT
    is_weekend,
    COUNT(*) AS total_rides,
    ROUND(
        (COUNT(*) * 100.0) /
        (
            SELECT COUNT(*)
            FROM bike_trips_features
        ),
        2
    ) AS ride_percentage
FROM bike_trips_features
GROUP BY is_weekend
ORDER BY is_weekend;

------- Weekday vs Weekend Rides Trend by member types -------
SELECT
    is_weekend,
    member_casual,
    COUNT(*) AS total_rides
FROM bike_trips_features
GROUP BY
    is_weekend,
    member_casual
ORDER BY
    is_weekend,
    member_casual;


------- Top Start Stations -------
SELECT
    start_station_name,
    COUNT(*) AS total_rides
FROM bike_trips_features
WHERE start_station_name IS NOT NULL
GROUP BY start_station_name
ORDER BY total_rides DESC
LIMIT 10;

------- Top End Stations --------
SELECT
    end_station_name,
    COUNT(*) AS total_rides
FROM bike_trips_features
WHERE end_station_name IS NOT NULL
GROUP BY end_station_name
ORDER BY total_rides DESC
LIMIT 10;