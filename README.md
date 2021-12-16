# Projet Elasticsearch

Source des données:
https://data.world/promptcloud/fashion-products-on-amazon-com

Pour obtenir une instance elasticsearch:

```
docker run -d --name elasticsearch -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" elasticsearch:7.10.1
```