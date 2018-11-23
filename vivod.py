import sqlite3
conn = sqlite3.connect('my.sqlite')
c = conn.cursor()
c.execute('SELECT * FROM users')
row = c.fetchone()
while row is not None:
   print("id:"+str(row[0])+" Логин: "+row[1]+" | Пароль: "+row[2])
   row = c.fetchone()
c.close()
conn.close()