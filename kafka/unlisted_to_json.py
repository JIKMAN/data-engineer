from kafka import KafkaProducer
import pandas as pd
import json
import sys


topic = 'JUPITER_FINANCE_IN'
servers = ['10.35.30.81:9092', '10.35.30.82:9092', '10.35.30.83:9092', '10.35.30.84:9092', '10.35.30.85:9092', '10.35.30.86:9092', '10.35.30.87:9092', '10.35.30.88:9092']

def parse_data(input_dir):
    loaded_csv = pd.read_csv(f"{input_dir}/unlisted_stock_list.csv", sep=',')

    code = loaded_csv["CODE"]
    name = loaded_csv["NAME"]

    value = {"data":[]}

    for i in range(len(code)):
        combined = f"{code[i]}:{name[i]}"
        value["data"].append(combined)

    unlisted_dict = {"key":"unlisted", "value":value}

    p = KafkaProducer(acks=0, bootstrap_servers=servers, value_serializer=lambda x: json.dumps(x, ensure_ascii=False).encode('utf-8'))

    p.send(topic, value=unlisted_dict)
    p.flush()

def main():
    parse_data(sys.argv[1])

if __name__ == '__main__':
    main()