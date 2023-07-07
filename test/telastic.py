"""
from datetime import datetime
from elasticsearch import Elasticsearch
es = Elasticsearch("http://localhost:9200")

resp = es.indices.get(index="*")
print(resp)
"""
from opensearchpy import OpenSearch
client = OpenSearch(
    hosts = [{'host': 'localhost', 'port': 9200}],
    http_compress = True, # enables gzip compression for request bodies
)

query = \
{
  "query": {
    "match_all": {}
  },
  "size": 0,
  "aggs": {
    "deposit_date_grp": {
      "date_histogram": {
        "fixed_interval": "1h",
        "field": "deposit_date"
      },
      "aggs": {
        "amount_sum": {
          "sum": {
            "field": "amount"
          }
        }
      }
    }
  }
}
response = client.search(
    body = query,
    index = "deposit.raffle"
)
print(response.get('aggregations').get('deposit_date_grp').get('buckets'))