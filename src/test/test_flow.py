from config import PATH_TO_DATABASE

import test.test_client as retriever

import polars as pl


# Fetch the products
products = retriever.fetch_products()


#Convert to nice table
df = pl.DataFrame(products)


print(df)

#download table


final_path = PATH_TO_DATABASE + "/products.parquet"

df.write_parquet(final_path)

print("Products saved to: " + final_path)