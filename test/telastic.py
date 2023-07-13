from datetime import datetime
"""
from elasticsearch import Elasticsearch
es = Elasticsearch("http://localhost:9200")

resp = es.indices.get(index="*")
print(resp)
"""
from opensearchpy import OpenSearch, exceptions

def parser(response):
    q = response.get('aggregations').get('deposit_account_grp').get('buckets')
    #q = response.get('aggregations').get('deposit_date_grp').get('buckets')
    #qq = [ {
    #    "date":row['key_as_string'], 
    #    "datetime":datetime.strptime(row['key_as_string'],"%Y-%m-%dT%H:%M:%S.%fZ" ),
    #    "count":row['doc_count'], 
    #    "amount_sum":row['amount_sum']['value']
    #    } for row in q]
    qq = [ {
        "account":row['key'], 
        "count":row['doc_count'], 
        "amount_sum":row['amount_sum']['value']
        } for row in q]
    return qq    

client = OpenSearch(
#    hosts = [{'host': 'localhost', 'port': 9200}],
    hosts = 'http://localhost:9200',
    http_compress = True, # enables gzip compression for request bodies
)

query = \
{
  "query": {
    "match_all": {}
  },
  "size": 0,
  "aggs": {
    "deposit_account_grp": {
      "terms": {
        "field": "account.keyword"
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
"""
query = \
{
  "query": {
    "match_all": {}
  },
  "size": 0,
  "aggs": {
    "deposit_date_grp": {
      "date_histogram": {
        "fixed_interval": "1d",
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
"""
try:
  response = client.search(
      body = query,
      index = "deposit.raffle"
  )
except exceptions.NotFoundError as e:
    print(e.__str__())

print(parser(response))
#print(response)

client.close()