## 데이터에 따른 도구 선정 기준

|                  | __실시간 조회__ | __통계분석__ |
| :--------------- | :-------------: | :----------: |
| 데이터 보관 주기 |    __단기__     |   __장기__   |
| Storage 비용     |     고비용      |    저비용    |
| 데이터 조회 주기 |      잦음       |    주기적    |
| 데이터 처리 과정 |      원본       |  정제, 축소  |
| 요구 성능        |     고성능      |    저성능    |

#### Open source + Cloud platform

* 실시간 조회 : elasticsearch + kibana
* 통계 분석 : spark/emr/dataproc + zeppelin
* legacy data : oracle, mysql, mariadb, redis

#### Cloud platform

* 실시간 + 통계분석
  * aws s3 + athena + quick sight / zeppelin
  * GCS + bigquery + datastudio / quicksight

* legacy data : Amazon aurora, Google spanner



## 파이프라인 설계, 고려사항

#### 데이터 선정, 수집

* 장애 발생에 대한 데이터 처리 보장
* 누락된 데이터 확인을 위한 메타정보 추가
* 데이터 복구 방안

#### 저장, 가공, 분석

* 데이터 사용에 대한 고가용성 보장
* 데이터 처리 후 정합성 체크를 위한 원본 데이터 보관
* 항상 압축 파일 형태를 고민
* 장애에 대한 영향도 전파되지 않도록 구성
* shards, replica 전략

#### 예측 & 자동화



