#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 21:55:02 2021

@author : ARHAM ZAKKI EDELO
@contact: edelo.arham@gmail.com
"""
from collections import defaultdict as dfdict
import glob, os
from pyproj import Proj
import pandas as pd
from pathlib import Path

print ("""
Python code for generating initial hiposenter catalog from NonLinLoc output
""")

def create_catalog(file_hyp, _id, myProj, df_holder):    
    data_to_formated=[line.split() for line in open(file_hyp,'r').readlines()]
    for i in data_to_formated:
        try:
            if i[0]=="GEOGRAPHIC":
                long, lat=myProj((float(i[11])*1000), (float(i[9])*1000), inverse=True)
                df_holder["ID"].append(_id)
                df_holder["Lat"].append(lat)
                df_holder["Lon"].append(long)
                df_holder["UTM_X"].append((float(i[11])*1000))
                df_holder["UTM_Y"].append((float(i[9])*1000))
                df_holder["Depth"].append((float(i[13])*1000))
                df_holder["Elev"].append((float(-1*(float(i[13])*1000))))
                df_holder["Year"].append((int(i[2])))
                df_holder["Month"].append((int(i[3])))
                df_holder["Day"].append((int(i[4])))
                df_holder["Hour"].append((int(i[5])))
                df_holder["Minute"].append((float(i[6])))
                df_holder["T0"].append((float(i[7])))
            elif i[0]=="QUALITY" :
                df_holder["RMS_error"].append((float(i[8])))
                df_holder["N_Phases"].append((int(i[10])))
                df_holder["GAP"].append((float(i[12])))
            elif i[0]=="STATISTICS":
                errXX=(3.53 * float(i[8]))**0.5  # it is the double error
                errYY=(3.53 * float(i[14]))**0.5
                errZZ=(3.53 * float(i[18]))**0.5
                df_holder["PDF_errXX(m)"].append(errXX*1000)
                df_holder["PDF errYY(m)"].append(errYY*1000)
                df_holder["PDF errZZ(m)"].append(errZZ*1000)
            else:
                pass
        except Exception:
                continue
    return None

# initialize input and output path
hyp_path    = Path(r"F:\SEML\DATA PROCESSING\MEQ MISCELANEOUS PROCESSING\NonLinLoc Results\2023\re run 2023_01 2023_10\re run all 2023")  # file solusi NLL
output_path = Path(r"F:\SEML\DD RELOCATION\ph2dt")

# dinamic input prompt
output_name = input("Input your desired hypocenter detail output name: ")
zone_input  = int(input("Insert UTM zone for convertion to Geographic system : "))
myProj      = Proj(proj='utm', zone=zone_input, ellps='WGS84', datum='WGS84', units='m', south=True )
ID          = int(input('Insert custom ID (4 digits integer ex. 1000) : '))

# gather all .hyp file
file_name = glob.glob(os.path.join(hyp_path, '*.grid0.loc.hyp'), recursive=True)
file_name.sort()

# initiate dataframe for initial catalog
df_catalog   = {
                 "ID":[],
                 "Lat":[],
                 "Lon":[], 
                 "UTM_X":[],
                 "UTM_Y":[], 
                 "Depth":[], 
                 "Elev":[], 
                 "Year":[], 
                 "Month":[],
                 "Day":[], 
                 "Hour":[], 
                 "Minute":[],
                 "T0":[],
                 "RMS_error":[],
                 "N_Phases":[],
                 "GAP":[],
                 "PDF_errXX(m)":[], 
                 "PDF errYY(m)":[],
                 "PDF errZZ(m)":[]
                    }
for i in file_name:
    create_catalog (i, ID, myProj, df_catalog)
    ID+=1 #adding 1 to create uniq id per events    
df_cat = pd.DataFrame.from_dict(df_catalog)
# save and set dataframe index
df_cat.to_excel(output_path.joinpath(f"{output_name}.xlsx"), index = False)
print('-----------  The code has run succesfully! --------------')