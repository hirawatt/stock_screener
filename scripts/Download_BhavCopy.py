#!/usr/bin/python3.8
import requests
import zipfile
from dateutil.parser import parse
from datetime import datetime
from io import BytesIO

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
    nsezip = zipfile.ZipFile(BytesIO(response), 'r')
    filelist = nsezip.namelist()
    if len(filelist) > 1:
        raise ValueError("More than one file found. Quitting!!")
    for f in filelist:
        bhavcopyfile = nsezip.open(f, 'r')
        data = bhavcopyfile.read()
        #compressed = dbutils.compress(data)
        filename = "/home/vh/Desktop/finance/personal_fin/scripts/marketsdata/nsecm_{}_bhavcopy.csv".format(
            bcdate.strftime('%Y%m%d'))
        with open(filename, 'wb') as f:
            f.write(data)
    return True

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
