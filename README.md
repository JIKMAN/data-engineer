## Roadmap for Studying Data Engineer  

<br>


데이터 엔지니어 학습을 위한 로드맵을
다양한 소스들을 참고해 나름대로 정리해 보았다.  

<br>



> 데이터 엔지니어와 데이터 사이언티스트

데이터 엔지니어는 데이터 분석가와 데이터 사이언티스트와 협업을 한다.  
겹치는 업무도 존재하지만 회사의 성격과 해당 조직의 상황에 따라 달라질 수 있다.  
프로그래밍에 관심이 있다면 데이터 엔지니어, 데이터 분석에 관심이 있다면 데이터 사이언티스트가 더 적합하다고 할 수 있다.

![engineer vs scientist](https://tech.kakao.com/wp-content/uploads/2021/03/01-3.png)

<br>



> 데이터 엔지니어의 역할

데이터 엔지니어는 주로 앱 또는 웹에서 발생하는 데이터들을 파이프라인을 통해 저장소(Database, S3,...)에 저장하고, 대용량 데이터를 수집하고 관리하며 유지하는 일을 담당한다.

데이터 엔지니어의 업무는 주어진 환경에서 최상의 퍼포먼스를 낼 수 있도록 파이프라인을 구축하는 것이다.

![img](https://camo.githubusercontent.com/fbb3e684f6561512d457132d5cdf6c74bea2180583916286bf66b0aeefade61c/68747470733a2f2f7777772e64726f70626f782e636f6d2f732f3572307462623374356666636533692f53637265656e73686f74253230323031382d30372d323225323030392e31342e30352e706e673f7261773d31)
<br>



> 데이터 엔지니어의 역량

아래 역량 밑에 있는 도구들은 도구일 뿐, **모두 알 필요는 없지만**, 특정 기술을 사용할 때 왜 이 도구를 선택했는가?를 항상 고민해보는 습관이 필요하다.

언어와 플랫폼은 "선택"의 문제이고 문제해결을 위한 "도구"라 생각하는 유연한 자세가 중요하다.

#### 1. 수집, 가공, 저장

수많은 서비스에서 생산된 수많은 데이터를 모을 수 있도록 거대한 데이터 파이프라인을 설계, 구축한. 데이터를 가공 하며, 데이터의 성격에 따라 스트리밍 혹은 배치 처리를 한다. 이것을 제대로 하려면 적합한 기술들의 선택과 조화로운 설계가 필요하다.

스트리밍 데이터를 모으기 위해 logstash, fluentd 같은 수집기와 kafka, rabbitMQ 같은 MQ를 사용하고 스트리밍 데이터 가공을 위해 storm, flink, spark streaming 등을 사용한다. 배치 처리는 hadoop MR, hive, spark 등을 사용하며 용도에 따라 다른 기술을 사용하기도 한다. 이런 처리를 하는 환경에서는 프로그래밍이 필요하며 python, scala, java 같은 언어들이 주로 쓰이고 있다. 

- 데이터 수집
  - Apache Kafka, Fluntd, Embulk, Logstash, Redis, Pub/Sub, Kinesis
- 데이터 저장
  - HDFS, json, Parquet, AWS S3 or GCP Storage, RDB, NoSQL, Amazon Redshift, Google BigQuery

#### 2. 분석

저장된 데이터에서 hive 등의 쿼리로 일회성 분석을 하기도 합니다. 그래서 데이터 엔지니어는 쿼리에 대한 이해가 필요합니다. visualization tool 을 통해 self service BI 환경을 개발하기도 한다.

위 두 분석 업무 중 중요한 데이터에 대해서는 서비스 조직에서 수시로 확인할 수 있도록 analytics system을 개발하기도 한다.

- 데이터 처리
  - Apache Hadoop, Apache Spark, Apache Hive, SQL

#### 3. 협업

* 심화된 분석, ML, AI 등을 하는 데이터 사이언티스트들과 협업이 필요하다. 어떤 데이터들을 쓰고 있고, 어떤 데이터들이 필요한지 알아야 일이 원활하게 진행이 되기 때문이다. 더 나아가 데이터 사이언티스트의 업무도 잘 이해한다면 더 좋다.

  서비스 조직과 협업도 필요하다. 예를 들어 서비스에서 개편을 위해 ab test를 한다면 여러 가설을 세우고 실험을 하고 분석을 같이 해야 한다.

  이후 서비스 개편 후에 대한 성과 분석 지표를 analytics system에 나오도록 한다면 이미 수집하고 있는 데이터로 충분한지 확인해보고, 부족하다면 니즈에 맞으며 확장성 있게 데이터를 추가 수집해야 한다.

#### 4. 그 외

- Java, Scala, Python

- 리눅스
- 클라우드 서비스
  - AWS, GCP, Azure, IBM, NBP 등
- Dashboard
  - Metabase, Superset, Zeppelin, Redash, Tableau
- Task Management Tool(Luigi, Airflow...)
- Docker



<br>

> 데이터 파이프라인 실제 적용사례

![twitter-pipeline](https://camo.githubusercontent.com/ba1ed6394839f5e7b4ccfc7a96891102c321ad8909e9793cafecaa600e8f7942/68747470733a2f2f7777772e64726f70626f782e636f6d2f732f783668733938306e666135676262692f53637265656e73686f74253230323031382d30372d323225323030392e31362e30382e706e673f7261773d31)

![uber-pipeline](https://camo.githubusercontent.com/ecbf6a48de2e4d33aa07a7cc2534cc121571cf57139c4853f976fc331fc2de4c/68747470733a2f2f7777772e64726f70626f782e636f6d2f732f6a6662387a717071643466743872352f53637265656e73686f74253230323031382d30362d313525323032312e30372e32312e706e673f7261773d31)



#

> 참고한 자료

* https://github.com/Team-Neighborhood/I-want-to-study-Data-Science/wiki/%EB%8D%B0%EC%9D%B4%ED%84%B0-%EC%97%94%EC%A7%80%EB%8B%88%EC%96%B4
* https://tech.kakao.com/2020/11/30/kakao-data-engineering/

* https://brunch.co.kr/@imagineer/301
