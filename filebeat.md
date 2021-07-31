* ```bash
  filebeat modules enable system nginx mysql
  ```

* ```shell
  filebeat setup --pipelines --modules system
  ```

```bash
filebeat.inputs:
- type: log
  enabled: true
  paths:
    - /var/log/*.log
    #- c:\programdata\elasticsearch\logs\*
```

```bash
#----------------------------- Logstash output --------------------------------
output.logstash:
  hosts: ["127.0.0.1:5044"]
```



```bash
#-------------------------------Kafka Output-----------------------------------
output.kafka:
  # enabled : true (default: true)

  # initial brokers for reading cluster metadata
  hosts: ["kafka1:9092", "kafka2:9092", "kafka3:9092"]

  # message topic selection + partitioning
  topic: '%{[fields.log_topic]}'
  topics:
    - topic: "critical-%{[agent.version]}"
      when.contains:
        message: "CRITICAL"
    - topic: "error-%{[agent.version]}"
      when.contains:
        message: "ERR"
  partition.round_robin: # 파티션 순서대로 차곡차곡 저장
  # partition.random : 이용 가능한 파티션부터 차례대로 저장
    reachable_only: false 

  required_acks: 1
  compression: gzip # 압출 할건지
  max_message_bytes: 1000000
```

```bash
#--------------------------- ElasticSearch output -----------------------------
output.elasticsearch:
  hosts: ["https://myEShost:9200"] 
  index: "%{[fields.log_type]}-%{[agent.version]}-%{+yyyy.MM.dd}" 
  indices:
    - index: "warning-%{[agent.version]}-%{+yyyy.MM.dd}"
      when.contains:
        message: "WARN"
    - index: "error-%{[agent.version]}-%{+yyyy.MM.dd}"
      when.contains:
        message: "ERR"
```



* ```shell
  filebeat -e
  ```



공식문서 : https://www.elastic.co/guide/en/beats/filebeat/current/index.html

카프카 설정 : https://www.elastic.co/guide/en/beats/filebeat/current/kafka-output.html#topics-option-kafka
