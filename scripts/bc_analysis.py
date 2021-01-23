import pandas as pd
import matplotlib.pyplot as plt
import os

pwd = os.getcwd()
bhav_cp = pd.read_csv(pwd + "/marketsdata/nsecm_20201222_bhavcopy.csv", "r")

print(bhav_cp.head())
