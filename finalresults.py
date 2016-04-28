import sys
import psycopg2

con = psycopg2.connect(database='postgres')
cur = con.cursor()

def qry(word):
  if word is None:
    q = ''
  else:
    q = "select count from Tweetwordcount where word='%s';" % word
    print q
    count = cur.execute(q)
    print count
  print "Total number of occurences of '%s': %s" % (word, count)
  
qry(sys.argv[1])
