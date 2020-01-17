
import psycopg2

connection = psycopg2.connect(dbname="table_db", user="postgres", password="cyberfalcon")

cursor = connection.cursor()

# cursor.execute('''CREATE TABLE test_table (
#     id INTEGER PRIMARY KEY, 
#     completed BOOLEAN NOT NULL DEFAULT False);''')

#cursor.execute('INSERT INTO test_table (id, completed) VALUES(1, true);')
cursor.execute('INSERT INTO test_table (id, completed) VALUES(2, true);')

connection.commit()

cursor.close()
connection.close()



