# ============================================================
# Cyclistic Bike Share Analysis
# Data Visualization using Python
# ============================================================


# ============================================================
# IMPORT LIBRARIES
# ============================================================

import pandas as pd
import matplotlib.pyplot as plt
import os

from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from matplotlib.ticker import FuncFormatter


# ============================================================
# DATABASE CONNECTION
# ============================================================

DATABASE_URL = URL.create(
    drivername="postgresql+psycopg2",
    username="postgres",
    password="os.getenv(DB_PASSWORD)",
    host="localhost",
    port=5432,
    database="cyclistic"
)

engine = create_engine(DATABASE_URL)


# ============================================================
# GLOBAL VARIABLES
# ============================================================

BAR_FIG_SIZE = (8, 5)
LINE_FIG_SIZE = (10, 5)

number_formatter = FuncFormatter(
    lambda x, _: f"{int(x):,}"
)


# ============================================================
# VISUALIZATION 1
# DISTRIBUTION OF RIDES BY MEMBER TYPE
# ============================================================


query_member_distribution = """
SELECT
    member_casual,
    COUNT(*) AS total_rides
FROM bike_trips_features
GROUP BY member_casual
ORDER BY total_rides DESC;
"""

df_member_distribution = pd.read_sql(
    query_member_distribution,
    engine
)

plt.figure(figsize=BAR_FIG_SIZE)

bars = plt.bar(
    df_member_distribution["member_casual"],
    df_member_distribution["total_rides"]
)

plt.title(
    "Distribution of Rides by Member Type",
    fontsize=14,
    fontweight="bold"
)

plt.xlabel("Member Type", fontsize=11)
plt.ylabel("Total Rides", fontsize=11)

plt.grid(axis="y", linestyle="--", alpha=0.4)

plt.gca().yaxis.set_major_formatter(number_formatter)

for bar in bars:
    height = bar.get_height()

    plt.text(
        bar.get_x() + bar.get_width() / 2,
        height,
        f"{int(height):,}",
        ha="center",
        va="bottom",
        fontsize=10,
        fontweight="bold"
    )

plt.tight_layout()
plt.show()
plt.close()


# ============================================================
# VISUALIZATION 2
# DISTRIBUTION OF RIDES BY BIKE TYPE
# ============================================================

query_bike_type = """
SELECT
    rideable_type,
    COUNT(*) AS total_rides
FROM bike_trips_features
GROUP BY rideable_type
ORDER BY total_rides DESC;
"""

df_bike_type = pd.read_sql(
    query_bike_type,
    engine
)

plt.figure(figsize=BAR_FIG_SIZE)

bars = plt.bar(
    df_bike_type["rideable_type"],
    df_bike_type["total_rides"]
)

plt.title(
    "Distribution of Rides by Bike Type",
    fontsize=14,
    fontweight="bold"
)

plt.xlabel("Bike Type", fontsize=11)
plt.ylabel("Total Rides", fontsize=11)

plt.grid(axis="y", linestyle="--", alpha=0.4)

plt.gca().yaxis.set_major_formatter(number_formatter)

for bar in bars:
    height = bar.get_height()

    plt.text(
        bar.get_x() + bar.get_width() / 2,
        height,
        f"{int(height):,}",
        ha="center",
        va="bottom",
        fontsize=10,
        fontweight="bold"
    )

plt.tight_layout()
plt.show()
plt.close()


# ============================================================
# VISUALIZATION 3
# AVERAGE RIDE DURATION BY MEMBER TYPE
# ============================================================

query_avg_duration = """
SELECT
    member_casual,
    ROUND(
        AVG(ride_length_minutes),
        2
    ) AS avg_ride_duration_minutes
FROM bike_trips_features
GROUP BY member_casual
ORDER BY avg_ride_duration_minutes DESC;
"""

df_avg_duration = pd.read_sql(
    query_avg_duration,
    engine
)

plt.figure(figsize=BAR_FIG_SIZE)

bars = plt.bar(
    df_avg_duration["member_casual"],
    df_avg_duration["avg_ride_duration_minutes"]
)

