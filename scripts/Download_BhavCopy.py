#!/usr/bin/python3.8
import requests
import zipfile
from dateutil.parser import parse
from datetime import datetime
import io
import csv
import os
import pandas as pd

def download_nsecm_bhavcopy(bcdate):

    year = bcdate.year
    mnth = bcdate.strftime('%b').upper()
    dt = bcdate.strftime('%d')

    base_path = "https://archives.nseindia.com/content/historical/EQUITIES/{}/{}/cm{}{}{}bhav.csv.zip"
    path = base_path.format(year, mnth, dt, mnth, year)
    response = requests.get(path)
    if response.status_code == 200:
        response = response.content
    else:
        raise ValueError("Error Downloadning BhavCopy")
    nsezip = zipfile.ZipFile(io.BytesIO(response), 'r')
    filelist = nsezip.namelist()
    if len(filelist) > 1:
        raise ValueError("Something is wrong. More than one file found. Quitting.")
    filename = "marketsdata/nsecm.{}.bhavcopy.csv".format(
            bcdate.strftime('%Y%m%d'))
    with nsezip.open(filelist[0], 'r') as csvfile:
        data = pd.read_csv(csvfile)
        csv_data = pd.DataFrame.to_csv(data, encoding='utf-8', index=False)
    with open(filename, 'w') as f:
        f.write(csv_data)
    return filename

'''

    with zipfile.ZipFile(io.BytesIO(response), 'r') as nseunzip:
        nseunzip.extractall("/home/vh/Desktop/finance/personal_fin/scripts/marketsdata/")
    os.rename(r"/home/vh/Desktop/finance/personal_fin/scripts/marketsdata/cm{}{}{}bhav.csv".format(dt, mnth, year), r"/home/vh/Desktop/finance/personal_fin/scripts/marketsdata/nsecm_{}_bhavcopy.csv".format(
        bcdate.strftime('%Y%m%d')))
    filename = "/home/vh/Desktop/finance/personal_fin/scripts/marketsdata/nsecm_{}_bhavcopy.csv".format(
        bcdate.strftime('%Y%m%d'))
    with open(filename, 'w') as f:
        text_obj = f.decode('UTF-8')
        f.write(text_obj)
    return filename
'''
# Date Parser Function
def GetParser():
    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument('date')
    return parser

if __name__ == '__main__':
    args = GetParser().parse_args()
    date = datetime.strptime(args.date, '%Y%m%d')
    print("Downloadning BhavCopy dated...", date)
    download_nsecm_bhavcopy(date)
    print("BhavCopy downloaded and saved in csv format")
