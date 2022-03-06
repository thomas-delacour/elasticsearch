# Projet Elasticsearch

## Pré-requis

Source des données:
https://data.world/promptcloud/fashion-products-on-amazon-com

Pour obtenir une instance elasticsearch:

```
docker run -d --name elasticsearch -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" elasticsearch:7.10.1
```

## Préparation des données
Le script `process.py` permet de nettoyer les données et de créer un fichier CSV qui sera utilisé pour remplir la base

## Création de la base

Une fois l'instance d'Elasticsearch disponible l'execution du script `create_es_database.sh` va créer l'index via les informations contenues dans `pipeline.json` et `index.json`
puis va insérer les données dans la base.

## API avec FastAPI

L'API est dévelopée avec le framework [FastAPI](https://fastapi.tiangolo.com/)

### Enpoints

#### /
Cet endpoint permet de contrôler si l'API est en fonctionnement
#### /docs
Fastapi fournit cet endpoint qui permet d'accèder à une documentation de l'API et de tester les différents endpoints
#### /info
Renvoie les informations des indexes présents dans la base
#### /search
Permet de requêter la base en donnant le terme de recherche et le champ dans lequelle cette recherche s'effectue. Il est possible de filtrer les champs retournés avec l'attribut **outputs**
#### /count
Renvoie le nombre de document présent dans la base. Les paramètre **index** et **q** donnent la possibilité de sélectionner l'index et d'affiner le résultat
#### /create_document/{index}
Cet endpoint permet d'ajouter un nouveau document à l'index spécifié. Les données du document sont transmises dans le corps de la requête