from __future__ import absolute_import, print_function, unicode_literals
import psycopg2
from collections import Counter
from streamparse.bolt import Bolt
from redis import StrictRedis


class WordCounter(Bolt):

    def initialize(self, conf, ctx):
        self.counts = Counter()
        self.redis = StrictRedis()
        self.conn = psycopg2.connect(database="postgres")
        self.cur = self.conn.cursor()

    def process(self, tup):
        word = tup.values[0].replace("'","")
        # Increment the local count
        self.counts[word] += 1
        self.emit([word, self.counts[word]])

        # Log the count - just to see the topology running
        self.log('%s: %d' % (word, self.counts[word]))
        
        # Write codes to increment the word count in Postgres
        # Get and increment current db count
        self.cur.execute("select count from Tweetwordcount where word='%s';" % word)
        count = self.cur.fetchone()
        if count is None:
            self.cur.execute("INSERT into Tweetwordcount VALUES ('%s',%s);" % (word,1))
        else:
            up_count = 1 + count[0]
            self.cur.execute("UPDATE Tweetwordcount SET count=%s WHERE word='%s';" % (up_count, word))

        # Commit count change to db
        self.conn.commit()
