## Elasticsearch 데이터 처리

* Elasticsearch는 데이터 저장 형식으로 json 도큐먼트를 사용한다.
* Elasticsearch는 http 프로토콜로 접근이 가능한 REST API를 지원한다.
  자원별로 고유 URL로 접근이 가능하며, http 메서드 PUT, POST, GET, DELETE 를 이용해서 자원을 처리한다.(이런 특성을 가진 시스템을 보통 **RESTFul** 한 시스템이라고 함)

---

Elasticsearch에서는 도큐먼트 접근 URL이

`http://<호스트>:<포트>/<인덱스>/_doc/<도큐먼트 id> `

구조로 되어있다. (7.x 버전 이후)



#### 입력(PUT)

```bash
# my_index/_doc/1 에 도큐먼트 입력

$ curl -XPUT "http://localhost:9200/my_index/_doc/1" -H 'Content-Type: application/json' -d'
{
  "name": "Jungik",
  "message": "안녕하세요"
}'

{"_index":"my_index","_type":"_doc","_id":"1","_version":1,"result":"created","_shards":{"total":2,"successful":1,"failed":0},"_seq_no":0,"_primary_term":1}
```



#### 조회(GET)

```bash
# my_index/_doc/1 도큐먼트 조회
GET my_index/_doc/1
```



#### 삭제(DELETE)

```bash
# my_index/_doc/1 도큐먼트 삭제
DELETE my_index/_doc/1

# my_index 인덱스 전체 삭제
DELETE my_index
```



#### 수정(POST)

```bash
# POST 명령으로 my_index/_doc 도큐먼트 입력
POST my_index/_doc
{
  "name":"Jungik Kim",
  "message":"안녕하세요"
}
```



#### bulk API

```bash
_bulk 명령 실행
POST _bulk
{"index":{"_index":"test", "_id":"1"}}
{"field":"value one"}
{"index":{"_index":"test", "_id":"2"}}
{"field":"value two"}
{"delete":{"_index":"test", "_id":"2"}}
{"create":{"_index":"test", "_id":"3"}}
{"field":"value three"}
{"update":{"_index":"test", "_id":"1"}}
{"doc":{"field":"value two"}}
```

해당 내용을 bulk.json 파일에 저장

```bash
# bulk.json 파일 내용을 _bulk로 실행, 파일 이름 앞에는 @ 문자 입력

$ curl -XPOST "http://localhost:9200/_bulk" -H 'Content-Type: application/json' --data-binary @bulk.json
```



#### Search API

```bash
# URI 검색으로 test 인덱스에서 "value" 검색, q='검색어'
GET test/_search?q=value

# "value AND three" 검색
# AND / OR / NOT 사용가능. 반드시 대문자로 입력
GET test/_search?q=value AND three

# "field" 필드에서 검색어 "value" 검색
GET test/_search?q=field:value
```

* __relevancy__(정확도)가 가장 높은 문서 10개가 나타남


#### 데이터 본문(Data Body) 검색

```bash
# 데이터 본문 검색으로 "field" 필드에서 검색어 "value" 검색
GET test/_search
{
  "query": {
    "match": {
      "field": "value"
    }
  }
}
```



#### 멀티테넌시(Multitenancy)

한번에 검색

```bash
# 쉼표로 나열해서 여러 인덱스 검색
GET logs-2018-01,2018-02,2018-03/_search

# 와일드카드 * 를 이용해서 여러 인덱스 검색
GET logs-2018-*/_search
```

