# Travel_experience
This is a Command Line Application that helps keep track of tourists and their travel records.

## Database Mission Statement
The purpose of travel record Database is to keep track the data of tourists, and to supply information of their traveling experience when needed.

## Database Mission Objectives
1. fetch All Tourist Details
2. fetch All Travel Information
3. fecht Most Expensive Travel Costs by City
4. fetch Best Country to Visit

## How to run
Before running this application, you should first setup the virtual environment, database, environment variables, install packages and optionally add fake data.

### Set up database

**NB**: Open a terminal from the `db` folder in the working directory

```sql
-- Start psql shell from any database and superuser. Preferably postgres
psql -U postgres

-- Create the database 
CREATE DATABASE travelrecord;

-- Connect to the database
\c travelrecord

-- Create the schema 'project'
CREATE SCHEMA travel;


-- Set your path 'travel'
SET search_path TO travel;


-- Run the script to create all tables
\i db_sql/tables.sql

-- OPTIONAL: Insert dummy data to start with 
\i db_sql/insert_country.sql   -- insert country data
\i db_sql/insert_city.sql     -- insert cities data
\i db_sql/insert_rating.sql  -- insert rating  data
\i db_sql/insert_satisfaction_level.sql  -- insert satisfaction data table
\i db_sql/insert_travel_info.sql  -- insert travel informations data
\i db_sql/insert_tourist_details.sql    -- insert all tourist details  data
```
### Set up .env file
Create a `.env` file in the working directory. Copy the text below and change the values if yours is different.

```
db_host=localhost
db_name=travelrecord
db_user=postgres
db_password=postgres
db_port=5432
```

### Set up Virtual Environment
In the working directory, open a terminal and run the following command

```bash
$ python3 -m venv .venv --prompt travel
```
Source the virtual environment

```bash
$ source .venv/bin/activate
```
Install all packages

```bash
$ pip install -r requirements.txt
```

### Start App
From the working directly, run the following command
```bash
$ python3 -m src.main
```
You will be presented with a menu. Continue by selecting the options you want.

