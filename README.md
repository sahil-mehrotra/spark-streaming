# Spark Streaming Sample Project

## Setup

* Run `docker build -f Dockerfile -t  pyspark .` to build a docker image to be used for spark cluster setup
* Run `docker-compose up -d` in the project root to setup the kafka brokers and the spark cluster

## Development

The `spark-apps` folder on the project root will be already mounted on the spark master container under `/mnt/host`. Just `spark-submi` whichever sparkapp.py file needs to run

Run below command in spark node to run your streaming application.

```spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.1.2 /mnt/host/streaming_app.py```

## Note

* The kafka broker will be available as `localhost:9092` on your host.
* To access the broker from within the docker network and in your spark apps use `broker:29092` as the broker address

## Exercise 1

Create a tcp stream using `nc` and listen to its port using the Spark Socket Stream API and try to try to aggregate the counts of selected words in every line of text you send via `nc`

## Exercise 2

Run the Kafka Simulator by running the dockerized cluster and publish events to it by running the `policy-producer.py` file.
Then try to read two of the topics in `["policy", "customer", "product"]`  as df in structured streaming mode and try to do joins on them

## Extra Credit

Setup a twitter streaming `https://developer.twitter.com/en/docs/tutorials/consuming-streaming-data` and try to listen to a specific list of hashtags and do the following:

1. Do aggregations on the count of hashtags over a sliding window of your chosen interval
2. Setup a stateful stream that counts the total number of tweets with a specific hashtag
