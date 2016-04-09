#!/bin/bash
pip install --upgrade pip
pip install psycopg2
sparse quickstart EX2Tweetcount
cp 'w205-spring-16-labs-exercises/exercise_2/tweetwordcount/src/spouts/tweets.py' 'EX2Tweetcount/src/spouts/tweets.py'
cp 'w205-spring-16-labs-exercises/exercise_2/tweetwordcount/src/bolts/parse.py' 'EX2Tweetcount/src/bolts/parse.py'
cp 'w205-spring-16-labs-exercises/exercise_2/tweetwordcount/src/bolts/wordcount.py' 'EX2Tweetcount/src/bolts/wordcount.py'
cp 'w205-spring-16-labs-exercises/exercise_2/Twittercredentials.py' 'EX2Tweetcount/Twittercredentials.py'
cp 'w205-spring-16-labs-exercises/exercise_2/hello-stream-twitter.py' 'EX2Tweetcount/hello-stream-twitter.py'
cp 'w205-spring-16-labs-exercises/exercise_2/psycopg-sample.py' 'EX2Tweetcount/psycopg-sample.py'
cp 'w205-spring-16-labs-exercises/exercise_2/tweetwordcount/topologies/tweetwordcount.clj' 'EX2Tweetcount/topologies/tweetwordcount.clj'
pip install tweepy
