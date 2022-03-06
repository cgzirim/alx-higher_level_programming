#!/usr/bin/python3
"""Lists all cities from the database hbtn_0e_4_usa.
Usage: ././4-cities_by_state.py <msql username> <msql password> <database name>
"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    with db.cursor() as cur:
        cur.execute("SELECT cities.id, cities.name, states.name \
            FROM cities LEFT JOIN states \
            ON states.id = cities.state_id \
            ORDER BY id ASC")
        [print(city) for city in cur.fetchall()]
