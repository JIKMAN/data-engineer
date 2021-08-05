# SAA-C02

**1.** **A solutions architect is designing a solution where users will be directed to a backup static error page if the primary website is unavailable. The primary website’s DNS records are hosted in Amazon Route 53 where their domain is pointing to an Application Load Balancer (ALB).**

**Which configuration should the solutions architect use to meet the company’s needs while minimizing changes and infrastructure overhead?**

* Set up a Route 53 `active-passive failover` configuration. Direct traffic to a static error page hosted within an Amazon S3 bucket when Route 53 health checks determine that the ALB endpoint is unhealthy.

> #### Amazon Route 53
>
> AWS의 DNS 서비스
>
> - 도메인 등록
> - DNS 라우팅
> - 상태 체크(Health check)
>
> 해당 도메인을 AWS 내 서비스(EC2, ELB, S3 등)와 연결할 수 있으며 AWS 외 요소들과도 연결 가능함
>
> 도메인 생성 후 레코드 세트를 생성하여 하위 도메인을 등록할 수 있음
>
> 레코드 세트 등록시에는 IP 주소, 도메인, **‘Alias(별칭, CNAME와 동일한 개념)’** 등을 지정하여 쿼리를 라우팅할 수 있음

---

**2. A solutions architect needs to design a network that will allow multiple Amazon EC2 instances to access a common data source used for mission-critical data that can be accessed by all the EC2 instances simultaneously. The solution must be highly scalable, easy to implement and support the NFS protocol.**

* Create an `Amazon EFS file system`. Configure a mount target in each Availability Zone. Attach each instance to the appropriate mount target.

> #### Amazon EFS(Elastic File System)
>
> EC2에서 확장 사용 가능한 파일 스토리지.
> 파일을 추가/제거할 때마다 스토리지 용량이 탄력적으로 자동 확장 및 축소

```python
# EFS
- AWS 클라우드 및 사내 서버의 컴퓨팅 인스턴스에 사용할 공유 file 스토리지
- 네트워크 연결 공유 파일 스토리지 (NFSv4 프로토콜 사용)
- 수천 대의 EC2 인스턴스 간 파일 시스템 공유
- 페타바이트 규모로 탄력적으로 자동 확장 및 축소
- Multi AZ(Availability Zone:가용성 존)
- ACID 만족하며 resiliency 가지고 있음

# EBS
- block 레벨 스토리지
- 파일 시스템 생성하고 파일 저장
- 단일 EC2 인스턴스의 전용 블록 스토리지
- 볼륨의 크기를 변경은 수동적인 작업

# EC2 Instance Store
- 임시 블록 스토리지
- 임시 콘텐츠와 같이 자주 변경되는 정보의 임시 스토리지로 사용하기 좋음
- 인스턴스의 수명 기간 동안에만 데이터 지속(재부팅은 유지)

# S3
- 웹에서 사용 가능한 object 저장소
- 뛰어난 내구성, 제약 없는 확장성
- 5가지 유형(Standard, Standard IA, One Zone IA, Glacier, Glacier Deep Archive)
```



---

**3. A company has an on-premises application that collects data and stores it to an on-premises NFS server. The company recently set up a 10 Gbps AWS Direct Connect connection. The company is running out of storage capacity on premises. The company needs to migrate the application data from on premises to the AWS Cloud while maintaining low-latency access to the data from the on-premises application.**

* Deploy `AWS Storage Gateway` for the application data, and use the file gateway to store the data in Amazon S3. Connect the on-premises application servers to the file gateway using NFS.

> #### Amazon Storage Gateway
>
> 온프레미스를 클라우드 기반 스토리지와 연결하여, **온프레미스와 IT 환경과 AWS의 스토리지를 사용하는 서비스**
>
> 비용 효율적으로 데이터 보안 유지 및 확장이 가능

---

**4. A company is planning on deploying a newly built application on AWS in a default VPC. The application will consist of a web layer and database layer. The web server was created in public subnets, and the MySQL database was created in private subnets. All subnets are created with the default network ACL settings, and the default security group in the VPC will be replaced with new custom security groups.**

**The following are the key requirements:**
**The web servers must be accessible only to users on an SSL connection.**
**The database should be accessible to the web layer, which is created in a public subnet only.**
**All traffic to and from the IP range 182.20.0.0/16 subnet should be blocked.**

**Which combination of steps meets these requirements? (Select two.)**

* Create a database server security group with an inbound rule for MySQL port 3306 and specify the source as a web server security group.
* Create a web server security group with an inbound rule for HTTPS port 443 traffic from anywhere (0.0.0.0/0). Create network ACL inbound and outbound deny rules for IP range 182.20.0.0/16.

[**VPN(Virtual Private Network)**, **VPC(Virtual Private Cloud)**의 개념](https://medium.com/harrythegreat/aws-%EA%B0%80%EC%9E%A5%EC%89%BD%EA%B2%8C-vpc-%EA%B0%9C%EB%85%90%EC%9E%A1%EA%B8%B0-71eef95a7098)

```python
# ACL(Access List)

접근하는 것을 허용 또는 거부하는 접근제어 리스트

ACL을 통해 필터링 이라는 기능을 수행할 수 있는데 특정 주소를 가진 호스트의 접근을 막거나 특정 서비스를 차단하는 등의 여러 목적으로 사용될 수 있다.
```

---

