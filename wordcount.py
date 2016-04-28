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
        word = tup.values[0]
        
        # Write codes to increment the word count in Postgres
        # Get and increment current db count
        count = self.cur.execute("select count from Tweetwordcount where word='%s';" % word)
        if count is None:
            count = 0
        else:
            count += 1
        
        # Commit count change to db
        self.cur.execute("UPDATE Tweetwordcount SET count=%s WHERE word='%s';" % (count, word))
        self.conn.commit()

        # Increment the local count
        self.counts[word] += 1
        self.emit([word, self.counts[word]])

        # Log the count - just to see the topology running
        self.log('%s: %d' % (word, self.counts[word]))
