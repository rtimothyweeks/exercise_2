source /opt/py27environment/bin/activate
pip install psycopg2
sparse quickstart EXT2Tweetwordcount

git clone https://github.com/UC-Berkeley-I-School/w205-spring-16-labs-exercises/

cp w205-spring-16-labs-exercises/exercise_2/tweetwordcount/src/spouts/tweets.py EX2Tweetwordcount/src/spouts
cp w205-spring-16-labs-exercises/exercise_2/tweetwordcount/src/bolts/parse.py EX2Tweetwordcount/src/bolts
cp w205-spring-16-labs-exercises/exercise_2/tweetwordcount/src/bolts/wordcount.py EX2Tweetwordcount/src/bolts
cp w205-spring-16-labs-exercises/exercise_2/Twittercredentials.py EX2Tweetwordcount
cp w205-spring-16-labs-exercises/exercise_2/hello-stream-twitter.py EX2Tweetwordcount
cp w205-spring-16-labs-exercises/exercise_2/psycopg-sample.py EX2Tweetwordcount
cp w205-spring-16-labs-exercises/exercise_2/tweetwordcount/topologies/tweetwordcount.clj EX2Tweetwordcount/topologies

pip install tweepy

