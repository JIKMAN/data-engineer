## GCP Professional Bigdata Engineer Certification

![gcp](https://image-kr.bespinglobal.com/wp-content/uploads/2018/06/google-cloud-platform.jpg)

1. Your company has recently grown rapidly and now ingesting data at a significantly higher rate than it was previously. You manage the daily batch MapReduce analytics jobs in Apache Hadoop. However, the recent increase in data has meant the batch jobs are falling behind. You were asked to recommend ways the development team could increase the responsiveness of the analytics without increasing costs. What should you recommend they do?

   - Rewrite the job in Pig.

   > **pig**
   >
   > 대용량 빅데이터 처리에 특화된 스크립트 언어

2. You are developing an application that uses a recommendation engine on Google Cloud. Your solution should display new videos to customers based on past views. Your solution needs to generate labels for the entities in videos that the customer has viewed. Your design must be able to provide very fast filtering suggestions based on data from other customer preferences on several TB of data. What should you do?

   * Build an application that calls the Cloud Video Intelligence API to generate labels. Store data in Cloud Bigtable, and filter the predicted labels to match the user's viewing history to generate preferences.

   > [Cloud Video Intelligence API](https://cloud.google.com/video-intelligence)
   >
   > 동영상 분석, 추천, 필터링 등 제공

3. You are selecting services to write and transform JSON messages from Cloud Pub/Sub to BigQuery for a data pipeline on Google Cloud. You want to minimize service costs. You also want to monitor and accommodate input data volume that will vary in size with minimal manual intervention. What should you do?

   * Use Cloud Dataproc to run your transformations. Use the diagnose command to generate an operational output archive. Locate the bottleneck and adjust cluster resources

   > #### [**Dataproc**](https://cloud.google.com/dataproc/docs/concepts/overview?hl=ko#getting-started-with-dataproc)
   >
   > Dataproc은 일괄 처리, 쿼리, 스트리밍, 머신 러닝에 오픈소스 데이터 도구를 활용할 수 있는 관리형 Spark 및 Hadoop 서비스입니다. Dataproc 자동화를 통해 신속하게 클러스터를 만들고 손쉽게 관리하며 불필요한 클러스터를 사용 중지하여 비용을 절감할 수 있습니다. 관리 시간과 비용이 절감되므로 작업과 데이터에 집중할 수 있습니다.
   >
   > - **저렴한 비용** — 초당 사용량 결제와 최저 1분 결제 기간을 사용하여 실제 사용량에 대해서만 비용을 청구합니다.
   > - **매우 빠름** — Dataproc을 사용하지 않으면 사내에 또는 IaaS 제공업체를 통해 Spark 및 Hadoop 클러스터를 만드는 데 5분에서 30분까지 소요될 수 있습니다. 반대로 Dataproc 클러스터는 빠르게 시작하고 확장하며 종료할 수 있습니다.
   > - **통합** -  [BigQuery](https://cloud.google.com/bigquery?hl=ko), [Cloud Storage](https://cloud.google.com/storage?hl=ko), [Cloud Bigtable](https://cloud.google.com/bigtable?hl=ko), [Cloud Logging](https://cloud.google.com/logging?hl=ko), [Cloud Monitoring](https://cloud.google.com/monitoring?hl=ko)과 같은 다른 Google Cloud Platform 서비스와 기본적으로 통합되어 있으므로 Spark 또는 Hadoop 클러스터 이상의 완벽한 데이터 플랫폼을 사용할 수 있습니다. 
   > - **관리형임** — Google Cloud Console, Cloud SDK, Dataproc REST API를 통해 클러스터 및 Spark 또는 Hadoop 작업과 쉽게 상호작용할 수 있습니다. 
   > - **간단하고 친숙함** - Dataproc을 사용하기 위해 새로운 도구나 API를 배울 필요가 없습니다.

   > #### Cloud Dataflow
   >
   > Cloud Dataflow는 Apache Beam(연산이 지연된 노드의 업무를 연산이 끝난 노드로 옮겨 전체 연산 시간을 줄이도록 리밸런싱)을 완전 관리형 서비스로 출시한 제품으로 서버리스 특징으로 작업의 양에 따라 리소스를 자동으로 프로비저닝하고 관리해줍니다.  
   >
   > 기존에 Apache Hadoop과 Spark 환경을 가지거나 직접 DevOps를 하는 환경을 원하는 사용자라면 Dataproc을 사용하는 것을 추천하고 있으며, 스트리밍 및 배치 데이터 처리를 Serverless로 하고자 한다면 Dataflow를 추천하고 있습니다. 

![img](https://blog.kakaocdn.net/dn/5Yio0/btqA2ORfogG/8f3Q9t7jHVECDOTFAOuE41/img.jpg)



4. Your infrastructure includes a set of YouTube channels. You have been tasked with creating a process for sending the YouTube channel data to Google Cloud for analysis. You want to design a solution that allows your world-wide marketing teams to perform ANSI SQL and other types of analysis on up-todate YouTube channels log data. How should you set up the log data transfer into Google Cloud?
   * Use **Storage Transfer Service** to transfer the offsite backup files to a Cloud Storage Regional bucket as a final destination.

> #### Storage Transfer Service
>
> - 클라우드 스토리지 제공업체 또는 [온프레미스](https://cloud.google.com/storage-transfer/docs/key-terms?hl=ko#on-prem) 스토리지에서 Cloud Storage 버킷으로 데이터를 이동하거나 백업합니다.
> - 데이터를 여러 사용자 그룹 또는 애플리케이션에서 사용할 수 있도록 Cloud Storage 버킷 하나에서 다른 버킷으로 이동합니다.
> - 데이터 처리 파이프라인 또는 분석 워크플로의 일환으로 데이터를 정기적으로 이동합니다.
> - 대역폭이 제한된 소스에서 오프라인 데이터, 대용량 데이터 세트 또는 데이터를 이동하는 [Transfer Appliance](https://cloud.google.com/transfer-appliance?hl=ko)
> - SaaS 애플리케이션에서 BigQuery로 데이터를 이동하는 [BigQuery Data Transfer Service](https://cloud.google.com/bigquery/transfer?hl=ko)
> - 온프레미스 머신에서 Cloud Storage로 데이터를 이동하는 [Transfer Service for On Premises Data](https://cloud.google.com/storage-transfer/docs/on-prem-overview?hl=ko)



## Single Topic

1. Your company built a TensorFlow neutral-network model with a large number of neurons and layers. The model fits well for the training data. However, when tested against new data, it performs poorly. What method can you employ to address this?

   - A. Threading
   - B. Serialization
   - **C. Dropout Methods**
   - D. Dimensionality Reduction

   참고 - https://www.cs.toronto.edu/~rsalakhu/papers/srivastava14a.pdf

   ```
   Dropout is A Simple Way to Prevent Neural Networks from
   Overfitting
   
   Option A - wrong (as Threading is to make training faster)
   Option B - wrong (Serialization) used while saving the model
   Option D - Wrong (Dimensionality Reduction) - This is though core parameter, but in question it's mention model works okay on Training Data..So dimension is not the issue here
   ```

   

2. You are building a model to make clothing recommendations. You know a user's fashion preference is likely to change over time, so you build a data pipeline to stream new data back to the model as it becomes available. How should you use this data to train the model?

   - A. Continuously retrain the model on just the new data.
   - **B. Continuously retrain the model on a combination of existing data and the new data.**
   - C. Train on the existing data while using the new data as your test set.
   - D. Train on the new data while using the existing data as your test set.

   ```
    it should be B because we have to use a combination of old and new test data as well as training data
   ```



3. You designed a database for patient records as a pilot project to cover a few hundred patients in three clinics. Your design used a single database table to represent all patients and their visits, and you used self-joins to generate reports. The server resource utilization was at 50%. Since then, the scope of the project has expanded. The database must now store 100 times more patient records. You can no longer run the reports, because they either take too long or they encounter errors with insufficient compute resources. How should you adjust the database design?

   - A. Add capacity (memory and disk space) to the database server by the order of 200.
   - B. Shard the tables into smaller ones based on date ranges, and only generate reports with prespecified date ranges.
   - **C. Normalize the master patient-record table into the patient table and the visits table, and create other necessary tables to avoid self-join.**
   - D. Partition the table into smaller tables, with one for each clinic. Run queries against the smaller table pairs, and use unions for consolidated reports.

   ```
   based on Google documentation, self-join is an anti-pattern
   ```

   참고 - https://cloud.google.com/bigquery/docs/best-practices-performance-patterns

   

4. You create an important report for your large team in **Google Data Studio 360**. The report uses Google BigQuery as its data source. You notice that visualizations are not showing data that is less than 1 hour old. What should you do?

   - **A. Disable caching by editing the report settings.**
   - B. Disable caching in BigQuery by editing table details.
   - C. Refresh your browser tab showing the visualizations.
   - D. Clear your browser history for the past hour then reload the tab showing the virtualizations.3

   ```
   캐시는 임시 데이터 저장소 시스템입니다. 캐시된 데이터를 가져오는 것은 기본 데이터 세트에서 직접 데이터를 가져오는 것보다 훨씬 빠르며 전송되는 쿼리 수를 줄여 유료 데이터 액세스 비용을 최소화할 수 있습니다.
   ```

   참고 - https://support.google.com/datastudio/answer/7020039?hl=en

   

5. An external customer provides you with a daily dump of data from their database. The data flows into Google Cloud Storage GCS as comma-separated values
   (CSV) files. You want to analyze this data in Google BigQuery, but the data could have rows that are formatted incorrectly or corrupted. How should you build this pipeline?

   - A. Use federated data sources, and check data in the SQL query.
   - B. Enable BigQuery monitoring in Google Stackdriver and create an alert.
   - C. Import the data into BigQuery using the gcloud CLI and set max_bad_records to 0.
   - **D. Run a Google Cloud Dataflow batch pipeline to import the data into BigQuery, and push errors to another dead-letter table for analysis.**

   참고 - https://cloud.google.com/bigquery/docs/loading-data#dataflow



6. Your weather app queries a database every 15 minutes to get the current temperature. The frontend is powered by Google App Engine and server millions of users. How should you design the frontend to respond to a database failure?

   - A. Issue a command to restart the database servers.
   - **B. Retry the query with exponential backoff, up to a cap of 15 minutes.**
   - C. Retry the query every second until it comes back online to minimize staleness of data.
   - D. Reduce the query frequency to once every hour until the database comes back online.

   ```
   지수 백오프
   애플리케이션에서 데이터베이스 연결을 시도하지만 성공하지 못할 경우 데이터베이스를 일시적으로 사용하지 못할 수 있습니다. 이 경우 동시 연결 요청을 너무 많이 전송하면 추가 데이터베이스 리소스가 낭비되고 복구에 필요한 시간이 늘어납니다. 지수 백오프를 사용하면 애플리케이션이 데이터베이스에 연결할 수 없을 때 응답하지 않는 수의 연결 요청을 전송하지 않습니다.
   ```

   참고 - https://cloud.google.com/sql/docs/mysql/manage-connections#backoff



7. You are creating a model to predict housing prices. Due to budget constraints, you must run it on a single resource-constrained virtual machine. Which learning algorithm should you use?

   - **A. Linear regression**
   - B. Logistic classification
   - C. Recurrent neural network
   - D. Feedforward neural network

   ```
   If you are forecasting that is the values in the column that you are predicting is numeric, it is always liner regression.
   Neural Networks(Feed Forward or Recurrent) require resource intensive machines(i.e GPU's) whereas Linear regression can be done on ordinary CPU's
   ```



8. You are building new real-time data warehouse for your company and will use Google BigQuery streaming inserts. There is no guarantee that data will only be sent in once but you do have a unique ID for each row of data and an event timestamp. You want to ensure that duplicates are not included while interactively querying data. Which query type should you use?

   - A. Include ORDER BY DESK on timestamp column and LIMIT to 1.
   - B. Use GROUP BY on the unique ID column and timestamp column and SUM on the values.
   - C. Use the LAG window function with PARTITION by unique ID along with WHERE LAG IS NOT NULL.
   - **D. Use the ROW_NUMBER window function with PARTITION by unique ID along with WHERE row equals 1.**

   ```
   Row Number equals 1 with partitioning will ensure only one record is fetched per partition
   ```

   참고 - https://cloud.google.com/bigquery/streaming-data-into-bigquery#manually_removing_duplicates



9. Your company is using WILDCARD tables to query data across multiple tables with similar names. The SQL statement is currently failing with the following error:
   \# Syntax error : Expected end of statement but got "-" at [4:11]

   SELECT age -

   FROM -
   bigquery-public-data.noaa_gsod.gsod

   WHERE -
   age != 99
   AND_TABLE_SUFFIX = "˜1929'

   ORDER BY -
   age DESC
   Which table name will make the SQL statement work correctly?

   - A. "˜bigquery-public-data.noaa_gsod.gsod"˜
   - B. bigquery-public-data.noaa_gsod.gsod*
   - C. "˜bigquery-public-data.noaa_gsod.gsod'*
   - D. **\`bigquery-public-data.noaa_gsod.gsod*\`**

   참고 - https://cloud.google.com/bigquery/docs/querying-wildcard-tables#before_you_begin



10. Your company is in a highly regulated industry. One of your requirements is to ensure individual users have access only to the minimum amount of information required to do their jobs. You want to enforce this requirement with Google BigQuery. Which three approaches can you take? (Choose three.)

    - A. Disable writes to certain tables.
    - **B. Restrict access to tables by role.**
    - C. Ensure that the data is encrypted at all times.
    - **D. Restrict BigQuery API access to approved users.**
    - E. Segregate data across multiple tables or databases.
    - **F. Use Google Stackdriver Audit Logging to determine policy violations.**

    ```
    A is not because, we cannot restrict write access to particular tables as the access is provided at dataset level.
    C is not because data is by default automatically encrypted by Google
    E is not because segregating data across tables or databases won't help
    ```



11. You are designing a basket abandonment system for an ecommerce company. The system will send a message to a user based on these rules:
    ✑ No interaction by the user on the site for 1 hour
    ✑ Has added more than $30 worth of products to the basket
    ✑ Has not completed a transaction
    You use Google Cloud Dataflow to process the data and decide if a message should be sent. How should you design the pipeline?

    - A. Use a fixed-time window with a duration of 60 minutes.
    - B. Use a sliding time window with a duration of 60 minutes.
    - **C. Use a session window with a gap time duration of 60 minutes.**
    - D. Use a global window with a time based trigger with a delay of 60 minutes.

    ```
    There are 3 windowing concepts in dataflow and each can be used for below use case
    1) Fixed window
    2) Sliding window and
    3) Session window.
    
    Fixed window = any aggregation use cases, any batch analysis of data, relatively simple use cases.
    Sliding window = Moving averages of data
    Session window = per user basis session data, click data and real time gaming analysis.
    ```



12. Your company handles data processing for a number of different clients. Each client prefers to use their own suite of analytics tools, with some allowing direct query access via Google BigQuery. You need to secure the data so that clients cannot see each other's data. You want to ensure appropriate access to the data.
    Which three steps should you take? (Choose three.)
    
    - A. Load data into different partitions.
    - **B. Load data into a different dataset for each client.**
    - C. Put each client's BigQuery dataset into a different table.
    - **D. Restrict a client's dataset to approved users.**
    - E. Only allow a service account to access the datasets.
    - **F. Use the appropriate identity and access management (IAM) roles for each client's users.**
    
    ```
    A 관계 없음
    E : Person can't even access the Big Query Service via UI (if we give access only to Service account). 
    ```
    
    

13. You want to process payment transactions in a point-of-sale application that will run on Google Cloud Platform. Your user base could grow exponentially, but you do not want to manage infrastructure scaling.
    Which Google database service should you use?

    - A. Cloud SQL
    - B. BigQuery
    - C. Cloud Bigtable
    - **D. Cloud Datastore**

    참고 - https://cloud.google.com/datastore/docs/concepts/overview

    ```
    Datastore는 자동 확장, 고성능, 간편한 애플리케이션 개발을 위해 빌드된 NoSQL 문서 데이터베이스입니다. Datastore 기능은 다음과 같습니다.
    keyword : highly scalability
    ```

14. You want to use a database of information about tissue samples to classify future tissue samples as either normal or mutated. You are evaluating an unsupervised anomaly detection method for classifying the tissue samples. Which two characteristic support this method? (Choose two.)

    - **A. There are very few occurrences of mutations relative to normal samples.**
    - B. There are roughly equal occurrences of both normal and mutated samples in the database.
    - **C. You expect future mutations to have different features from the mutated samples in the database.**
    - D. You expect future mutations to have similar features to the mutated samples in the database.
    - E. You already have labels for which samples are mutated and which are normal in the database.

    ```
    B is incorrect as it's unsupervised learning and not a classification algorithm so a balanced sample is not a priority in this case
    
    E is incorrect as it's unsupervised learning we're talking to, not supervised learning
    
    C랑 D가 정답이 많이 갈리네요..
    ```

15. You need to store and analyze social media postings in Google **BigQuery** at a rate of 10,000 messages per minute in near **real-time**. Initially, design the application to use streaming inserts for individual postings. Your application also performs **data aggregations right after the streaming inserts.** You discover that the queries after streaming inserts do not exhibit strong consistency, and reports from the queries might **miss in-flight data**. How can you adjust your application design?

    - A. Re-write the application to load accumulated data every 2 minutes.
    - B. Convert the streaming insert code to batch load for individual messages.
    - C. Load the original message to Google Cloud SQL, and export the table every hour to BigQuery via streaming inserts.
    - **D. Estimate the average latency for data availability after streaming inserts, and always run queries after waiting twice as long.**

    ```
    The data is first comes to buffer and then written to Storage. If we are running queries in buffer we will face above mentioned issues. If we wait for the bigquery to write the data to storage then we won’t face the issue. So We need to wait till it’s written tio storage
    ```

16. Your startup has never implemented a formal security policy. Currently, everyone in the company has access to the datasets stored in Google BigQuery. Teams have freedom to use the service as they see fit, and they have not documented their use cases. You have been asked to secure the data warehouse. You need to discover what everyone is doing. What should you do first?

    - **A. Use Google Stackdriver Audit Logs to review data access.**
    - B. Get the identity and access management IIAM) policy of each table
    - C. Use Stackdriver Monitoring to see the usage of BigQuery query slots.
    - D. Use the Google Cloud Billing API to see what account the warehouse is being billed to.

    ```
    Stackdriver
    자체적인 대용량 Message Queueing 인프라를 이용하여, GCP 서비스에 대한 통합 모니터링 및 로깅을 제공합니다.
    
    Cloud Audit log(감사 로그)
    Cloud 감사 로그는 Google Cloud 프로젝트, 폴더, 조직에 세 가지 audit log(관리자 활동, 데이터 액세스, 시스템 이벤트)를 유지한다. Google Cloud 서비스에서 감사 로그 항목을 이 로그에 작성하여 Google Cloud 리소스에서 '누가, 언제, 어디서, 무엇을 했는지' 파악할 수 있다.
    
    query slots
    SQL 쿼리를 실행하기 위해 BigQuery에 사용되는 가상 CPU입니다.
    ```

17. Your company is migrating their 30-node Apache Hadoop cluster to the cloud. They want to re-use **Hadoop jobs** they have already created and **minimize the management of the cluster** as much as possible. They also want to be able to **persist data** beyond the life of the cluster. What should you do?

    - A. Create a Google Cloud Dataflow job to process the data.
    - B. Create a Google Cloud Dataproc cluster that uses persistent disks for HDFS.
    - C. Create a Hadoop cluster on Google Compute Engine that uses persistent disks.
    - **D. Create a Cloud Dataproc cluster that uses the Google Cloud Storage connector.**
    - E. Create a Hadoop cluster on Google Compute Engine that uses Local SSD disks.

    출처 - https://cloud.google.com/dataproc?hl=ko

    ```
    Dataproc is used to migrate Hadoop and Spark jobs on GCP. Dataproc with GCS connected through Google Cloud Storage connector helps store data after the life of the cluster. When the job is high I/O intensive, then we need to create a small persistent disk.
    
    minimize the management of the cluster as much as possible. They also want to be able to persist data beyond the life of the cluster.
    
    In Dataproc, best practice is as soon as the job is done, the cluster is shutdown/deleted which will remove the data also in the cluster. They want storage beyond the life of the cluster which B option won't provide.
    ```

18. Business owners at your company have given you a database of bank transactions. Each row contains the user ID, transaction type, transaction location, and transaction amount. They ask you to investigate what type of machine learning can be applied to the data. Which three machine learning applications can you use? (Choose three.)

    - A. Supervised learning to determine which transactions are most likely to be fraudulent.
    - B. **Unsupervised learning to determine which transactions are most likely to be fraudulent.**
    - **C. Clustering to divide the transactions into N categories based on feature similarity.**
    - D. Supervised learning to predict the location of a transaction.
    - **E. Reinforcement learning to predict the location of a transaction.**
    - F. Unsupervised learning to predict the location of a transaction.
