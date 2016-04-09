#Creates database and Tweetwordcount table

import psycopg2

conn = psycopg2.connect(dbname='postgres', user='Tcount', host="localhost", port="5432")
#conn = psycopg2.connect(database="Tcount", user="postgres", password="pass", host="localhost", port="5432")

#Create a Table
cur = conn.cursor()
cur.execute('''CREATE TABLE Tweetwordcount
       (word TEXT PRIMARY KEY     NOT NULL,
       count INT     NOT NULL);''')
conn.commit()
conn.close()
