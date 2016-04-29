import psycopg2

conn = psycopg2.connect(database="postgres")
cur = conn.cursor()

cur.execute("INSERT into Tweetwordcount VALUES ('RTW_test1',989);")
conn.commit()
cur.execute("select * from Tweetwordcount;")
cur.fetchall()
conn.close()
