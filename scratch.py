import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats


def hello(name):
    """
    :rtype: basestring.
    """
    print("Hello World from :", name)


def getMean(nparr):
    return (np.nanmean(nparr))

def getMedian(nparr):
    return (np.median(nparr))

def getMode(nparr):
    return (stats.mode(nparr)[0][0])

def getStdDevn(nparr):
    return (np.nanstd(nparr))

def getVariance(nparr):
    return (np.nanvar(nparr))


def getQ1(nparr):
    return (np.percentile(nparr,25))

def getQ3(nparr):
    return (np.percentile(nparr,75))

def getIQR(nparr):
    q1=np.percentile(nparr,25)
    q3=np.percentile(nparr,75)
    return(q3-q1)

def getUpperFence(nparr):
    q33=getQ3(nparr)
    iqr1=getIQR(nparr)
    paddedIQR=(1.5*iqr1)
    upperFence=q33+paddedIQR
    return upperFence

def getLowerFence(nparr):
    q11 = getQ1(nparr)
    iqr2 = getIQR(nparr)
    paddedIQR = (1.5 * iqr2)
    lowerFence = q11 - paddedIQR
    return lowerFence

def getZscores(nparr):
    return stats.zscore(nparr)


def getAllOutliers(nparr):
    outliers = [x for x in nparr if x < getLowerFence(nparr) or x > getUpperFence(nparr)]
    #print('Identified outliers : ', outliers)
    return outliers

def removeAllOutliers(nparr):
    col_with_outliers_removed = [x for x in nparr if x >= getLowerFence(nparr) and x <= getUpperFence(nparr)]
    return col_with_outliers_removed

def drawPie(nparr):
    '''
    To be used ideally only for categorical data , i.e < 10 distinct values
    :param nparr: numpy array column
    :return: none
    '''
    uniqueValues, occurCount = np.unique(nparr, return_counts=True)
    uniqueCount=len(uniqueValues)
    totalCount=np.sum(occurCount)
    print("Unique Values : ", uniqueValues)
    print("Occurrence Count : ", occurCount)
    print("Total count :",totalCount)
    # print ("# of unique values :",len(uniqueValues))

    if (uniqueCount>=10):
        print(" Too many values : not suited for pie chart ")
    else:
        labels=uniqueValues
        sizes = occurCount

        explode = (0, 0.1, 0,0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
                shadow=True, startangle=90)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        plt.show()


def drawBarChart(nparr,chartName,xlabel,ylabel):
    uniqueValues, occurCount = np.unique(nparr, return_counts=True)
    uniqueCount = len(uniqueValues)
    totalCount = np.sum(occurCount)
    print("Unique Values : ", uniqueValues)
    print("Occurrence Count : ", occurCount)
    print("Total count :", totalCount)
    print ("# of unique values :",uniqueCount)
    figureObject, axesObject = plt.subplots()
    categories = np.arange(uniqueCount)

    # Customize bar properties
    barWidth = 0.4
    barOpacity = 0.5
    errorConfig = {'ecolor': '0.2'}

    barChart = plt.bar(categories,occurCount,barWidth,alpha=barOpacity,
                           color='blue',label=chartName)

    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(chartName)
    plt.xticks(categories, uniqueValues)
    plt.legend()

    plt.tight_layout()
    plt.show()


def getPearsonCorrelationBetweenColumns(nparrcolumn1,nparrcolumn2):
    corr = stats.pearsonr(nparrcolumn1,nparrcolumn2)
    #print("correlation coefficient:\t\t", corr[0])
    return corr[0]

def getPValueBetweenColumns(nparrcolumn1,nparrcolumn2):
    corr = stats.pearsonr(nparrcolumn1,nparrcolumn2)
    #print("p-value:\t", corr[1])
    return corr[1]

def getCovarianceBetweenGroups(nparrcolumn1,nparrcolumn2):
    cov_mat = np.stack((nparrcolumn1,nparrcolumn2), axis=0)
    covar=np.cov(cov_mat)[0][1]
    #print("covariance :\t ",covar)
    return covar



hello("ramesh")


df=pd.read_csv("data.csv")
print(df.describe())
print(df)
df1 =df['PE']
print(df1)
df2=df['Group']
print(df2)

mean1=getMean(df1)
print("mean :",mean1)
median1=getMedian(df1)
print("median :",median1)
mode1=getMode(df1)
print("mode :",mode1)
sd1=getStdDevn(df1)
print("std dev :",sd1)
variance1=getVariance(df1)
print("variance :",variance1)
q1=getQ1(df1)
print("Q1 :",q1)
q3=getQ3(df1)
print("Q3 :",q3)
iqr=getIQR(df1)
print ("IQR :",iqr)
uFence=getUpperFence(df1)
print ("Upper Fence :",uFence)
lFence=getLowerFence(df1)
print ("Lower Fence :",lFence)
zscores1=getZscores(df1)
print ("Z scores :",zscores1)
x=getAllOutliers(df1)
print(x)
y=removeAllOutliers(df1)
print(y)
pearsoncoeff=getPearsonCorrelationBetweenColumns(df['PBV'],df['PE'])
print(" Pearsons coefficient of correlation : ",pearsoncoeff)
pValue=getPValueBetweenColumns(df['PBV'],df['PE'])
print(" P-Value of correlation : ",pValue)
covar=getCovarianceBetweenGroups(df['PBV'],df['PE'])
print("covariance :\t",covar)
#drawPie(df2)
#drawBarChart(df2,"Stock Groups","Stock group","Frequency")
