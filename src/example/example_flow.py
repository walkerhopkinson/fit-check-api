from config import PATH_TO_DATABASE

import example_client as retriever

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

#convert for csv
#df.write_csv(csv_path)
# Before writing, convert any 'List' or 'Struct' columns to String
df_for_csv = df.with_columns(
    pl.col(pl.List, pl.Struct).cast(pl.String)
)

df_for_csv.write_csv(csv_path)

print("Products saved to: " + parquet_path)
print("Products saved to: " + csv_path)