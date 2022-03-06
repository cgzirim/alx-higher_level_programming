#!/usr/bin/python3
"""Lists all cities of a state, using the database hbtn_0e_4_usa.
Usage: ./5-filter_cities.py <msql username> <msql password> <database name> \
                                                        <statename>
"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM cities as c \
            INNER JOIN states as s \
            ON c.state_id = s.id \
            ORDER BY c.id ASC")
    print(", ".join([ct[2] for ct in c.fetchall() if ct[4] == argv[4]]))
