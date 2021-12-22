# Query examples for Elasticsearch

# Product with price greater than 500
curl -X POST "localhost:9200/amazon/_search" -H 'Content-Type: application/json' -d '{"_source": ["price"], "query": {"range": { "price": {"gte": 500} } }}' | jq

# Price between 10 and 15
curl -X POST "localhost:9200/amazon/_search" -H 'Content-Type: application/json' -d '{"_source": ["price"], "query": {"range": { "price": {"gte": 10, "lte": 15} } }}' | jq

# Nb of product categories containing the word "toy"
curl -X POST "localhost:9200/amazon/_search" -H 'Content-Type: application/json' -d '{"_source": ["amazon_category_and_sub_category"], "query": {"match": {"amazon_category_and_sub_category": "toy"} }}' | jq

# Document with categories containing the word "train"
curl -X POST "localhost:9200/amazon/_search" -H 'Content-Type: application/json' -d '{"_source": ["amazon_category_and_sub_category"], "query": {"match": {"amazon_category_and_sub_category": "train"} }}' | jq

# Reviews containing "amazing"
curl -X POST "localhost:9200/amazon/_search" -H 'Content-Type: application/json' -d '{"_source": ["customer_reviews"], "query": {"match": {"customer_reviews": "amazing"} }}' | jq

# Reviews containing "amazing product"
curl -X POST "localhost:9200/amazon/_search" -H 'Content-Type: application/json' -d '{"_source": ["customer_reviews"], "query": {"match": {"customer_reviews": "amazing product"} }}' | jq