import sqlite3
import getpass


def main():
    create_user(4,'pepe','superclave')
    
def main2():
    username = input('Username: ')
    password = getpass.getpass('Password: ')
    
    
    if check_users(username, password):
        print('Login correct')
    else:
        print('ERROR!')
        
def check_users(username,password):
    conn = sqlite3.connect('app.db')
    cursor = conn.cursor()
    
    query = f'SELECT id FROM users WHERE username = {username} AND password = {password}'
    print(query)
    rows = cursor.execute(query)
    data = rows.fetchone()
    cursor.execute
    cursor.close()
    conn.close()

def create_user(id,username,password):
    conn = sqlite3.connect('app.db')
    cursor = conn.cursor()
    
    query = f'INSERT INTO users{id,username,password} VALUE({id}, {username}, {password})'
    
    rows = cursor.execute(query)
    print(type(rows))

    cursor.close()
    conn.close()


if __name__ == '__main__':
    main()
conn = sqlite3.connect('app.db')
#cursor --> variable que contiene múltiples datos
cursor = conn.cursor()
rows = cursor.execute('SELECT * FROM users WHERE username="bye"')
for row in rows:
    print(row)
cursor.close()

conn.close()