plt.title(
    "Average Ride Duration by Member Type",
    fontsize=14,
    fontweight="bold"
)

plt.xlabel("Member Type", fontsize=11)
plt.ylabel(
    "Average Ride Duration (Minutes)",
    fontsize=11
)

plt.grid(axis="y", linestyle="--", alpha=0.4)

for bar in bars:
    height = bar.get_height()

    plt.text(
        bar.get_x() + bar.get_width() / 2,
        height,
        f"{height:.2f}",
        ha="center",
        va="bottom",
        fontsize=10,
        fontweight="bold"
    )

plt.tight_layout()
plt.show()
plt.close()

# ============================================================
# VISUALIZATION 4
# MONTHLY RIDE TRENDS
# ============================================================

query_monthly_trends = """
SELECT
    month_number,
    COUNT(*) AS total_rides
FROM bike_trips_features
GROUP BY month_number
ORDER BY month_number;
"""

df_monthly_trends = pd.read_sql(
    query_monthly_trends,
    engine
)

months = [
    "Jan", "Feb", "Mar", "Apr",
    "May", "Jun", "Jul", "Aug",
    "Sep", "Oct", "Nov", "Dec"
]

plt.figure(figsize=LINE_FIG_SIZE)

plt.plot(
    df_monthly_trends["month_number"],
    df_monthly_trends["total_rides"],
    marker="o",
    linewidth=2
)

plt.title(
    "Monthly Ride Trends",
    fontsize=14,
    fontweight="bold"
)

plt.xlabel("Month", fontsize=11)
plt.ylabel("Total Rides", fontsize=11)

plt.xticks(range(1, 13), months)

plt.grid(True, linestyle="--", alpha=0.4)

plt.gca().yaxis.set_major_formatter(number_formatter)

plt.tight_layout()
plt.show()
plt.close()


# ============================================================
# VISUALIZATION 5
# MONTHLY RIDE TRENDS BY MEMBER TYPE
# ============================================================

query_monthly_member = """
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
"""

df_monthly_member = pd.read_sql(
    query_monthly_member,
    engine
)

df_monthly_member_pivot = df_monthly_member.pivot(
    index="month_number",
    columns="member_casual",
    values="total_rides"
)

plt.figure(figsize=LINE_FIG_SIZE)

plt.plot(
    df_monthly_member_pivot.index,
    df_monthly_member_pivot["member"],
    marker="o",
    linewidth=2,
    label="Member"
)

plt.plot(
    df_monthly_member_pivot.index,
    df_monthly_member_pivot["casual"],
    marker="o",
    linewidth=2,
    label="Casual"
)

plt.title(
    "Monthly Ride Trends by Member Type",
    fontsize=14,
    fontweight="bold"
)

plt.xlabel("Month", fontsize=11)
plt.ylabel("Total Rides", fontsize=11)

plt.xticks(range(1, 13), months)

plt.grid(True, linestyle="--", alpha=0.4)

plt.legend()

plt.gca().yaxis.set_major_formatter(number_formatter)

plt.tight_layout()
plt.show()
plt.close()


# ============================================================
# VISUALIZATION 6
# RIDE TRENDS BY DAY OF WEEK
# ============================================================

query_day_of_week = """
SELECT
    day_of_week_number,
    COUNT(*) AS total_rides
FROM bike_trips_features
GROUP BY day_of_week_number
ORDER BY day_of_week_number;
"""

df_day_of_week = pd.read_sql(
    query_day_of_week,
    engine
)

days = [
    "Mon", "Tue", "Wed",
    "Thu", "Fri", "Sat", "Sun"
]

plt.figure(figsize=LINE_FIG_SIZE)

plt.plot(
    df_day_of_week["day_of_week_number"],
    df_day_of_week["total_rides"],
    marker="o",
    linewidth=2
)

plt.title(
    "Ride Trends by Day of Week",
    fontsize=14,
    fontweight="bold"
)

plt.xlabel("Day of Week", fontsize=11)
plt.ylabel("Total Rides", fontsize=11)

