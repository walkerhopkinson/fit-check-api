import test_retriver as retriever

import polars as pl


# Fetch the products
products = retriever.fetch_products()


#Convert to nice table
df = pl.DataFrame(products)


print(df)