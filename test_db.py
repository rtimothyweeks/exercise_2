import psycopg2

conn = psycopg2.connect(database="postgres")
cur = self.conn.cursor()

cur.execute("INSERT into Tweetwordcount VALUES ('test',989);")
conn.commit()
print cur.execute("select * from Tweetwordcount;")
conn.close()
