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

---

**3. A company has an on-premises application that collects data and stores it to an on-premises NFS server. The company recently set up a 10 Gbps AWS Direct Connect connection. The company is running out of storage capacity on premises. The company needs to migrate the application data from on premises to the AWS Cloud while maintaining low-latency access to the data from the on-premises application.**

* Deploy `AWS Storage Gateway` for the application data, and use the file gateway to store the data in Amazon S3. Connect the on-premises application servers to the file gateway using NFS.

> #### Amazon Storage Gateway
>
> 온프레미스를 클라우드 기반 스토리지와 연결하여, **온프레미스와 IT 환경과 AWS의 스토리지를 사용하는 서비스**
>
> 비용 효율적으로 데이터 보안 유지 및 확장이 가능

---

