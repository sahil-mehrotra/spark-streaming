import json
import time
import sys
from kafka import KafkaProducer

KAFKA_TOPIC = ["policy", "customer", "product"]
KAFKA_BROKERS = "localhost:9092"

# Setup producer connection
producer = KafkaProducer(value_serializer=lambda v: json.dumps(v).encode("utf-8"),
                         bootstrap_servers=KAFKA_BROKERS)

print("connected to {} topic {}".format(KAFKA_BROKERS, KAFKA_TOPIC))


def send_to_topic(payload, topic_number):
    """Add a message to the produce buffer asynchronously to be sent to Eventador."""
    try:
        producer.send(KAFKA_TOPIC[topic_number], payload)
    except:
        print("unable to produce to {} topic {}".format(KAFKA_BROKERS, KAFKA_TOPIC[topic_number]))


try:
    POLICIES_FOLDER = "/Users/in-msahil/Desktop/Spark/spark-streaming-exercise/kafka-simulator/sample-policies"
    policy_file_list = ["003-policies_list.json", "004-policies_list.json", "005-policies_list.json", "006-policies_list.json"]
    for file in policy_file_list:
        policy = None
        with open(POLICIES_FOLDER+"/"+file, "r") as policy_file:
            policy = json.load(policy_file)
        print(policy)
        send_to_topic(policy, 0)
        producer.flush()
        time.sleep(0.1)
    CUSTOMER_FOLDER = "/Users/in-msahil/Desktop/Spark/spark-streaming-exercise/kafka-simulator/sample-customers"
    customer_file_list = ["001-customer.json", "002-customer.json"]
    for file in customer_file_list:
        customer = None
        with open(CUSTOMER_FOLDER+"/"+file, "r") as customer_file:
            customer = json.load(customer_file)
        print(customer)
        send_to_topic(customer, 1)
        producer.flush()
        time.sleep(0.1)
    PRODUCT_FOLDER = "/Users/in-msahil/Desktop/Spark/spark-streaming-exercise/kafka-simulator/sample-products"
    customer_file_list = ["001-product.json", "002-product.json"]
    for file in customer_file_list:
        product = None
        with open(PRODUCT_FOLDER+"/"+file, "r") as product_file:
            product = json.load(product_file)
        print(product)
        send_to_topic(product, 2)
        producer.flush()
        time.sleep(0.1)
except KeyboardInterrupt:
    sys.exit()
