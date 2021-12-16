curl -X DELETE localhost:9200/_ingest/pipeline/amazon_pipeline | jq
curl -X DELETE localhost:9200/amazon | jq


# Create pipeline
curl -X PUT localhost:9200/_ingest/pipeline/amazon_pipeline -H "Content-Type: application/json" -d @pipeline.json | jq

# Create index
curl -X PUT localhost:9200/amazon -H "Content-Type: application/json" -d @index.json | jq

rm insert_output.txt

while read line
do  
   # Write data to a file first
   # If data string is too long curl command won't execute
   echo "{ \"csv_entry\": \"$line\" }" > data.txt

   # Insert data to Elasticsearch using data in file
   curl -sX POST localhost:9200/amazon/_doc -H "Content-Type: application/json" -d @data.txt | jq >> insert_output.txt
done < <(tail -n +2 processed_data.csv)

curl -X GET localhost:9200/amazon/_count | jq