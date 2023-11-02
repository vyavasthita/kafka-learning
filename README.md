# kafka-learning
Learning Kafka

Event driven architecture also works as common communication layer.
Kafka stores data locally like cache to avoid network call.

Without Kafka, we need to remember the connection details of different systems.
Like Http methods, schema, request/response structure etc. But with Kafka, which is a command layer
between different systems, we need to just remember the kafka structure.

# References
TBD

## Zookeeper ;-
    - It manages brokers and keeps metadata information about kafka cluster in the form of key value pair.
    - It keeps communicating with each broker and getting its status. Each broker sends heartbeat to zookeeper after a particular interval.
    - It helps in controller election in kafka cluster.
    - A set of zookeepers nodes working together to manage other distributed systems is known as zookeper cluster.

### Commands;-
Connect to kafka broker:
    docker exec -it kafka-1 bash

Create topic:
    kafka-topics --create --topic <topic_name> --bootstrap-server kafka-1:9093,kafka-2:9094 --partitions 2 --replication-factor 1

List topics:
    kafka-topics --bootstrap-server kafka-1:9093,kafka-2:9094 --list

Describe topic:
    kafka-topics --bootstrap-server kafka-1:9093,kafka-2:9094 --describe <topic_name>

Create producer:
    kafka-console-producer --bootstrap-server kafka-1:9093 --topic <topic_name>

Create consumer:
    kafka-console-consumer --bootstrap-server kafka-1:9093  --topic <topic_name> --from-beginning

See consumer group:
    kafka-consumer-group --bootstrap-server kafka-1:9093  --list

### Intro ;-
    - In Kafka, there is only one controller node.
    - Kafka message contains Key binary, value binary, compression type, timestamp, headers (optional).
    - Kafka accepts only bytes as input from producers and sends bytes as output to consumers. Hence data gets serialized (data to bytes) before it is send to topic. Key and values are serialized. Kafka has common serializers.

### Kafka cluster;-
    - Set of brokers
    - It has only one controller node (broker)

    Scalable:
        - We can add more brokers in kafka cluster without any downtime. This is called horizontal scaling.

    Fault tolerant:
        - Kafka cluster can handle failures because of its distributed nature.
    
    Performance:
        - Kafka has high throughput for both publishing and subscribing messages.

    No Data loss:

    Zero down time:

### Brokers;-
    - Each broker is identified by an ID (integer).
    - We can add more brokers in a kafka cluster without any downtime.
    - Brokers are software processes who manage the topics and messages in the topics.
    - Brokers also manages the consumers by keeping information about the consumers that consumers have read
      these messages from topics/partitions and these are yet to read by using consumer offsets.
    - Replicas are not used for read or write data. They are used for backup.
    - Leader: Broker which is responsible for providing read/write support among the replicated brokers.
    - Partitions can be increased but not decreased due to data loss. At a time only one broker can be leader of a partition. Other brokers will replicate the data. Hence each parition has one leader and multiple ISR(in sync replica).

### Producers ;-
    - Producers produce message at topic level or partition level.

### Topics ;-

#### Partitions ;-
    - Kafka topics are immutable. Once data is written into a partition, it can not be changed.
    - Each message in a partition has a unique id known as offset.
    - Data is kept for a limited period of time (default 1 week, configurable).
    - Order is guaranteed withing a partition (not across partitions).
    - Data is assigned to a partition, unless a key is provided.

### Consumer Group ;-
    - A consumer group is a group of related consumers who perform a similar task.

### Consumers ;-
    - Consumers consume message at topic level or partition level.    
    - Consumers deserializes bytes into data.
    - Consumers are always associated with one consumer group.
    - Consumers pull data from kafka.
    - Data can be read by N number of consumers. When consumer receives the message it does not send the acknowledge back to broker.
    - If we have more consumers (in a consumer group) than the no of partitions, than the extra consumers will be inactive.
    - Kafka stores the offsets at which a consumer group is reading.

### Working ;-
    - By default messages are sent to different partitions in round robin fashion. If we use key, then we can send messages to a particular partition.

    Offset - sequential id for each message in a partition.

    Current Offset : Kafka sends number of messages to consumers, the last message offset is called current offset.

    Commit Offset: Consumer after reading the messages, sends commit acnoledgement to kafka cluster, the index of offset is called commit offset.

    a) Auto commit
    b) Manual Commit - 
        - Send commit offset at the end of all messages read.
        - Send commit offset for each message being read.
