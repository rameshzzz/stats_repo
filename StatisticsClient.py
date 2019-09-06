import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from StatisticsCalculator import StatisticsCalculator



def loadcsv(filename):
    df = pd.read_csv(filename)
    return df


datafile=loadcsv("data.csv")
dfpe =datafile['PE']
dfbv=datafile['PBV']
dfgroup=datafile['Group']


c1 = StatisticsCalculator(datafile,dfpe)
#c1.print_details()

mean1=c1.getMean()
print("mean :",mean1)
median1=c1.getMedian()
print("median :",median1)
mode1=c1.getMode()
print("mode :",mode1)
sd1=c1.getStdDevn()
print("std dev :",sd1)
variance1=c1.getVariance()
print("variance :",variance1)
q1=c1.getQ1()
print("Q1 :",q1)
q3=c1.getQ3()
print("Q3 :",q3)
iqr=c1.getIQR()
print ("IQR :",iqr)
uFence=c1.getUpperFence()
print ("Upper Fence :",uFence)
lFence=c1.getLowerFence()
print ("Lower Fence :",lFence)
zscores1=c1.getZscores()
print ("Z scores :",zscores1)
x=c1.getAllOutliers()
print(x)
y=c1.removeAllOutliers()
print(y)

pearsoncoeff=c1.getPearsonCorrelationBetweenColumns(dfbv,dfpe)
print(" Pearsons coefficient of correlation : ",pearsoncoeff)
pValue=c1.getPValueBetweenColumns(dfbv,dfpe)
print(" P-Value of correlation : ",pValue)
covar=c1.getCovarianceBetweenGroups(dfbv,dfpe)
print("covariance :\t",covar)

c1.drawPie(dfgroup)
c1.drawBarChart(dfgroup,"Stock Groups","Stock group","Frequency")


