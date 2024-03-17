#!/usr/bin/python3
"""script that takes in the name of a state as an argument and lists all
   cities of that state, using the database hbtn_0e_4_usa"""

import sys
import MySQLdb


if __name__ == "__main__":
    con = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                          passwd=sys.argv[2], db=sys.argv[3], charset='utf8')
    cursor = con.cursor()
    cursor.execute("SELECT c.name FROM cities as c LEFT JOIN states as s \
            ON c.state_id = s.id WHERE s.name = %s ORDER BY c.id \
            ASC", (sys.argv[4], ))
    rows = cursor.fetchall()
    [print(row) for row in rows]
    cursor.close()
    con.close()
