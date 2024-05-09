#!/usr/bin/env python
import argparse
from urllib import request
import json
import argparse
import pandas as pd
import time
import os

parser = argparse.ArgumentParser(
    prog='ezSNP: Read-in a list of the SNP, output MAFs', 
    description='Query the SNP from NCBI server', 
    epilog= 'Bo Wang Ph.D., https://github.com/pop3www/dbSNP2NCBI')
parser.add_argument('Input_csv',  help='Input SNP list (in csv format)')
parser.add_argument('Pause_Timer', type=float, help='An pause timer to avoid server overload, unit="s"')

args = parser.parse_args()
cwd = os.getcwd()
file_path = os.path.join(cwd, args.Input_csv)
print(file_path)
print(args.Pause_Timer)

csv_input = pd.read_excel(file_path)
timer = args.Pause_Timer


dbSNP_list = csv_input["dbSNP_RS"].values.tolist()
dbSNP_list = [item for items in dbSNP_list for item in items.split(",")]

df_all=pd.DataFrame()
for snp_id in dbSNP_list:
    time.sleep(0.5)
    snp_id=snp_id[2:]
    eutils_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?retmode=json&db=snp&id=" + snp_id
    f = request.urlopen(eutils_url)
    content = f.read()

    eutils_json = json.loads(content.decode("utf-8"))
    snp_json = eutils_json["result"][snp_id]
    MAFs = snp_json['global_mafs']

    df=pd.DataFrame.from_dict(MAFs)
    if df.empty==False:
        df=pd.DataFrame.from_dict(MAFs).T
        df.columns = df.iloc[0]
        df=df[1:]
        df=df.rename(index={'freq': "rs"+snp_id})
        df_all=pd.concat([df_all, df], ignore_index=False,sort=False)
df_all.to_csv("result_MAF.csv")
