import sys
import psycopg2

con = psycopg2.connect(database='postgres')
cur = con.cursor()

# t = cur.execute('select * from Tweetwordcount limit 20;')
# print t
def qry(word):
  if word is None:
    q = ''
  else:
    q = "select count from Tweetwordcount where word='%s';" % word
    # print q
    cur.execute(q)
    count = cur.fetchall()[0][0]
    # print count
  print "Total number of occurences of '%s': %s" % (word, count)
  
qry(sys.argv[1])
