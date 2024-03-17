#!/usr/bin/python3
"""script that lists all states with a name starting with N (upper N)
   from the database hbtn_0e_0_usa"""

import sys
import MySQLdb


if __name__ == "__main__":
    con = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                          passwd=sys.argv[2], db=sys.argv[3], charset='utf8')
    cursor = con.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ")
    rows = cursor.fetchall()
    [print(row) for row in rows]
    cursor.close()
    con.close()
