import psycopg2 as pg

CONN = pg.connect(
    user="tourist_user",
    password="tourist_user",
    dbname="travelrecord",
    port=5432
)


def fetch_all_tourist_details():
    # query
    query = """
        SELECT * FROM travel.tourist_details;
        """

    # Connection
    with CONN.cursor() as cursor:
        cursor.execute(query)
        all_tourist = cursor.fetchall()
        return all_tourist


def fetch_all_travel_info():
    # query
    query = """
        SELECT * FROM travel.travel_info;
        """

    # Connection
    with CONN.cursor() as cursor:
        cursor.execute(query)
        info = cursor.fetchall()
        return info


def fetch_all_experiences():
    query = """SELECT * FROM travel.travel_info WHERE satisfaction_level = 5;"""
    with CONN.cursor() as cursor:
        cursor.execute(query)
        best_experience = cursor.fetchall()
        return best_experience


def get_travel_info_with_country():
    query = """
                SELECT ti.travel_id, td.tourist_id, td.first_name, td.last_name,
                ti.country_id, c.country_id, ti.year, ti.hotel, ti.total_cost
                FROM travel.travel_info ti
                JOIN travel.tourist_details td ON ti.tourist_id = td.tourist_id
                JOIN travel.country c ON c.country_id = ti.country_id
                LIMIT 10;
            """
    with CONN.cursor() as cursor:
        cursor.execute(query)
        info = cursor.fetchall()
        return info


def expensive_travel_costs():
    query = """
    SELECT
        c.country_name,
        ci.city,
        MAX(ti.total_cost) AS max_total_cost
    FROM
        travel.travel_info ti
    JOIN
        travel.country c ON ti.country_id = c.country_id
    JOIN
        travel.city ci ON c.country_name = ci.country_name
    GROUP BY
        c.country_name,
        ci.city
    ORDER BY
        max_total_cost DESC
    LIMIT 1;"""
    with CONN.cursor() as cursor:
        cursor.execute(query)
        costly = cursor.fetchone()
        return costly


def best_country_to_visit():
    query = """
    SELECT
        c.country_name,
        AVG(ti.total_cost) AS avg_total_cost
    FROM
        travel.travel_info ti
    JOIN
        travel.country c ON ti.country_id = c.country_id
    GROUP BY
        c.country_name
    ORDER BY
        avg_total_cost ASC
    LIMIT 1;
                    """
    with CONN.cursor() as cursor:
        cursor.execute(query)
        best = cursor.fetchall()
        return best
