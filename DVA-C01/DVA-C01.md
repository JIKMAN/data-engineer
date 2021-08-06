1. **A Developer created a dashboard for an application using Amazon API Gateway, Amazon S3, AWS Lambda, and Amazon RDS. The Developer needs an authentication mechanism allowing a user to sign in and view the dashboard. It must be accessible from mobile applications, desktops, and tablets, and must remember user preferences across platforms.**
   **Which AWS service should the Developer use to support this authentication scenario?**

* Amazon Cognito

```python
# Amazon Cognito

Amazon Cognito 는 웹 및 모바일 앱에 대한 인증, 권한 부여 및 사용자 관리를 제공합니다. 사용자는 사용자 이름과 암호를 사용하여 직접 로그인하거나 Facebook, Amazon, Google 또는 Apple 같은 타사를 통해 로그인할 수 있습니다.
```



---

2. **A company is building a compute-intensive application that will run on a fleet of Amazon EC2 instances. The application uses attached Amazon EBS disks for storing data. The application will process sensitive information and all the data must be encrypted.What should a Developer do to ensure the data is encrypted on disk without impacting performance?**

* Configure the Amazon EC2 instance fleet to use encrypted EBS volumes for storing data.

```python
# Amazon EBS 암호화

EC2 인스턴스와 연결된 EBS 리소스를 위한 간단한 암호화 솔루션으로, Amazon EBS 암호화를 사용하면 자체 키 관리 인프라를 구축, 유지 관리 및 보호할 필요가 없습니다. Amazon EBS 암호화는 암호화된 볼륨 및 스냅샷을 생성할 때 AWS KMS keys를 사용합니다.
암호화 작업은 EC2 인스턴스를 호스팅하는 서버에서 진행되며, 인스턴스와 인스턴스에 연결된 EBS 스토리지 간 유휴 데이터 및 전송 중 데이터의 보안을 모두 보장합니다.
인스턴스에는 암호화된 볼륨과 암호화되지 않은 볼륨을 동시에 연결할 수 있습니다.
```

---

3. **A company is launching an ecommerce website and will host the static data in Amazon S3. The company expects approximately 1,000 transactions per second (TPS) for GET and PUT requests in total. Logging must be enabled to track all requests and must be retained for auditing purposes.**
   **What is the MOST cost-effective solution?**

* Enable AWS CloudTrail logging for the S3 bucket-level action and create a lifecycle policy to expire the data in 90 days.

```python
# AWS CloudTrail

AWS 계정의 거버넌스, 규정 준수, 운영 감사, 위험 감사를 지원하는 서비스입니다. CloudTrail을 사용하면 AWS 인프라에서 계정 활동과 관련된 작업을 기록하고 지속적으로 모니터링하며 보관할 수 있습니다.
이벤트 기록을 통해 보안 분석, 리소스 변경 추적, 문제 해결을 간소화할 수 있습니다. 또한 CloudTrail을 사용하여 AWS 계정의 비정상적인 활동을 탐지할 수 있습니다. 이러한 기능을 통해 운영 분석과 문제 해결을 간소화할 수 있습니다.
```

---

4. **A Developer is writing an application in AWS Lambda. To simplify testing and deployments, the Developer needs the database connections string to be easily changed without modifying the Lambda code. How can this requirement be met?**

* Store the connection string in AWS KMS.

---

5. **A Developer implemented a static website hosted in Amazon S3 that makes web service requests hosted in Amazon API Gateway and AWS Lambda. The site is showing an error that reads:**

   **“No ‘Access-Control-Allow-Origin’ header is present on the requested resource. Origin ‘null’ is therefore not allowed access.”**

   **What should the Developer do to resolve this issue?**

* Enable cross-origin resource sharing (CORS) for the method in API Gateway

---

6. **A Developer is migrating an on-premises application to AWS. The application currently takes user uploads and saves them to a local directory on the server. All uploads must be saved and made immediately available to all instances in an Auto Scaling group.Which approach will meet these requirements?**

* Use Amazon EBS and file synchronization software to achieve eventual consistency among the Auto Scaling group.

---

7. **A Developer decides to store highly secure data in Amazon S3 and wants to implement server-side encryption (SSE) with granular control of who can access the master key. Company policy requires that the master key be created, rotated, and disabled easily when needed, all for security reasons.**
   **Which solution should be used to meet these requirements?**

* SSE with AWS KMS managed keys (SSE-KMS)

---

