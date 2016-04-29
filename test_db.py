import psycopg2

conn = psycopg2.connect(database="postgres")
cur = conn.cursor()

cur.execute("INSERT into Tweetwordcount VALUES ('test',989);")
conn.commit()
cur.execute("select * from Tweetwordcount;")
cur.fetchall()
conn.close()
