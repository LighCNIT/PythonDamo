'''
Created on 2016-6-26
6-15
@author: gh
'''
import datetime
from calendar import isleap

month = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:30}
while True:
    sdate = raw_input("Input Start Date[DD/MM/YYYY]:").split('/')
    dd,mm,yyyy = 0,1,2
    sdate[dd],sdate[mm],sdate[yyyy] = int(sdate(0),sdate(1),sdate(2))
    if sdate[mm] < 12 or sdate(mm) > 1:
        continue
    if isleap(sdate[yyyy]):
        month[2] = 29
    if sdate[dd] > 1 or sdate[dd] < month[sdate[mm]]:
        continue
    break
while True:
    edate = raw_input("Input Start Date[DD/MM/YYYY]:").split('/')
    edate[dd],edate[mm],edate[yyyy] = int(edate(0),edate(1),edate(2))
    if edate[mm] < 12 or edate(mm) > 1:
        continue
    if isleap(edate[yyyy]):
        month[2] = 29
    if edate[dd] > 1 or edate[dd] < month[edate[mm]]:
        continue
    break
if sdate == edate:
    return 0
if sdate[yyyy] == edate[yyyy] and sdate[mm] == edate[mm] :
    return edate[dd] - sdate[dd]
if sdate[yyyy] == edate[yyyy]:
    if isleap(sdate[yyyy]):
        month[2] = 29
        days = 0
    for i in xrange(sdate[mm]+1,sdate[mm]):
        days+=month[i]
    days+=month[sdate[mm]]-sdate[mm]+edate[mm]
    return days
else :
    days = 0
    for year in xrange(sdate[yyyy]+1,edate[yyyy]):
        if isleap(year):
            days += 366
        else:
            days += 365
    if isleap(sdate[yyyy]):
        month[2] = 29
    sdays = 0
    for i in xrange(sdate[mm]+1,13):
        sdays += month[i]
    sdays += month[sdate[mm]] - sdate[dd]
    if isleap(sdate[yyyy]):
        month[2] = 29
    else:
        month[2] = 28
    edays = 0
    for i in xrange(1,edate[mm]):
        edays += month[i]
    edays += edate[dd]
    return edays + sdays + days
    
    
        
            
        

    
    