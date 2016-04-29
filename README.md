# exercise_2
W205 Exercise 2

This Twitter streaming application will use Storm in combination with a Postgres database to capture real time wordcounts from streaming tweets.

# Deployment
To deploy the application, start an AWS EC2 instance using the community AMI 'UCB W205 Spring Ex 2 Image.' Also, attach the required EBS volume with device name = '/dev/xvdf/'.

After connecting to the running instance via SSH, git clone the following repositories into the root directory:
- https://github.com/rtimothyweeks/exercise_2
- https://github.com/UC-Berkeley-I-School/w205-spring-16-labs-exercises

Executing the bash script exercise_2/setup.sh will install all required packages as well as create a Postgres user and target table.

The only remaining step is to update EXTwoTweetwordcount/src/tweets.py with Twitter API credentials, then use sparse run within EXTwoTweetwordcount to begin streaming.

Serving scripts 'finalresults.py' and 'histogram.py' can be used to explore results stored in Postgres. Passing a single word to finalresults will return the total wordcount for that term; execution without an argument will return all wordcount results. The histgram script requires two integer arguments and will return all words with counts between the two arguments.
