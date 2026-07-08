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

