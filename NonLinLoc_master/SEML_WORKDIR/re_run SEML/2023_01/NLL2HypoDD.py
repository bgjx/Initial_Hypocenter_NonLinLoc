#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 19:21:24 2021

@author: arhamze
"""

"""
Code untuk mengambil analisis statistik hasil NonLinLoc
"""

prompth='''
----------------------------------------------------------------

Develepoed by Arham Zakki

This code is used for formating GAD output (Result.dat) to 
hypoDD's ph2dt data format. Read the hypoDD documentation
for complete information.

'''

print(prompth)
from collections import defaultdict as dfdict
import glob; import os;import math
from pyproj import Proj
## Convertion using Pyproj
file_name=glob.glob('*.grid0.loc.hyp')
phase_file_out=input("Output phase file name (ex. ML_november) :" )
zone_input=input("Insert UTM zone for convertion to Geographic system : ")
ID_input=input('Insert custom ID (4 digits integer ex. 1000 : ')
myProj = Proj(proj='utm', zone=int(zone_input), ellps='WGS84', datum='WGS84', units='m', south=True )


with open ((phase_file_out + ".pha"), "w") as file_DD:   
   
    listOfStation=['M01','M02','M03','M04','M05','M06','M07','M08','M09','M10','M11','M12','M13','M14','M15'] # holder value for station code
            # code for handling station weighting value
    listOfPhases=['M01 P','M01 S','M02 P','M02 S','M03 P','M03 S','M04 P','M04 S','M05 P','M05 S',
                  'M06 P','M06 S','M07 P','M07 S','M08 P','M08 S','M09 P','M09 S','M10 P','M10 S',
                  'M11 P','M11 S','M12 P','M12 S','M13 P','M13 S','M14 P','M14 S','M15 P','M15 S'] # holder value for station code
            # code for handling station weighting value
    DictOfStation={'M01P':0,
                           'M01S':0,
                           'M02P':0,
                           'M02S':0,
                           'M03P':0,
                           'M03S':0,
                           'M04P':0,
                           'M04S':0,
                           'M05P':0,
                           'M05S':0,
                           'M06P':0,
                           'M06S':0,
                           'M07P':0,
                           'M07S':0,
                           'M08P':0,
                           'M08S':0,
                           'M09P':0,
                           'M09S':0,
                           'M10P':0,
                           'M10S':0,
                           'M11P':0,
                           'M11S':0,
                           'M12P':0,
                           'M12S':0,
                           'M13P':0,
                           'M13S':0,
                           'M14P':0,
                           'M14S':0,
                           'M15P':0,
                           'M15S':0}       
    key_list=list(DictOfStation)
    dio=DictOfStation
    listOfStaValue=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    lio=listOfStaValue
    count=0    
    for i in file_name:
        count+=1        
        f = open(i)
        data_collect=[]
        for line in f:
            data_collect.append(line)
        
        stopper=0
        for lines in data_collect:
            stopper+=1
            if lines.startswith("HYPOCENTER"):break
            
        data_collect=data_collect[stopper:]
        
        data_to_formated=[]
        for lines in data_collect:
            lines=lines.split()
            data_to_formated.append(lines)

        for i in data_to_formated:
            try:                
                if i[0]=="M01" and i[4]=="P": 
                    lio[0]+=1
                elif i[0]=="M01" and i[4]=="S": 
                    lio[1]+=1
                elif i[0]=="M02" and i[4]=="P": 
                    lio[2]+=1
                elif i[0]=="M02" and i[4]=="S": 
                    lio[3]+=1
                elif i[0]=="M03" and i[4]=="P": 
                    lio[4]+=1
                elif i[0]=="M03" and i[4]=="S": 
                    lio[5]+=1
                elif i[0]=="M04" and i[4]=="P": 
                    lio[6]+=1
                elif i[0]=="M04" and i[4]=="S": 
                    lio[7]+=1
                elif i[0]=="M05" and i[4]=="P": 
                    lio[8]+=1
                elif i[0]=="M05" and i[4]=="S": 
                    lio[9]+=1
                elif i[0]=="M06" and i[4]=="P": 
                    lio[10]+=1
                elif i[0]=="M06" and i[4]=="S": 
                    lio[11]+=1
                elif i[0]=="M07" and i[4]=="P": 
                    lio[12]+=1
                elif i[0]=="M07" and i[4]=="S": 
                    lio[13]+=1
                elif i[0]=="M08" and i[4]=="P": 
                    lio[14]+=1
                elif i[0]=="M08" and i[4]=="S": 
                    lio[15]+=1
                elif i[0]=="M09" and i[4]=="P": 
                    lio[16]+=1
                elif i[0]=="M09" and i[4]=="S": 
                    lio[17]+=1
                elif i[0]=="M10" and i[4]=="P": 
                    lio[18]+=1
                elif i[0]=="M10" and i[4]=="S": 
                    lio[19]+=1
                elif i[0]=="M11" and i[4]=="P": 
                    lio[20]+=1
                elif i[0]=="M11" and i[4]=="S": 
                    lio[21]+=1
                elif i[0]=="M12" and i[4]=="P": 
                    lio[22]+=1
                elif i[0]=="M12" and i[4]=="S": 
                    lio[23]+=1
                elif i[0]=="M13" and i[4]=="P": 
                    lio[24]+=1
                elif i[0]=="M13" and i[4]=="S": 
                    lio[25]+=1
                elif i[0]=="M14" and i[4]=="P": 
                    lio[26]+=1
                elif i[0]=="M14" and i[4]=="S": 
                    lio[27]+=1
                elif i[0]=="M15" and i[4]=="P": 
                    lio[28]+=1
                elif i[0]=="M15" and i[4]=="S": 
                    lio[29]+=1
                else:
                    pass
            except Exception:
                pass

        if count == len(file_name): 
            print ('--------------------------------------------------\n\n',
                " For wighting porposes here are the total phases for each station: \n",
                   'M01 P :', lio[0],'\n',
                   'M01 S :', lio[1],'\n',
                   'M02 P :', lio[2],'\n',
                   'M02 S :', lio[3],'\n',
                   'M03 P :', lio[4],'\n',
                   'M03 S :', lio[5],'\n',
                   'M04 P :', lio[6],'\n',
                   'M04 S :', lio[7],'\n',
                   'M05 P :', lio[8],'\n',
                   'M05 S :', lio[9],'\n',
                   'M06 P :', lio[10],'\n',
                   'M06 S :', lio[11],'\n',
                   'M07 P :', lio[12],'\n',
                   'M07 S :', lio[13],'\n',
                   'M08 P :', lio[14],'\n',
                   'M08 S :', lio[15],'\n',
                   'M09 P :', lio[16],'\n',
                   'M09 S :', lio[17],'\n',
                   'M10 P :', lio[18],'\n',
                   'M10 S :', lio[19],'\n',
                   'M11 P :', lio[20],'\n',
                   'M11 S :', lio[21],'\n',
                   'M12 P :', lio[22],'\n',
                   'M12 S :', lio[23],'\n',
                   'M13 P :', lio[24],'\n',
                   'M13 S :', lio[25],'\n',
                   'M14 P :', lio[26],'\n',
                   'M14 S :', lio[27],'\n',
                   'M15 P :', lio[28],'\n',
                   'M15 S :', lio[29],'\n',
                   '\n',
                   'Please read documentation for further information\n\n'
                   
        '---------------------------------------------------------' )
            stopper_stat=0
            for v in lio:
                stopper_stat+=1
                if v > 0:
                    print('For station', listOfPhases[stopper_stat-1])
                    weigth_input=(input('Please input number for weighting value (between 0 - 1): \n'))
                    weigth_input=float(weigth_input)
                    dio[(key_list[stopper_stat-1])]=weigth_input
                elif stopper_stat==29:
                    break
    ID=int(ID_input)
    for i in file_name:
        # Create OT Holder
        OT=[]
        ID+=1 #adding 1 to create uniq id per events
        f = open(i)
        data_collect=[]
        for line in f:
            data_collect.append(line)
        
        stopper=0
        for lines in data_collect:
            stopper+=1
            if lines.startswith("HYPOCENTER"):break
        data_collect=data_collect[stopper:]
        data_to_formated=[]
        for lines in data_collect:
            lines=lines.split()
            data_to_formated.append(lines)
#        # formating the time format    
        
        
        for i in data_to_formated:
            pagar='#'            
            try:
                if i[0]=="GEOGRAPHIC":
                    file_DD.write("%s  %4i  %2i %2i %2i %2i  %9.6f " % (pagar,int(i[2]),int(i[3]),int(i[4]),int(i[5]),int(i[6]),float(i[7]))) ## done for the time date 
                    OT.append(i[7])
                    i[9]=float(i[9])*1000
                    i[11]=float(i[11])*1000
                    i[13]=float(i[13])+1.250 # add 1.250 to solve hypoDD depth problem
                    long, lat=myProj(i[11], i[9], inverse=True)
                    #lat_long=utm.to_latlon(utm_x[-1],utm_y[-1],int(zone_input), 'S' )
                    file_DD.write("%13.9f %14.9f  %8.5f  %i  %i  %i " % (lat,long,i[13],0,0,0))
                elif i[0] == "QUALITY":
                    i[8]=float(i[8])
                    file_DD.write("%11.8f  %4i\n" % ( i[8],ID))
                else:
                    pass
            except Exception:
                pass

            try:
                if i[0] in listOfStation and i[4] == 'P':
                    cek_value=abs(float(i[8])-float(OT[0]))
                    if cek_value < 30: 
                        file_DD.write("%3s %11.8f  %5.3f  %s\n" % (i[0], (abs(float(i[8])-float(OT[0]))), dio[i[0]+'P'], 'P'))
                    elif cek_value > 30 and float(OT[0]) < 3 :
                        file_DD.write("%3s %11.8f  %5.3f  %s\n" % (i[0], (abs(float(i[8])-(float(OT[0])+60))), dio[i[0]+'P'], 'P'))
                    else:
                        file_DD.write("%3s %11.8f  %5.3f  %s\n" % (i[0], (abs((float(i[8])+60)-float(OT[0]))), dio[i[0]+'P'], 'P'))
                elif i[0] in listOfStation and i[4] == 'S':
                    cek_value=abs(float(i[8])-float(OT[0]))
                    if cek_value < 30:
                        file_DD.write("%3s %11.8f  %5.3f  %s\n" % (i[0], (abs(float(i[8])-float(OT[0]))), dio[i[0]+'S'], 'S'))
                    elif cek_value > 30 and float(OT[0]) < 3 :
                        file_DD.write("%3s %11.8f  %5.3f  %s\n" % (i[0], (abs(float(i[8])-(float(OT[0])+60))), dio[i[0]+'S'], 'S'))
                    else:
                        file_DD.write("%3s %11.8f  %5.3f  %s\n" % (i[0], (abs((float(i[8])+60)-float(OT[0]))), dio[i[0]+'S'], 'S'))
                    continue                
                else:
                    pass
            except Exception as e:
                print(e)
                pass
            pass
        
    file_DD.close()
    print('--------  The code has run succesfully! ------------------------')
                
            
    
    