plt.xticks(range(1, 8), days)

plt.grid(True, linestyle="--", alpha=0.4)

plt.gca().yaxis.set_major_formatter(number_formatter)

plt.tight_layout()
plt.show()
plt.close()

# ============================================================
# VISUALIZATION 7
# RIDE TRENDS BY DAY OF WEEK AND MEMBER TYPE
# ============================================================

query_day_member = """
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
"""

df_day_member = pd.read_sql(
    query_day_member,
    engine
)

df_day_member_pivot = df_day_member.pivot(
    index="day_of_week_number",
    columns="member_casual",
    values="total_rides"
)

plt.figure(figsize=LINE_FIG_SIZE)

plt.plot(
    df_day_member_pivot.index,
    df_day_member_pivot["member"],
    marker="o",
    linewidth=2,
    label="Member"
)

plt.plot(
    df_day_member_pivot.index,
    df_day_member_pivot["casual"],
    marker="o",
    linewidth=2,
    label="Casual"
)

days = [
    "Mon", "Tue", "Wed",
    "Thu", "Fri", "Sat", "Sun"
]

plt.xticks(range(1, 8), days)

plt.title(
    "Ride Trends by Day of Week and Member Type",
    fontsize=14,
    fontweight="bold"
)

plt.xlabel("Day of Week", fontsize=11)
plt.ylabel("Total Rides", fontsize=11)

plt.grid(True, linestyle="--", alpha=0.4)

plt.legend()

plt.gca().yaxis.set_major_formatter(number_formatter)

plt.tight_layout()
plt.show()
plt.close()


# ============================================================
# VISUALIZATION 8
# RIDE TRENDS BY HOUR OF DAY
# ============================================================

query_hourly = """
SELECT
    hour_of_day,
    COUNT(*) AS total_rides
FROM bike_trips_features
GROUP BY hour_of_day
ORDER BY hour_of_day;
"""

df_hourly = pd.read_sql(
    query_hourly,
    engine
)

plt.figure(figsize=LINE_FIG_SIZE)

plt.plot(
    df_hourly["hour_of_day"],
    df_hourly["total_rides"],
    marker="o",
    linewidth=2
)

plt.title(
    "Ride Trends by Hour of Day",
    fontsize=14,
    fontweight="bold"
)

plt.xlabel("Hour of Day", fontsize=11)
plt.ylabel("Total Rides", fontsize=11)

plt.xticks(range(24))

plt.grid(True, linestyle="--", alpha=0.4)

plt.gca().yaxis.set_major_formatter(number_formatter)

plt.tight_layout()
plt.show()
plt.close()


# ============================================================
# VISUALIZATION 9
# RIDE TRENDS BY HOUR OF DAY AND MEMBER TYPE
# ============================================================

query_hourly_member = """
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
"""

df_hourly_member = pd.read_sql(
    query_hourly_member,
    engine
)

df_hourly_member_pivot = df_hourly_member.pivot(
    index="hour_of_day",
    columns="member_casual",
    values="total_rides"
)

plt.figure(figsize=LINE_FIG_SIZE)

plt.plot(
    df_hourly_member_pivot.index,
    df_hourly_member_pivot["member"],
    marker="o",
    linewidth=2,
    label="Member"
)

plt.plot(
    df_hourly_member_pivot.index,
    df_hourly_member_pivot["casual"],
    marker="o",
    linewidth=2,
    label="Casual"
)

plt.title(
    "Ride Trends by Hour of Day and Member Type",
    fontsize=14,
    fontweight="bold"
)

plt.xlabel("Hour of Day", fontsize=11)
plt.ylabel("Total Rides", fontsize=11)

plt.xticks(range(24))

plt.grid(True, linestyle="--", alpha=0.4)

plt.legend()

plt.gca().yaxis.set_major_formatter(number_formatter)

plt.tight_layout()
plt.show()
plt.close()


# ============================================================
# END OF FILE
# ============================================================

print("=" * 60)
print("All visualizations generated successfully.")
print("=" * 60)