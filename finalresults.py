import sys
import psycopg2

con = psycopg2.connect(database='postgres')
cur = con.cursor()

# t = cur.execute('select * from Tweetwordcount limit 20;')
# print t
def qry(argv):
  print argv
  if len(argv) == 1:
    q = 'select word, count from Tweetwordcount order by count desc;'
    cur.execute(q)
    for pair in cur:
      print pair
  else:
    word = argv[1]
    q = "select count from Tweetwordcount where word='%s';" % word
    # print q
    cur.execute(q)
    count = cur.fetchall()[0][0]
    # print count
    print "Total number of occurences of '%s': %s" % (word, count)
  
qry(sys.argv)
