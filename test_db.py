import psycopg2

conn = psycopg2.connect(database="postgres")
cur = conn.cursor()

word = 'RTW_test2'
cur.execute("INSERT into Tweetwordcount VALUES ('%s',989);" % word)
conn.commit()
cur.execute("select * from Tweetwordcount where word='%s';" % word)
print cur.fetchall()
conn.close()
