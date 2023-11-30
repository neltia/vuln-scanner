from elasticsearch_dsl import Document
from elasticsearch_dsl import Date, Text, Boolean, Keyword


class Checker(Document):
    class Index:
        name = "vuln-report"

    name = Text()
    created_at = Date()
