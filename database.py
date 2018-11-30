import sqlite3
conn = sqlite3.connect('my.sqlite')
c = conn.cursor()
c.execute('''CREATE TABLE users (id int auto_increment primary key,name varchar, password varchar)''')

c.close()
conn.close()

