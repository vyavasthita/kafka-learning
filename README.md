# kafka-learning
Learning Kafka


# References

docker exec -it kafka-1 bash

Create topic;-

kafka-topics --create --topic newtopic --bootstrap-server kafka-1:29092,kafka-2:39092,kafka-3:49092 --partitions 4 --replication-factor 2

In Kafka, there is only one controller node.

Leader - Broker which is responsible for providing read/write support among the replicated brokers.
Partitions can be increased but not decreased due to data loss.

By default messages are sent to different partitions in round robin fashion. If we use key, then we can send messages to a particular partition.

Offset - sequential id for each message in a partition.

Current Offset : Kafka sends number of messages to consumers, the last message offset is called current offset.

Commit Offset: Consumer after reading the messages, sends commit acnoledgement to kafka cluster, the index of offset is called commit offset.

a) Auto commit
b) Manual Commit - 
    - Send commit offset at the end of all messages read.
    - Send commit offset for each message being read.
