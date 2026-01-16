from config import PATH_TO_DATABASE

import test.test_client as retriever

import polars as pl


# Fetch the products
products = retriever.fetch_products()


#Convert to nice table
df = pl.DataFrame(products)


print(df)

#download table


parquet_path = PATH_TO_DATABASE + "/products.parquet"
csv_path = PATH_TO_DATABASE + "/products.csv"

df.write_parquet(parquet_path)
#df.write_csv(csv_path)

print("Products saved to: " + parquet_path)
print("Products saved to: " + csv_path)