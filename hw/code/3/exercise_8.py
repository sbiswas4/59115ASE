# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 10:13:53 2015

@author: akond
"""

def has_duplicates(listParam):
    valToRet = False 
    for listItem in listParam: 
        countVal = listParam.count(listItem)
        if countVal > 1: 
            valToRet = True 
    return valToRet





def generateBirthdays(studentCountParam, startRangeParam, endRangeParam):
    import random
    listToRet=[]
    for cnt in range(0, studentCountParam):
        listToRet.append(random.randint(startRangeParam, endRangeParam))
    #print listToRet    
    return listToRet    



def findBdayMatches(stdCntParam, startParam, endParam, simRunCount):
    countToRet = 0      
    for k in range(simRunCount): 
        listToUse=generateBirthdays(stdCntParam, startParam, endParam)
        dupResult = has_duplicates(listToUse)
        if dupResult: 
            countToRet =  countToRet + 1 
    return countToRet         

#listToUse=['rahman', 'akond' , 'a', 'rahman'] 
listToUse=[-10, -10000 , 4, 5] 
res = has_duplicates(listToUse)
print "Duplicates finding: ", res 
##Birthday Paradox 
studentCount=23 
startVal = 1 
endVal =365
simulationRun = 10 
resBdayCount = findBdayMatches(studentCount, startVal, endVal, simulationRun)
print "So far matches for {} students , are {}".format(studentCount, resBdayCount)  
 