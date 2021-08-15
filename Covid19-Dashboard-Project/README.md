# COVID-19 Dash board Project

* #### docker-compose 이용하여 elasticsearch-kibana server 구성

```yaml
version: "3.3"
services:
  elasticsearch:
    image: docker.elastic.co/elasticsearch/elasticsearch:7.14.0
    container_name: elasticsearch
    restart: always
    environment:
      - xpack.security.enabled=false
      - discovery.type=single-node
      - "ES_JAVA_OPTS=-Xms512m -Xmx512m"
    ulimits:
      memlock:
        soft: -1
        hard: -1
      nofile:
        soft: 65536
        hard: 65536
    cap_add:
      - IPC_LOCK
    volumes:
      - elasticsearch-data:/usr/share/elasticsearch/data
    ports:
      - 9200:9200
  kibana:
    container_name: kibana
    image: docker.elastic.co/kibana/kibana:7.14.0
    restart: always
    environment:
      - ELASTICSEARCH_HOSTS=http://elasticsearch:9200    # address of elasticsearch docker container which kibana will connect
    ports:
      - 5601:5601
    depends_on:
      - elasticsearch                                   # kibana will start when elasticsearch has started
volumes:
  elasticsearch-data:
```



#### 데이터 소스

https://datahub.io/core/covid-19



![covid19_dashboard](C:\Users\user\JIKMAN\data-engineer\Covid19-Dashboard-Project\covid19_dashboard.PNG)

