import sqlite3
conn = sqlite3.connect('my.sqlite')
c = conn.cursor()
def add_user(username,userpass):
    c.execute("INSERT INTO users (name,password) VALUES ('%s','%s')"%(username,userpass))
    conn.commit()
name = input("Введите Логин\n")
passwd = input("Введите Пароль\n")
print('\n')
print("Список пользователей:\n")
add_user(name,passwd)
c.execute('SELECT * FROM users')
row = c.fetchone()
while row is not None:
   print("id:"+str(row[0])+" Логин: "+row[1]+" | Пароль: "+row[2])
   row = c.fetchone()
c.close()
conn.close()
