import psycopg2
import sys

con = psycopg2.connect(database="postgres")
cur = con.cursor()

if len(sys.argv) < 3:
  print 'Insufficient arguments provided'
  sys.exit()

start = sys.argv[1]
end = sys.argv[2]
q = 'select word, count from Tweetwordcount where count between %s and %s
order by count desc;' % (start,end)

cur.execute(q)
cur.fetchall()
