## POC for Kafka

A flask webapp serves rider page and biker page. Every click on the map is being translated to a location. This location in latitude and longitude is being pushed to kafka using kafka-python.

A kafka server is running in the background with zookeeper in docker to accept the data.
