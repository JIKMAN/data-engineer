# Elastic Search 데이터 처리

> ### Rest API
>
> Elasticsearch는 http 프로토콜로 접근이 가능한 REST API를 지원합니다. 자원별로 고유 URL로 접근이 가능하며 http 메서드 PUT, POST, GET, DELETE 를 이용해서 자원을 처리합니다. 이런 특성을 가진 시스템을 보통 **RESTFul** 한 시스템이라고 말합니다.



* #### curl 명령어를 통한 REST API

```bash
# GET 메서드로 elasticsearch 클러스터 조회

$ curl "localhost:9200"

{
  "name" : "596526604b77",
  "cluster_name" : "docker-cluster",
  "cluster_uuid" : "NkTqQNV8TNWCPQci3IKn1g",
  "version" : {
    "number" : "7.14.0",
    "build_flavor" : "default",
    "build_type" : "docker",
    "build_hash" : "dd5a0a2acaa2045ff9624f3729fc8a6f40835aa1",
    "build_date" : "2021-07-29T20:49:32.864135063Z",
    "build_snapshot" : false,
    "lucene_version" : "8.9.0",
    "minimum_wire_compatibility_version" : "6.8.0",
    "minimum_index_compatibility_version" : "6.0.0-beta1"
  },
  "tagline" : "You Know, for Search"
}
```



* ### Kibana Dev Tools















* 두가지 쿼리를 동시에 만족시키는 도큐먼트 검색

```http
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

