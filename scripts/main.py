from Download_BhavCopy import download_nsecm_bhavcopy
from create_tables import create_tables, executeScriptsFromFile
from datetime import date
import os

if __name__ == '__main__':
    today = date.today()
    download_nsecm_bhavcopy(str(today.year) + str(today.month) + str(today.day))
    pwd = os.getcwd()
    create_tables()
    sql_query = ["/database/markets_india_nse_bhavcopy.psql","/database/markets_india_stock_price.psql", "/database/markets_india_stock_symbols.psql", "/database/markets_india_balance_sheet.psql", "/database/markets_india_calculated_ratios.psql", "/database/markets_india_pnl.psql"]
    for sq in sql_query:
        executeScriptsFromFile(pwd + sq)
    
