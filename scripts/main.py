from Download_BhavCopy import download_nsecm_bhavcopy
from create_tables import create_tables, executeScriptsFromFile
from config  import config
from dbutil import database
import datalayer
from datetime import datetime
import os
import psycopg2

if __name__ == '__main__':

    bhavcopyfile = download_nsecm_bhavcopy(datetime(2021, 1, 18))
    print("File saved at " + bhavcopyfile)
    pwd = os.getcwd()
    create_tables()
    sql_query = ["/database/markets_india_nse_bhavcopy.psql","/database/markets_india_stock_price.psql", "/database/markets_india_stock_symbols.psql", "/database/markets_india_balance_sheet.psql", "/database/markets_india_calculated_ratios.psql", "/database/markets_india_pnl.psql"]
    for sq in sql_query:
        executeScriptsFromFile(pwd + sq)

    # copy data from csv to database
    f = open(bhavcopyfile, 'r')
    params = config()
    conn = psycopg2.connect(**params)
    cur = conn.cursor()
    next(f)
    cur.copy_from(f, 'markets_india_nse_bhavcopy', sep=',')
    conn.commit()
    f.close()
    '''
        query = "/sql_query/cp_bhavcopy.psql"
        executeScriptsFromFile(pwd + query)
    '''
