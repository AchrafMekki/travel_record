
CREATE DATABASE travelrecord;

\c travelrecord


CREATE SCHEMA travel;

SET search_path TO travel;


CREATE USER tourist_user WITH PASSWORD 'touristuser';


GRANT USAGE ON SCHEMA travel TO tourist_user;
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA travel TO tourist_user;
ALTER DEFAULT PRIVILEGES IN SCHEMA travel GRANT SELECT, INSERT, UPDATE, DELETE ON TABLES TO tourist_user;


CREATE TYPE travel.rating_enum AS ENUM ('1 Star', '2 Stars', '3 Stars', '4 Stars', '5 Stars');
CREATE TYPE travel.satisfaction_enum AS ENUM ('Very Unsatisfied', 'Unsatisfied', 'Neutral', 'Satisfied', 'Very Satisfied');


CREATE TABLE travel.rating (
    rating_id SERIAL PRIMARY KEY,
    rating_value travel.rating_enum NOT NULL
);

CREATE TABLE travel.satisfaction_level (
    satisfaction_id SERIAL PRIMARY KEY,
    satisfaction_value travel.satisfaction_enum NOT NULL
);

CREATE TABLE travel.tourist_details (
    tourist_id SERIAL PRIMARY KEY,
    first_name VARCHAR(40) NOT NULL,
    last_name VARCHAR(40),
    gender VARCHAR(15),
    age SMALLINT,
    occupation VARCHAR(100),
    nationality VARCHAR(100),
    language VARCHAR(20)[]
);

CREATE TABLE travel.country (
    country_id SERIAL PRIMARY KEY,
    country_name VARCHAR(50) UNIQUE NOT NULL
);

CREATE TABLE travel.city (
    city_id SERIAL PRIMARY KEY,
    country_id INT REFERENCES travel.country(country_id),
    city_name VARCHAR(50) NOT NULL
);

CREATE TABLE travel.travel_info (
    travel_id SERIAL PRIMARY KEY,
    tourist_id INT REFERENCES travel.tourist_details(tourist_id),
    country_id INT REFERENCES travel.country(country_id),
    year INTEGER NOT NULL,
    hotel VARCHAR(100),
    transportation VARCHAR(40)[],
    total_duration INTERVAL,
    total_cost NUMERIC(10, 2),
    currency VARCHAR(3), 
    trip_type VARCHAR(30),
    preferred_language VARCHAR(30),
    rating INT REFERENCES travel.rating(rating_id), 
    satisfaction_level INT REFERENCES travel.satisfaction_level(satisfaction_id)
);


ALTER TABLE travel.rating OWNER TO tourist_user;
ALTER TABLE travel.satisfaction_level OWNER TO tourist_user;
ALTER TABLE travel.tourist_details OWNER TO tourist_user;
ALTER TABLE travel.country OWNER TO tourist_user;
ALTER TABLE travel.city OWNER TO tourist_user;
ALTER TABLE travel.travel_info OWNER TO tourist_user;