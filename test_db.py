import psycopg2

conn = psycopg2.connect(database="postgres")
cur = conn.cursor()

word = 'RTW_test6'
cur.execute("INSERT into Tweetwordcount VALUES ('%s',989);" % word)
conn.commit()
cur.execute("select count from Tweetwordcount where word='%s';" % word)
print cur.fetchone()[0]
conn.close()
