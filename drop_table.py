import psycopg2

conn = psycopg2.connect(database="postgres")
cur = conn.cursor()

cur.execute('TRUNCATE TABLE Tweetwordcount;')
conn.commit()
conn.close()
