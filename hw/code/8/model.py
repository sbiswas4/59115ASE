# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 10:47:36 2015

@author: akond
"""

from random import uniform
import math

class Model(object):
    def __init__(self):
        self.decisionVec=[0]
        self.lowerRange=[0]
        self.numOfDec=0
        self.numOfObjs=0
        self.upperRange=[0]
        self.baseline=[999999, 0]

    def check(self):
        for count in range(0,self.numOfDec):
            if (self.decisionVec[count]<self.lowerRange[count]) or (self.decisionVec[count]>self.upperRange[count]):
              return False
        return True

    def copy(self,other):
        self.decisionVec = [_ for _ in other.decisionVec]
        self.lowerRange = [_ for _ in other.lowerRange]
        self.numOfDec = other.numOfDec
        self.numOfObjs = other.numOfObjs
        self.upperRange = [_ for _ in other.upperRange]

    def generateInitialVector(self):
        ## we use random.uniform() as it geives floating point values as well
        while True:
            for cnt in range(0,self.numOfDec):
                self.decisionVec[cnt]=uniform(self.lowerRange[cnt],self.upperRange[cnt])
            if self.check(): break

    def getobj(self):
        return []

    def sumOfObjs(self):
        # print "GET OBJECTIVES:",self.getobj()
        # exit()
        #print "obj:{}, currBaseline:{}".format(self.getobj(), self.getCurrentBaseline())
        #exit()
        ## old formula 
        # float(sum(self.getobj())  / sum(self.getCurrentBaseline())) 
        objs= sum(self.getobj())  
        #print "*** objs {} **** baseline_min {} *** baseline_max{} ".format(objs, BaseLine.baseline_min, BaseLine.baseline_max)
        normalizedScore = (objs- BaseLine.baseline_min) / float(BaseLine.baseline_max - BaseLine.baseline_min) 
        return normalizedScore 

    def updateBaseline(self, baselineParam):
      self.baseline =   [_ for _ in   baselineParam ]

    def getCurrentBaseline(self):
      return self.baseline

    def sumOfObjsInit(self):
        return float(sum(self.getobj()))



class Osyczka2(Model):

    def __init__(self):
        ## first specify the requirements
        self.decisionVec=[0,0,0,0,0,0]
        self.lowerRange=[0,0,1,0,1,0]
        self.numOfDec=6
        self.numOfObjs=2
        self.upperRange=[10,10,5,6,5,10]
        ## then create the initialization
        self.generateInitialVector()

    def check(self):
        constCheckerVec = [0,0,0,0,0,0]
        constCheckerVec[0]=     (self.decisionVec[0]) + (self.decisionVec[1]) - 2
        constCheckerVec[1]= 6 - (self.decisionVec[0]) - (self.decisionVec[1])
        constCheckerVec[2]= 2 - (self.decisionVec[1]) + (self.decisionVec[0])
        constCheckerVec[3]= 2 - (self.decisionVec[0]) + (3*self.decisionVec[1])
        constCheckerVec[4]= 4 - (self.decisionVec[3]) - math.pow(((self.decisionVec[2]) - 3), 2)
        constCheckerVec[5]=     math.pow((self.decisionVec[4]-3), 3) + ((self.decisionVec[5]) - 4)
        for cnt in range(0,self.numOfDec):
            if (self.decisionVec[cnt] < self.lowerRange[cnt]) or (self.decisionVec[cnt]>self.upperRange[cnt]) or (constCheckerVec[cnt] < 0):
              return False
        return True


    def getobj(self):
        giveSquaredValue = lambda val : math.pow(val, 2)
        f1=-(
             25 * math.pow((self.decisionVec[0]-2), 2)+
             math.pow((self.decisionVec[1]-2), 2)     +
             math.pow((self.decisionVec[2]-1), 2)     *
             math.pow((self.decisionVec[3]-4), 2)     +
             math.pow((self.decisionVec[4]-1), 2)
             )

        f2=(
             giveSquaredValue(self.decisionVec[0]) +
             giveSquaredValue(self.decisionVec[1]) +
             giveSquaredValue(self.decisionVec[2]) +
             giveSquaredValue(self.decisionVec[3]) +
             giveSquaredValue(self.decisionVec[4]) +
             giveSquaredValue(self.decisionVec[5])
           )
        return [f1,f2]



class Schaffer(Model):

    def __init__(self):
        ## first specify the requirements
        self.decisionVec=[0]
        self.lowerRange=[-100000]
        self.numOfDec=1
        self.numOfObjs=2
        self.upperRange=[100000]
        ## then create the initialization
        self.generateInitialVector()
        self.baseline = [999999, 0]

    def getobj(self):
        f1=math.pow(self.decisionVec[0], 2)
        f2=math.pow((self.decisionVec[0]-2), 2)
        return [f1,f2]


#    def updateBaseline(self, baselineParam):
#      self.baseline =   [_ for _ in   baselineParam ]
#    def getCurrentBaseline(self):
#      return self.baseline
#    def sumOfObjsInit(self):
#        return float(sum(self.getobj()))


class Kursawe(Model):

    def __init__(self):
        ## first specify the requirements
        self.decisionVec=[0,0,0]
        self.lowerRange=[-5,-5,-5]
        self.numOfDec=3
        self.numOfObjs=2
        self.upperRange=[5,5,5]
        ## then create the initialization
        self.generateInitialVector()

    def getobj(self):
        f1=0
        f2=0
        theA = 0.8
        theB = 1.0
        for cntI in range(0,self.numOfDec):
            if cntI< self.numOfDec-1:
                f1 = f1 + ( -10*math.exp(-0.2*math.sqrt( math.pow( self.decisionVec[cntI], 2) + math.pow( self.decisionVec[cntI+1], 2))))
                f2 = f2 + ( math.pow( abs(self.decisionVec[cntI]), theA ) + 5 * math.sin( math.pow( self.decisionVec[cntI], theB) ) )
        return [f1,f2]
class dtlz7(Model):

    def __init__(self):
        ## first specify the requirements
        self.decisionVec=[0,0,0, 0,0,0, 0,0,0, 0]
        self.lowerRange= [0,0,0, 0,0,0, 0,0,0, 0]
        self.numOfDec=10
        self.numOfObjs=2
        self.upperRange= [1,1,1, 1,1,1, 1,1,1, 1]
        ## baseline
        self.baseline = [9999999, 0]
        ## then create the initialization
        self.generateInitialVector()


    def calcG(self, decVecParam):
      res= float(0)
      res = 1 + float(9)/float(len(decVecParam)) * sum(decVecParam)
      return float(res)

    def calcH(self, f1Obj, gValueParam):
       res= float(0)
       res  = float(self.numOfObjs) - float(f1Obj/( 1 + gValueParam)) * float(1 + math.sin(3* math.pi*f1Obj))
       return res

    def getobj(self):
        gVal = self.calcG(self.decisionVec)
        f1=self.decisionVec[0]
        f2= (1 + gVal) * self.calcH(f1, gVal)
        return [f1,f2]

    def copy(self,other):
        self.decisionVec = [_ for _ in other.decisionVec]
        self.lowerRange = [_ for _ in other.lowerRange]
        self.numOfDec = other.numOfDec
        self.numOfObjs = other.numOfObjs
        self.upperRange = [_ for _ in other.upperRange]
        self.baseline = [_ for _ in other.baseline]


class BaseLine():
  baseline_min=9999999
  baseline_max=0
  is_baseline_set=False

  @staticmethod
  def getInitialBaseline(modelParam):
      tries=1000
      # tries=1
      minEnergy = 9999999
      maxEnergy = 0
      modelObj = modelParam()
      for cnt in range(tries):
        modelObj.generateInitialVector()
        energyToCheck = modelObj.sumOfObjs()
        if energyToCheck < minEnergy:
          minEnergy = energyToCheck
        if maxEnergy < energyToCheck:
          maxEnergy = energyToCheck
      #print "min : {}, max: {} in Baseline.getInitialBaseline()".format(minEnergy, maxEnergy)

      return [minEnergy, maxEnergy]



