FROM docker.io/bitnami/spark:3-debian-10
USER root

RUN mkdir -p /var/lib/apt/lists/partial
RUN apt-get update && apt-get install -y kafkacat
RUN pip install pyspark kafka-python
RUN curl https://repo1.maven.org/maven2/org/apache/spark/spark-streaming-kafka_2.11/1.6.3/spark-streaming-kafka_2.11-1.6.3.jar  --output /opt/bitnami/spark/jars/spark-streaming-kafka_2.11-1.6.3.jar