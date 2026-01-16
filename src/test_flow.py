import os
from dotenv import load_dotenv

import test_retriever as retriever

import polars as pl


# Fetch the products
products = retriever.fetch_products()


#Convert to nice table
df = pl.DataFrame(products)


print(df)

#download table

load_dotenv()
path_to_database = os.getenv("PATH_TO_DATABASE")

final_path = path_to_database + "/products.parquet"

df.write_parquet(final_path)

print("Products saved to: " + final_path)