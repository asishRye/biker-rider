from kafka import KafkaProducer

TOPIC_NAME = "demo"
KAFKA_SERVER = "localhost:9092"

producer = KafkaProducer(bootstrap_servers=KAFKA_SERVER)

produceMessage(message):
    producer.send(TOPIC_NAME, message)
    producer.flush()
