import psycopg2

conn = psycopg2.connect(database="postgres")
cur = conn.cursor()

word = 'RTW_test10'
cur.execute("INSERT into Tweetwordcount VALUES ('%s',989);" % word)
conn.commit()
cur.execute("select count from Tweetwordcount where word='%s';" % word)
count = cur.fetchone()[0]
print count
print count > 1
conn.close()
