* ```bash
  filebeat modules enable system nginx mysql
  ```

* ```shell
  filebeat setup --pipelines --modules system
  ```

```bash
#output.elasticsearch:
  #hosts: ["localhost:9200"]
output.kafka:
  hosts: ["kafka:9092"]
  topic: "filebeat"
  codec.json:
    pretty: false
```

* ```shell
  filebeat -e
  ```



