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

2. 