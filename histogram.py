import psycopg2
import sys

con = psycopg2.connect(database="postgres")
cur = con.cursor()

if len(sys.argv) < 2:
  print 'Insufficient arguments provided'
  sys.exit()
print sys.argv
start = sys.argv[1]
end = sys.argv[2]
q = 'select word, count from Tweetwordcount where count between %s and %s order by count desc;' % (start,end)

cur.execute(q)
for pair in cur:
  print pair
