#!/bin/bash
pip install --upgrade pip
pip install psycopg2
sparse quickstart EXTwoTweetwordcount
cp 'w205-spring-16-labs-exercises/exercise_2/tweetwordcount/src/spouts/tweets.py' 'EXTwoTweetwordcount/src/spouts/tweets.py'
cp 'w205-spring-16-labs-exercises/exercise_2/tweetwordcount/src/bolts/parse.py' 'EXTwoTweetwordcount/src/bolts/parse.py'
cp 'w205-spring-16-labs-exercises/exercise_2/tweetwordcount/src/bolts/wordcount.py' 'EXTwoTweetwordcount/src/bolts/wordcount.py'
cp 'w205-spring-16-labs-exercises/exercise_2/Twittercredentials.py' 'EXTwoTweetwordcount/Twittercredentials.py'
cp 'w205-spring-16-labs-exercises/exercise_2/hello-stream-twitter.py' 'EXTwoTweetwordcount/hello-stream-twitter.py'
cp 'w205-spring-16-labs-exercises/exercise_2/psycopg-sample.py' 'EXTwoTweetwordcount/psycopg-sample.py'
cp 'w205-spring-16-labs-exercises/exercise_2/tweetwordcount/topologies/tweetwordcount.clj' 'EXTwoTweetwordcount/topologies/tweetwordcount.clj'
rm EXTwoTweetwordcount/topologies/*.clj
cp 'exercise_2/EX2tweetwordcount.clj' 'EXTwoTweetwordcount/topologies/EX2tweetwordcount.clj'
pip install tweepy
