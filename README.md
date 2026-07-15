               Cyclistic Bike Share Analysis 





## Project Overview

Cyclistic is a Chicago bike-share company with two types of riders: casual riders who pay per ride, and annual members who pay a yearly fee. Members bring in steadier, more predictable revenue, so converting casual riders to members matters to the business.
This project uses twelve months of trip data to compare how casual riders and members actually use the bikes. SQL handles the data prep and analysis; Python (mainly Matplotlib) handles the charts. The goal is to turn ridership patterns into business recommendations the marketing team can act on.


## Business Problem and Dataset
Cyclistic's marketing team wants more casual riders to convert to annual memberships. The question driving this analysis:
How do casual riders and members use Cyclistic bikes differently, and what could push casual riders toward buying a membership?

The data comes from the Cyclistic trip history used in the Google Data Analytics Professional Certificate capstone project.
Details:

- Twelve monthly CSV files, one full year
- Millions of individual rides
- Loaded into PostgreSQL for analysis

Fields used: 
- ride ID 
- bike type 
- start/end time
- start/end station
- coordinates
- rider type (casual or member)

## Tools Used


| Tool | Purpose |
| :--- | :--- |
| PostgreSQL | Storage and querying |
| SQL | Cleaning, feature engineering, EDA |
| Python / Pandas | Data manipulation |
| Matplotlib | Charts |
| SQLAlchemy | Connects Postgres to Python |
| Git / GitHub | Version control, hosting |

## Data Cleaning

Before analysis, I checked the data for:
- Missing values
- Duplicate rows
- Correct data types
- Invalid ride durations (removed)


## Feature Engineering
Feature Engineering

New columns added to support the analysis:

- Ride duration
- Day of week
- Month
- Hour of day
- Season

These columns made it possible to look at when people ride, not just how often.
## Exploratory Data Analysis
Using SQL, I looked at:

- Total rides by rider type
- Average ride duration
- Bike type preference
- Monthly and weekly trends
- Hourly distribution
## Visualizations
Charts built in Matplotlib cover total rides by rider type, average duration by rider type, bike type preference, monthly and weekly trends, hourly distribution, ride duration distribution, and seasonal trends.
<img width="600" height="616" alt="01_Distribution of rides by member type" src="https://github.com/user-attachments/assets/c786a662-089e-4282-8381-717cf91f9aaf" />
<img width="600" height="616" alt="02_Distribution of rides by bike type" src="https://github.com/user-attachments/assets/5d2466e2-f967-4776-b5ca-7dd456d99b89" />
<img width="600" height="616" alt="03_Average ride duration by member type" src="https://github.com/user-attachments/assets/ff23b62c-ee1b-4111-a040-3825dee11558" />
<img width="600" height="616" alt="04_Monthly ride trends" src="https://github.com/user-attachments/assets/de584826-8123-4d23-8f4e-f7b2e937b752" />
<img width="600" height="616" alt="05_Monthly ride trends by member type" src="https://github.com/user-attachments/assets/daf7c7fa-e019-4f60-9314-fad23b5d935a" />
<img width="600" height="399" alt="06_Ride trends by day of week" src="https://github.com/user-attachments/assets/82356b98-b4a0-48cf-b50d-b6dfe4c64b6e" />
<img width="600" height="616" alt="07_Ride trends by day of week and member type" src="https://github.com/user-attachments/assets/7510a94c-7600-4824-a223-88ee3af40358" />
<img width="600" height="616" alt="08_Ride trends by hour of day" src="https://github.com/user-attachments/assets/2eb07abe-0b13-4803-b799-2bcbe564bfab" />
<img width="600" height="616" alt="09_Ride trends by hour of day and member type" src="https://github.com/user-attachments/assets/5c9e0ea0-3bcc-451d-aed0-fea83455245b" />

## Key Findings

- Members took more total rides than casual riders.
- Casual riders individual rides lasted longer on average.
- Both groups preferred electric bikes.
- Ridership rose in summer.
- Members rode mostly on weekdays, likely commuting.
- Casual riders rode more on weekends, likely recreational use.
- Ride times throughout the day varied for both groups.
## Recommendations

1. Target casual riders with long rides. These riders may already be getting enough value to justify a membership. Show them the cost savings directly.
2. Run weekend-focused membership campaigns. Weekends are when casual riders are most active, so that's when a pitch is most likely to land.
3. Build electric bike perks into membership. Both groups already prefer e-bikes; membership-only e-bike access or discounts could tip the decision.
4. Add flexible membership tiers. Monthly, seasonal, or weekend-only plans lower the commitment barrier compared to a full annual membership.
