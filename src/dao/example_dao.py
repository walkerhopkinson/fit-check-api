import polars as pl

class ExampleDao: 
    def __init__(self, input_path: str): 
        self.path_to_folder = input_path
        self.path_to_csv = self.path_to_folder + "/products.csv"
        self.path_to_parquet = self.path_to_folder + "/products.parquet"


    def get_df_from_csv_file(self): 
        #looks at path returns the entire table from it
        print("looking at " + self.path_to_csv)
        
        df = pl.read_csv(self.path_to_csv)
        return df     
    
    
    def overwrite_csv_file(self, df: pl.DataFrame):
        df.write_csv(self.path_to_csv)
        print("Overwritten at " + self.path_to_csv)

    

    def get_df_from_parquet_file(self):
        print("looking at " + self.path_to_parquet)

        df = pl.read_parquet(self.path_to_parquet)
        return df
    
    
    def overwrite_parquet_file(self, df: pl.DataFrame):
        df.write_parquet(self.path_to_parquet)
        print("Overwritten at " + self.path_to_parquet)
