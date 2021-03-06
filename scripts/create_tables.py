#!/usr/bin/python
import psycopg2
from config import config
import os

def create_tables():
    conn = None
    try:
        params = config()                                   # read connection parameters
        print('Connecting to the PostgreSQL database...')   # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()                                 # create a cursor
        print('PostgreSQL database version:')	            # execute a statement
        cur.execute('SELECT version()')
        db_version = cur.fetchone()                         # display the PostgreSQL database server version
        print(db_version)

	    # close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')

def executeScriptsFromFile(filename):
    fd = open(filename, 'r')
    sqlFile = fd.read()
    fd.close()
    # all SQl commands (split on ';')
    sqlCommands = sqlFile.split(';')

    # Execute every command from the input file
    for command in sqlCommands[:-1]:
        conn = None
        # This will skip and report errors
        # For example, if the tables do not yet exist, this will skip over
        # the DROP TABLE commands
        try:
            params = config()
            conn = psycopg2.connect(**params)
            cur = conn.cursor()
            cur.execute(command)
            conn.commit()
            cur = conn.close()
        except (Exception, psycopg2.OperationalError) as msg:
            print ("Command skipped: ", msg)
        finally:
            if conn is not None:
                conn.close()
                print('Database connection closed.')

if __name__ == '__main__':
    pwd = os.getcwd()
    create_tables()
    sql_query = ["/database/markets_india_nse_bhavcopy.psql","/database/markets_india_stock_price.psql", "/database/markets_india_stock_symbols.psql", "/database/markets_india_balance_sheet.psql", "/database/markets_india_calculated_ratios.psql", "/database/markets_india_pnl.psql"]
    for sq in sql_query:
        executeScriptsFromFile(pwd + sq)
