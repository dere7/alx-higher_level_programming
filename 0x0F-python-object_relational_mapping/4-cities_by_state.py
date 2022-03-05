#!/usr/bin/python3
"""
Lists all cities from the database hbtn_0e_4_usa
"""
if __name__ == '__main__':
    import MySQLdb
    from sys import argv
    db = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute('SELECT c.id, c.name, s.name FROM cities c, states s \
            WHERE c.state_id = s.id ORDER BY c.id')
    for row in cur:
        print(row)
