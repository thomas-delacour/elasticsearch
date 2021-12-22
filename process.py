"""
Script to pre-process data before inserting in Elasticsearch.
It will remove several caracters that cuold be an issue for Elasticsearch
to process. The resulting processed data will be saved in a new CSV file
"""

import re
import pandas as pd


def clean_data(data):
    """
    Clean data so it can be processed with Elasticsearch
    """

    for col in data.columns:

        if hasattr(data[col], "str"):
            data[col] = data[col].str.replace("'", "")
            data[col] = data[col].str.replace('"', "")
            data[col] = data[col].str.replace(",", "")
            data[col] = data[col].str.replace("£", "")
            data[col] = data[col].str.replace("&", "and")

            # Only keep numerical value at the beginning of the string
            if col in [
                "number_available_in_stock",
                "average_review_rating",
                "price",
            ]:
                data[col] = data[col].str.replace(" .+", "", regex=True)

            # Remove reviews titles to avoid duplicate tokens
            if col == "customer_reviews":
                data[col] = data[col].str.replace("(^|\|).+?//", "", regex=True)
                data[col] = data[col].str.strip()
    return data


ids_list = []
with open("amazon_co-ecommerce_sample.csv") as csv_file:

    with open("processed_data.csv", "w") as processed_file:
        line = csv_file.readline()

        while line:
            line = line.strip()
            line = line.replace(" ", " ")
            line = line.replace("!", ".")
            line = line.replace("\t", " ")

            # New entry
            if re.search("^[0-9a-f]{32}", line):
                processed_file.write("\n" + line)
                ids_list.append(line[0:32])
            else:
                if line:
                    processed_file.write(" " + line)

            line = csv_file.readline()

# Use pandas Dataframe to perform more complex cleaning on csv columns
data = pd.read_csv("processed_data.csv")

data = clean_data(data)
data.to_csv("processed_data.csv", index=False)
