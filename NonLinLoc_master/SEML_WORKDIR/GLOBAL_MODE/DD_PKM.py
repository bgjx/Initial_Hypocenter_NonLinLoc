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
import glob; import os;import math


uniq_ID=input("Masukan ID gempa (iD unik yang berada diawal nama file ex. sunda) :")
file_name=glob.glob('*.loc.hyp')
file_name_skip_sum=[]
cnv_Out=input("FIle PHA akan disimpan dengan (ex. zakki) :" )
zone_input=input("Masukan Zone UTM untuk dikonversi ke Lat Long: ")
with open ((cnv_Out+".pha"), "w") as file_DD:
    def utmToLatLng(zone, easting, northing, northernHemisphere=True):
        if not northernHemisphere:
            northing = 10000000 - northing

        a = 6378137
        e = 0.081819191
        e1sq = 0.006739497
        k0 = 0.9996

        arc = northing / k0
        mu = arc / (a * (1 - math.pow(e, 2) / 4.0 - 3 * math.pow(e, 4) / 64.0 - 5 * math.pow(e, 6) / 256.0))

        ei = (1 - math.pow((1 - e * e), (1 / 2.0))) / (1 + math.pow((1 - e * e), (1 / 2.0)))

        ca = 3 * ei / 2 - 27 * math.pow(ei, 3) / 32.0

        cb = 21 * math.pow(ei, 2) / 16 - 55 * math.pow(ei, 4) / 32
        cc = 151 * math.pow(ei, 3) / 96
        cd = 1097 * math.pow(ei, 4) / 512
        phi1 = mu + ca * math.sin(2 * mu) + cb * math.sin(4 * mu) + cc * math.sin(6 * mu) + cd * math.sin(8 * mu)

        n0 = a / math.pow((1 - math.pow((e * math.sin(phi1)), 2)), (1 / 2.0))

        r0 = a * (1 - e * e) / math.pow((1 - math.pow((e * math.sin(phi1)), 2)), (3 / 2.0))
        fact1 = n0 * math.tan(phi1) / r0

        _a1 = 500000 - easting
        dd0 = _a1 / (n0 * k0)
        fact2 = dd0 * dd0 / 2

        t0 = math.pow(math.tan(phi1), 2)
        Q0 = e1sq * math.pow(math.cos(phi1), 2)
        fact3 = (5 + 3 * t0 + 10 * Q0 - 4 * Q0 * Q0 - 9 * e1sq) * math.pow(dd0, 4) / 24

        fact4 = (61 + 90 * t0 + 298 * Q0 + 45 * t0 * t0 - 252 * e1sq - 3 * Q0 * Q0) * math.pow(dd0, 6) / 720

        lof1 = _a1 / (n0 * k0)
        lof2 = (1 + 2 * t0 + Q0) * math.pow(dd0, 3) / 6.0
        lof3 = (5 - 2 * Q0 + 28 * t0 - 3 * math.pow(Q0, 2) + 8 * e1sq + 24 * math.pow(t0, 2)) * math.pow(dd0, 5) / 120
        _a2 = (lof1 - lof2 + lof3) / math.cos(phi1)
        _a3 = _a2 * 180 / math.pi

        latitude = 180 * (phi1 - fact1 * (fact2 + fact3 + fact4)) / math.pi

        if not northernHemisphere:
            latitude = -latitude

        longitude = ((zone > 0) and (6 * zone - 183.0) or 3.0) - _a3

        return (latitude, longitude)

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
        data_OT[7]=float(data_OT[7])*1000.;data_OT[8]=float(data_OT[8])*1000.
        UTM_to_Lat_long=utmToLatLng(int(zone_input),float(data_OT[8]),float(data_OT[7]),True)
        data_OT[7]=UTM_to_Lat_long[0]
        data_OT[8]=UTM_to_Lat_long[1]
        DD=data_OT
        file_DD.write("%s %4i  %2i  %2i  %2i  %2i  %8.5f  %13.9f  %14.9f  %8.5f  %1i  %1i  %1i  %8.6f  %4i\n" % (DD[0],int(DD[1]),int(DD[2]),int(DD[3]),int(DD[4]),int(DD[5]),float(DD[6]),float(DD[7]),float(DD[8]),float(DD[9]),int(DD[10]),int(DD[11]),int(DD[12]),float(DD[13]),int(DD[14])))
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
        list_dt=data_pd_clt[i].values.tolist()
        h=0
        for p in list_dt:
            h+=1
            file_DD.write("%4s  %8.5f  %5s  %s\n" % (p[0],p[1],p[2],p[3]))
            if len(list_dt)==h:
                break            
    file_DD.close()
