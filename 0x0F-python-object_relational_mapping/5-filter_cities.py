#!/usr/bin/python3
"""
Takes in the name of a state as an argument and lists all cities of
that state, using the database hbtn_0e_4_usa
"""
if __name__ == '__main__':
    import MySQLdb
    from sys import argv
    db = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute('SELECT c.name FROM cities c, states s WHERE c.state_id = \
            s.id AND s.name = %s ORDER BY c.id', (argv[4],))
    print(', '.join(map(lambda x: x[0], cur)))
