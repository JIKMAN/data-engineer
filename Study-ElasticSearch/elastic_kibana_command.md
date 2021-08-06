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

