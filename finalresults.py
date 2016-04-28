import sys
import psycopg2

con = psycopg2.connect(database='postgres')
cur = con.cursor()

def qry(word):
  if word is None:
    q = ''
  else:
    count = cur.execute("select count from Tweetwordcount where word='%s';" % word)
  return "Total number of occurences of '%s': %s" % (word, count))
  
qry(sys.argv[1])
