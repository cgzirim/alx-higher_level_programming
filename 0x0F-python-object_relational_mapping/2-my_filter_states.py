#!/usr/bin/python3
"""Displays all values in the states table of hbtn_0e_0_usa where name
matches the argument.
Usage: 2-my_filter_states.py <mysql username> <mysql password> <database name>
"""
from sys import argv
import MySQLdb


if __name__ == "__main__":
	db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
	passwd=argv[2], db=argv[3])
	cur = db.cursor()
	cur.execute("SELECT * FROM states \
		WHERE name = '{}' \
		ORDER BY id ASC".format(argv[4]))
	[print(row) for row in cur.fetchall()]
	cur.close()
	db.close()
