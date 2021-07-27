카프카의 이해

![img](https://t1.daumcdn.net/cfile/tistory/99EA16425C46ABA62F)



> ### 메시지 큐?

MOM(Message Oriented Middleware, 메시지 지향 미들웨어)은 비동기 메시지를 사용하는 다른 응용프로그램 사이의 데이터 송수신을 의미하는데, 그것을 구현한 시스템을 메시지 큐(MQ, Message Queue) 라고 한다.



> ### 카프카란?

Linked-In에서 개발한 플랫폼으로, pub-sub을 이용한 플랫폼으로 개발되었다.

```python
# pub-sub
메시지를 특정 수신자에게 직접적으로 보내주는 시스템이 아니고, 메시지를 받기를 원하는 사람이 해당 토픽(topic)을 구독함으로써 메시지를 읽어 올 수 있다. 보내는 사람과 받는 사람이 서로 독립적으로 작동
```



> ### 카프카의 특징

* 대용량 실시간 로그처리에 특화되어 설계된 메시징 시스템으로 TPS(초당 처리하는 트랜잭션)가 매우 우수함
* 메시지를 메모리에 저장하지 않고 파일에 저장하기 때문에 메시지 유실 우려가 감소
* 컨슈머(Consumer)가 브로커(Broker)로부터 메시지를 직접 가져가는 PULL 방식으로 동작
  * 컨슈머는 자신의 처리능력 만큼의 메시지만 가져오므로 최적의 성능을 냄



> ### 카프카의 구성요소

#### Topic, Partition

* 카프카에 저장되는 메시지는 topic으로 분류되고, topic은 여러개의 partition으로 나뉜다.

* partition 안에는 message의 위치를 나타내는 offset이 있는데, offset정보를 통해 다음에 메시지를 가져갈 때 이전 위치정보를 알 수 있다.
* 파티션을 증가하는 것은 아무 때나 변경이 가능하지만, 반대로 파티션의 수를 줄이는 것은 토픽을 삭제하는 방법 말고는 없다. 따라서 파티션의 수를 정할 때 원하는 목표 처리량의 기준을 잡고 조금씩 파티션의 수를 늘려가며 정적 수를 유지하는 것이 좋다.

#### Producer, Consumer

* Producer는 메시지를 생산, Consumer는 소비하며, 서로 독립적으로 작동한다.

#### Consumer Group

* 하나의 토픽을 읽어가기 위한 Counsumer들을 Consumer Group이라고 한다.

* Topic의 파티션은 그 Consumer group과 1:n 매칭. 즉, 읽고 있는 파티션에는 같은 그룹 내 다른 컨슈머가 읽을 수 없다.

* 파티션 개수보다 컨슈머 그룹의 컨슈머 개수가 더 많으면 남는 컨슈머가 발생 (일반적으로 파티션 개수와 컨슈머 개수를 동일하게 구성한다고 한다.)

  ![img](https://blog.kakaocdn.net/dn/HZKBH/btqFWcVyDXL/ycAkzTOum7md1ZIxGrGGv1/img.png)

* 특정 컨슈머에 문제가 생겼을 경우 그룹 내 다른 컨슈머가 대신 읽을 수 있다.

#### Broker, Zookeeper

* Broker는 카프카 서버를 말한다.  동일한 노드 내에서 여러개의 broker server를 띄울 수 있다.
* Zookeeper는 이러한 분산 메시지큐의 정보를 관리해주는 역할을 한다. 기존에는 카프카 실행을 위해 반드시 zookeeper가 실해되어야 했으나, 현재 주키퍼 의존성을 제거한 카프카 버전이 배포되었다. (KRaft mode, [관련 사이트](https://towardsdatascience.com/kafka-no-longer-requires-zookeeper-ebfbf3862104))

#### Replication

* 카프카에서는 replication 수를 임의로 지정해서 topic을 만들 수 있다.

![img](https://t1.daumcdn.net/cfile/tistory/99E5AD425C3FE33B10)

*  topic으로 통하는 모든 데이터의 read/write는 오직 leader에서 이루어지고 follower는 leader와 sync를 유지함으로써 leader에 문제가 생겼을 경우 follower들 중 하나가 leader역할을 하게 되는 것이다.

* 복제된 데이터가 follower들에게 있으니, 메시지의 유실이 없다는 장점이 있지만, 복제를 하기 위한 시간과 네트워크 비용이 들기 때문에 데이터의 중요도에 따라 ack옵션으로 성능과 데이터의 중요도에 따라 다음과 같이 세부설정이 가능하다.

```bash
# ack (default: 1) - 프로듀서가 메시지를 보내고 그 메시지를 카프카가 잘 받았는지 확인할 것인지 또는 확인하지 않을 것인지를 결정하는 옵션

0 : 프로듀서는 서버로부터 어떠한 ack도 기다리지 않음. 유실율 높으나 높은 처리량

1 : 리더가 메시지를 받았는지 확인, 팔로워는 확인하지 않음 (follower에게 복제가 되기 전에 	leader가 fail되면, 해당 메시지는 손실가능)

-1(또는 all) : 모든 ISR(In Sync Replica) 확인. 무손실
```



> #### 카프카 구성도

![img](https://t1.daumcdn.net/cfile/tistory/998C274D5C3FE33B0A)

* 카프카 공식문서 (https://kafka.apache.org/documentation/)