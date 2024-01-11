#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 21:55:02 2021

@author : ARHAM ZAKKI EDELO
@contact: edelo.arham@gmail.com
"""
from collections import defaultdict as dfdict
import glob
from pyproj import Proj

print ("""
----------------------------------------------------------------
This code is used for making initial hiposenter catalog from NonLinLoc output


""")

# initialize input output
custom_name1 = input("Input your desired hypocenter detail output name: ")
zone_input   = int(input("Insert UTM zone for convertion to Geographic system : "))
myProj       = Proj(proj='utm', zone=zone_input, ellps='WGS84', datum='WGS84', units='m', south=True )
ID           = int(input('Insert custom ID (4 digits integer ex. 1000) : '))

# gather all .hyp file
file_name=glob.glob('*.grid0.loc.hyp')
file_name.sort()
with open (custom_name1 + ".csv", "w") as file_output_hypo:
    file_output_hypo.write("ID\tLat\tLong\tUTM X (m)\tUTM Y (m) \tDepth (m)\tElev (m)\tYear\tMonth\tDay\tHour\tMinute\tOT(sec)\tRMS error\tN Phases\tGAP\tPDF errXX +/- (m)\tPDF errYY +/- (m)\tPDF errZZ +/- (m)\n")
    for i in file_name:
        data_to_formated=[line.split() for line in open(i,'r').readlines()]
        for i in data_to_formated:
            try:
                if i[0]=="GEOGRAPHIC":
                    long, lat=myProj((float(i[11])*1000), (float(i[9])*1000), inverse=True)
                    file_output_hypo.write("%4i\t%.12f\t%.12f\t%.6f\t%.6f\t%.6f\t%.6f\t%2i\t%2i\t%2i\t%2s\t%2s\t%.7f\t" % (ID,lat,long,float(i[11])*1000,float(i[9])*1000,float(i[13])*1000 ,float(-1*(float(i[13])*1000 )),int(i[2]),int(i[3]),int(i[4]),int(i[5]),float(i[6]),float(i[7])))
                elif i[0]=="QUALITY" :
                    file_output_hypo.write("%s\t%i\t%.6f\t" % (i[8], float(i[10]),float(i[12]))) 
                elif i[0]=="STATISTICS":
                    errXX=((3.53 * float(i[8]))**0.5)*0.5
                    errYY=((3.53 * float(i[14]))**0.5)*0.5
                    errZZ=((3.53 * float(i[18]))**0.5)*0.5
                    file_output_hypo.write("%.6f\t%.6f\t%.6f\n" % (errXX*1000, errYY*1000, errZZ*1000))
                else:
                    pass
            except Exception:
                    continue
        ID+=1 #adding 1 to create uniq id per events    
    file_output_hypo.close()
    print('-----------  The code has run succesfully! --------------')