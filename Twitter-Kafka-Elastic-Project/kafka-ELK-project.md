EC2 생성시 꼭 Seoul 선택

* 회사에서 사용시 보안 때문에 네트웤을 분리하고 서브넷을 나누는 작업을 하게될 텐데..
* IAM role?







---

1. Amazon EC2 생성 ,  ssh key 발급

`chmod 400 ssh_key.pem`

` ssh -i ssh-key.pem ubuntu@{server IP}`

```shell
input {
  twitter {
	consumer_key => "8C96ESoXxxxxxxxxxxxxxxx"
	consumer_secret => "DdiFkdflkjadfEszZDfjdfhoweryqbdFd"
	oauth_token => "90722238952835725-asjhdfoiquyoeuqhehjfjashasdf"
	oauth_token_secret => "qajsdfljkaoiqOIUFJlkqjLKJlkjdafopifpqpisdkfI"
	keywords => ["news","game","data"]
	full_tweet => true
  }
}
output {
  file {
	path => "/tmp/twitter-%{+YYYY-MM-dd}.json"
	codec => json_lines
  }
}
```

