import psycopg2

conn = psycopg2.connect(database="postgres")
cur = conn.cursor()

# word = 'RTW_test10'
# cur.execute("INSERT into Tweetwordcount VALUES ('%s',989);" % word)
# conn.commit()
cur.execute("select word, count from Tweetwordcount order by count desc limit 20;")
for pair in cur:
  print pair
conn.close()
