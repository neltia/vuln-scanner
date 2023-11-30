from dotenv import load_dotenv
import os
from elasticsearch_dsl import connections
from app.models.dao import Checker


# es 설정 초기화
def es_init():
    load_dotenv(verbose=True)

    es_client()
    index_mapping()


# 엘라스틱서치 클라이언트 세션 생성
def es_client():
    # es host info
    es_api_key = os.getenv("ES_API_KEY")
    es_host = os.getenv("ES_HOST")
    es_port = os.getenv("ES_PORT")

    # es ssl key (vagrant/virtualbox 8.10.4)
    # cp /etc/elasticsearch/certs/http_ca.crt /vagrant
    ca_file_path = os.getenv("ES_CRT_PATH")

    # connection create
    connections.create_connection(
        hosts=[f"https://{es_host}:{es_port}"],
        ca_certs=ca_file_path,
        api_key=es_api_key
    )


# nori plugin 적용을 위한 매핑 설정
def index_mapping():
    return
