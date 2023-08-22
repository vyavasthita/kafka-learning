# kafka-learning
Learning Kafka


# References

docker exec -it kafka-1 bash

Create topic;-

kafka-topics --create --topic newtopic --bootstrap-server kafka-1:29092,kafka-2:39092,kafka-3:49092 --partitions 4 --replication-factor 3
