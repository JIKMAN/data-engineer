# Data pipeline based GCP

![image-20210726233733623](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20210726233733623.png)

---

#### 1. Twitter API 발급

* Twitter Developer Platform 공식 문서 : https://developer.twitter.com/en/docs/twitter-api
* GCP IAM 서비스 계정 생성
  * 계정 권한 추가 : pub/sub 편집자 / Big-query 데이터 편집자
  * 비공개 키 발급 ( json 형태 )



#### 2. Twitter Streaming Code 작성

```python
import tweepy

twitter_api_key = '<twitter_api_key>'
twitter_api_secret_key = '<twitter_api_secret_key>'
twitter_access_token = '<twitter_access_token>'
twitter_access_token_secret = '<twitter_access_token_secret>'

class SimpleStreamListener(tweepy.StreamListener):
	def on_status(self, status):
		print(status)
        
stream_listener = SimpleStreamListener()

auth = tweepy.OAuthHandler(twitter_api_key, twitter_api_secret_key)
auth.set_access_token(twitter_access_token, twitter_access_token_secret)

twitterStream = tweepy.Stream(auth, stream_listener)
twitterStream.filter(track=['tesla']) # tesla 내용이 들어간 트윗을 스트림
```

##### 

#### 3. Google Cloud Pub/Sub

1. Topic 생성

2. Subscription(구독) 추가

   ```bash
   # Subscription name 예시
   projects/My_project/subscriptions/My_Sub
   
   # Delivary Type
   Pull 설정
   ```

3.  Pub/Sub으로 메시지 전송

   * Streaming Code 추가

```
import json
import tweepy
from google.cloud import pubsub_v1
from google.oauth2 import service_account

key_path = "ta-8755-90de8ad4bc7d.json"

credentials = service_account.Credentials.from_service_account_file(
key_path,
scopes=["https://www.googleapis.com/auth/cloud-platform"],
)
client = pubsub_v1.PublisherClient(credentials=credentials)
topic_path = client.topic_path('ta-8755', 'tweets')
twitter_api_key = '<twitter_api_key>'
twitter_api_secret_key = '<twitter_api_secret_key>'
twitter_access_token = '<twitter_access_token>'
twitter_access_token_secret = '<twitter_access_token_secret>'
```

![pubsub](../../img/pubsub.png)

* 공식문서 : https://cloud.google.com/pubsub/docs/overview
* 

