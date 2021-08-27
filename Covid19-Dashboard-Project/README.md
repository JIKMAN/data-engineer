

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



* #### 데이터 소스

데이터 소스를 살펴보면 데이터 row는 총 156239개로 **Date, Country, Confirmed, Recovered, Deaths**로 구성되어 있고, 코로나가 발생한 날로부터 현재 날짜인 21년 8월 3일까지의 확진자 수, 회복자 수, 사망자 수가 나라별로 표기되어 있다. 

출처 - https://datahub.io/core/covid-19



* #### Index Mapping

저용량의 데이터는 엘라스틱서치에 자체적으로 업로드하여 인덱스를 생성할 수 있다.

자동으로 매핑을 지정해주지만, 현재 데이터 타입에 long까지 지정할 필요는 없어보여, 메모리를 절약하기 위해 **integer**로 변경해 주었다.

![index-setting](../img/index-setting.png)



* #### Create index pattern

생성한 Covid-19 Index의 인덱스 패턴을 생성해준다.

날짜 필드는 timestamp로 지정한 후 인덱스 패턴을 생성해주면 데이터 조회가 가능하다.

![search](../img/dovid-data.png)



* #### Visualization

visualize library를 이용하여, 원하는 데이터를 조회해 시각화 자료를 생성해주었다.

![image-20210827214806735](../img/visual.png)



* #### Update Data

시각화 자료를 만들다 보니, 국내 2021-07-26 데이터가 2021-07-25 데이터와 동일하게 나타나 있는 오류를 발견하였다. 

의미있는 데이터라 생각하여 삭제하지 않고, 전날과 다음날 데이터 값의 평균으로 대체해 주었다.

```sh
# 데이터 수정
# PUT 명령어로도 가능하지만, _update를 이용하면 원하는 필드만 지정해서 변경할 수 있다.

POST covid19-time/_update/QJiVh3sBAmil_3VJbMjF
{
  "doc": {
    "Confirmed" : 191797,
    "Deaths" : 2080,
    "Recovered" : 168930
  }
}
```

![update](../img/update.png)

다시한번 조회 해보면

```bash
GET covid19-time/_search
{
  "query": {
    "bool": {
      "must": [
        {
          "match": {
            "Date": "2021-07-26"
          }
        },
        {
          "match": {
            "Country/Region": "Korea, South"
          }
        }
      ]
    }
  }
}
```

정상적으로 변경되었음을 확인할 수 있다.

![update-complete](../img/update-complete.png)



이후, 필요한 자료들을 조회해서 잘못된 데이터들을 몇번 더 수정해주고,

또한, 지도 서비스를 이용하기 위해 공식 문서를 찾아본 결과 ISO 3166 code, 위경도 등 다양한 방법으로 지도 표시가 가능했는데, Country 필드의 타입을 **"geo_point"**로 변경해 country name을 이용해 지도에 표시하였다.

참고 - 공식문서[(https://maps.elastic.co/#file/world_countries)](https://maps.elastic.co/#file/world_countries)

이렇게 해서,

* 현재 날짜 까지의 전세계 감염자 수 및 사망자 수 / 국내 감염자 수, 사망자 수
* 전세계 확진자 수 Top 5 국가
* 국내 및 해외의 일일 감염자 수의 추이 비교
* 나라별 감염/회복/사망 인원을 나타내는 지도

를 나타내는 covid19 대시보드를 완성하였다.

* #### Dashboard

![dashboard](./covid19_dashboard.png)



