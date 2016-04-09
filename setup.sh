#!/bin/bash
pip install --upgrade pip
pip install psycopg2
sparse quickstart EXTwoTweetwordcount
cp 'w205-spring-16-labs-exercises/exercise_2/tweetwordcount/src/spouts/tweets.py' 'EXTwoTweetwordcount/src/spouts/tweets.py'
cp 'w205-spring-16-labs-exercises/exercise_2/tweetwordcount/src/bolts/parse.py' 'EXTwoTweetwordcount/src/bolts/parse.py'
cp 'w205-spring-16-labs-exercises/exercise_2/Twittercredentials.py' 'EXTwoTweetwordcount/Twittercredentials.py'
cp 'w205-spring-16-labs-exercises/exercise_2/hello-stream-twitter.py' 'EXTwoTweetwordcount/hello-stream-twitter.py'
cp 'w205-spring-16-labs-exercises/exercise_2/psycopg-sample.py' 'EXTwoTweetwordcount/psycopg-sample.py'
rm EXTwoTweetwordcount/topologies/*.clj
cp 'exercise_2/EX2tweetwordcount.clj' 'EXTwoTweetwordcount/topologies/EX2tweetwordcount.clj'
cp 'exercise_2/wordcount.py' 'EXTwoTweetwordcount/src/bolts/wordcount.py'
pip install tweepy
python 'exercise_2/create_db.py'
