# kafka-learning
Learning Kafka


# References

docker exec -it kafka-1 bash

Zookeeper ;-
- It manages brokers and keeps metadata information about kafka cluster in the form of key value pair.
- It helps in controller election in kafka cluster.


Create topic;-

kafka-topics --create --topic newtopic --bootstrap-server kafka-1:29092,kafka-2:39092,kafka-3:49092 --partitions 4 --replication-factor 2

In Kafka, there is only one controller node.

Each broker is identified by an ID (integer).

Kafka topics are immutable. Once data is written into a partition, it can not be changed.

Data is kept for a limited period of time (default 1 week, configurable).

Order is guaranteed withing a partition (not across partitions).

Data is assigned to a partition, unless a key is provided.

Kafka message contains Key binary, value binary, compression type, timestamp, headers (optional).

Kafka accepts only bytes as input from producers and sends bytes as output to consumers. Hence data gets serialized (data to bytes) before it is send to topic. Key and values are serialized. Kafka has common serializers.

Brokers;-
- We can add more brokers in a kafka cluster without any downtime.

Consumers deserializes bytes into data.

Consumers are always associated with one consumer group.

Consumers pull data from kafka.

Replicas are not used for read or write data. They are used for backup.

If we have more consumers (in a consumer group) than the no of partitions, than the extra consumers will be inactive.

Kafka stores the offsets at which a consumer group is reading.

Leader - Broker which is responsible for providing read/write support among the replicated brokers.
Partitions can be increased but not decreased due to data loss. At a time only one broker can be leader of a partition. Other brokers will replicate the data. Hence each parition has one leader and multiple ISR(in sync replica).

By default messages are sent to different partitions in round robin fashion. If we use key, then we can send messages to a particular partition.

Offset - sequential id for each message in a partition.

Current Offset : Kafka sends number of messages to consumers, the last message offset is called current offset.

Commit Offset: Consumer after reading the messages, sends commit acnoledgement to kafka cluster, the index of offset is called commit offset.

a) Auto commit
b) Manual Commit - 
    - Send commit offset at the end of all messages read.
    - Send commit offset for each message being read.
