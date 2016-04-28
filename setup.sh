#!/bin/bash
mount -t ext4 /dev/xvdf/ /data
bash /data/start_postgres.sh
sudo -u postgres createuser root -s
mv /usr/bin/python /usr/bin/python266
ln -s /usr/bin/python2.7 /usr/bin/python
sudo curl -o ez_setup.py https://bootstrap.pypa.io/ez_setup.py
python ez_setup.py
/usr/bin/easy_install-2.7 pip
pip install redis
pip install virtualenv
pip install streamparse
pip install --upgrade pip
pip install psycopg2
pip install tweepy
sparse quickstart EXTwoTweetwordcount
cp 'w205-spring-16-labs-exercises/exercise_2/tweetwordcount/src/spouts/tweets.py' 'EXTwoTweetwordcount/src/spouts/tweets.py'
cp 'w205-spring-16-labs-exercises/exercise_2/tweetwordcount/src/bolts/parse.py' 'EXTwoTweetwordcount/src/bolts/parse.py'
cp 'w205-spring-16-labs-exercises/exercise_2/Twittercredentials.py' 'EXTwoTweetwordcount/Twittercredentials.py'
cp 'w205-spring-16-labs-exercises/exercise_2/hello-stream-twitter.py' 'EXTwoTweetwordcount/hello-stream-twitter.py'
cp 'w205-spring-16-labs-exercises/exercise_2/psycopg-sample.py' 'EXTwoTweetwordcount/psycopg-sample.py'
rm EXTwoTweetwordcount/topologies/*.clj
cp 'exercise_2/EX2tweetwordcount.clj' 'EXTwoTweetwordcount/topologies/EX2tweetwordcount.clj'
cp 'exercise_2/wordcount.py' 'EXTwoTweetwordcount/src/bolts/wordcount.py'
