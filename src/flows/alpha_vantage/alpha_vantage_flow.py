import alpha_vantage_client as avc
from dao.example_dao import ExampleDao
import polars as pl
from config import PATH_TO_DATABASE
import datetime as dt

slave = ExampleDao(PATH_TO_DATABASE)


def main():
    winners, losers = avc.get_winners_losers()
    
    winners3 = winners.head(3)
    losers3 = losers.head(3)

    slave.overwrite_csv_file_with_df_and_name(winners3, f"top_3_{dt.date.today()}")
    slave.overwrite_csv_file_with_df_and_name(losers3, f"bottom_3_{dt.date.today()}")
    
    print("Download Complete!")
    
    print("Top 3:", winners3)
    print("Bottom 3:", losers3)


if __name__ == "__main__":
    main()

    
