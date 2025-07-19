import logging
import signal
import sys

from confluent_kafka import Consumer

c = Consumer(
    {
        "bootstrap.servers": "kafka:9092",
        "group.id": "mygroup",
        "auto.offset.reset": "earliest",
    }
)

c.subscribe(["grafana-alerting"])


# Define a signal handler to close the consumer gracefully
def signal_handler(sig, frame):
    logging.info("Received termination signal, closing consumer...")
    c.close()
    sys.exit(0)


# Register the signal handler for SIGINT and SIGTERM
signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)

while True:
    msg = c.poll(1.0)

    if msg is None:
        continue
    if msg.error():
        logging.error("Consumer error: {}".format(msg.error()))
        print("Consumer error: {}".format(msg.error()))
        continue
    logging.error("Received message: {}".format(msg.value().decode("utf-8")))

# close when got terminated signal
c.close()
