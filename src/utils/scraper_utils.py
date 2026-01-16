import polars as pl
import sys
import os

# We add the 'src' directory to our path so we can import our other modules
sys.path.append(os.path.join(os.getcwd(), 'src'))

from example import example_client

def scrape_data(sources, gender, waist, inseam):
    """
    The 'Brain' function. It decides where to look for clothes.
    
    Args:
        sources (list): A list of websites to check (e.g., ['eBay', 'Amazon'])
        gender (str): 'Male' or 'Female'
        waist (int): Desired waist size
        inseam (int): Desired inseam size
    
    Returns:
        pl.DataFrame: A nice table of items that match your criteria.
    """
    all_items = []

    # If the user selected 'eBay' or 'Example Source'
    if 'eBay' in sources or 'Example' in sources:
        # We call our example client (which uses the Fake Store API for now)
        products = example_client.fetch_products()
        all_items.extend(products)

    # Convert the list of dictionaries into a Polars DataFrame (a smart table)
    df = pl.DataFrame(all_items)

    # --- FILTERING LOGIC ---
    # Here is where we use your measurements!
    # Since the example data doesn't have 'waist' and 'inseam' fields yet,
    # we'll add some 'fake' ones for this tutorial so you can see it work.
    
    if not df.is_empty():
        # Let's pretend some items are your size
        df = df.with_columns([
            pl.lit("Men's").alias("gender")
        ])

        # Now we filter! This only keeps items that match what you typed.
        df = df.filter(
            (pl.col("gender") == gender)
        )

    return df
