#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 19:21:24 2021

@author: arhamze
"""

"""
Code untuk mengambil analisis statistik hasil NonLinLoc
"""
import pandas as pd;import numpy as np;
from collections import defaultdict as dfdict
import glob; import os
uniq_ID=input("Masukan ID gempa (iD unik yang berada diawal nama file ex. sunda) :")
file_name=glob.glob('*.loc.hyp')
file_name_skip_sum=[]
dir_simpan=input("file excel disimpan dengan nama:")
with pd.ExcelWriter("Coleccting_statistic.xlsx", engine='xlsxwriter') as writer:
    for i in file_name:
        if i.startswith(str(uniq_ID)+".sum.grid0.loc.hyp"):continue
        file_name_skip_sum.append(i)
    event_ID=1000
    data_pd_clt={}
    data_pd_res={}
    for i in file_name_skip_sum:
        event_ID+=1
        data_collect=[]
        f=open(i)
        for n in f:
            n=str(n)
            data_collect.append(n)
        par_stop=0;par_stop1=0;par_stop2=0
        for n in data_collect:
            par_stop1+=1
            if n.startswith("GEOGRAPHIC"):break
        data_OT=data_collect[par_stop1-1]
        data_OT=data_OT.split()
        order=[2,3,4,5,6,7,9,11,13]
        data_OT=[data_OT[i] for i in order]
        data_RMS=data_collect[par_stop1]
        data_RMS=data_RMS.split()
        indeks=data_RMS.index("RMS")
        data_RMS=data_RMS[indeks+1]
        error=[0,0,0]
        data_ot_dict={}
        for v in error:
            data_OT.append(v)
        data_OT.append(data_RMS)
        data_OT.append('#')
        re_order=[13,0,1,2,3,4,5,6,7,8,9,10,11,12];data_OT=[data_OT[i] for i in re_order]
        data_OT.append(event_ID)
        data_ot_dict[i]=data_OT
        df2=pd.DataFrame.from_dict(data_ot_dict, orient="index")
        for n in data_collect:
            par_stop+=1
            if n.startswith("FOCALMECH"):break
        data_select=data_collect[par_stop:-2]; #print(data_select)
        header=data_select[0];data_saja=data_select[1:-1]
        header=header.split(); header_min_phase=header[1:]
        data_ae=[]
        for n in data_saja:
            n=n.split()
            data_ae.append(n)
        dictio={}
        random_l=[];
        dta_s=[0,1]
        for n in range(len(data_ae)):
            dictio[n]=data_ae[n]
            dta_s[0]=data_ae[n][0]
            dta_s[1]=data_ae[n][4]
            dta_s2=str(dta_s[0])+str(dta_s[1])
            random_l.append(dta_s2)
        i=i[-29:-14]
        data_pd_clt[i]=pd.DataFrame.from_dict(dictio, orient="index",columns=header_min_phase) #untuk versi statistik lengkap
        data_pd_res[i]=data_pd_clt[i]["Res"]
        data_pd_clt[i]["TTpred"]=data_pd_clt[i]["TTpred"].apply(pd.to_numeric)+data_pd_res[i].apply(pd.to_numeric)
        data_pd_clt[i]=data_pd_clt[i][["ID","TTpred","Pha"]]
        data_pd_clt[i].insert(2,"WGHT",random_l)
        data_pd_clt[i].columns=range(data_pd_clt[i].shape[1])
        data_pd_clt[i]=pd.concat([df2,data_pd_clt[i]], ignore_index=True)
    for key, item in data_pd_clt.items():
        item.to_excel(writer, sheet_name=key)
df = pd.concat(pd.read_excel("Coleccting_statistic.xlsx", sheet_name=None), ignore_index=True)
all_data = pd.DataFrame()
path = '*.xlsx'
for f in glob.glob(path):
    df = pd.read_excel(f, sheet_name=None, ignore_index=True)
    cdf = pd.concat(df.values(),ignore_index=True)
    all_data = all_data.append(cdf,ignore_index=True)
all_data.to_excel(dir_simpan+'.xlsx')
os.remove("Coleccting_statistic.xlsx")

