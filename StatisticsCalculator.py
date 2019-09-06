import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

class StatisticsCalculator:

    def __init__(self,string1,string2):
        self.dataframe=pd.DataFrame(string1)
        self.npcolumn=np.array(string2)
        print("Creating StatisticsCalculator ")


    def print_details(self):
        """
        Prints the details of the class
        """
        print(self.dataframe.info())
        print("-----")
        print(self.npcolumn)

    def loadcsv(self):
        df=pd.read_csv("data.csv")
        return df


    def getMean(self):
        nparr=self.npcolumn
        #print(nparr)
        x=round(np.nanmean(nparr),3)
        return (x)

    def getMedian(self):
        nparr = self.npcolumn
        x=round(np.median(nparr),3)
        return (x)

    def getMode(self):
        nparr = self.npcolumn
        return (stats.mode(nparr)[0][0])

    def getStdDevn(self):
        nparr = self.npcolumn
        x=round(np.nanstd(nparr),3)
        return (x)

    def getVariance(self):
        nparr = self.npcolumn
        return round((np.nanvar(nparr)),3)

    def getQ1(self):
        nparr = self.npcolumn
        return round((np.percentile(nparr,25)),3)

    def getQ3(self):
        nparr = self.npcolumn
        return round((np.percentile(nparr,75)),3)

    def getIQR(self):
        nparr = self.npcolumn
        q1=np.percentile(nparr,25)
        q3=np.percentile(nparr,75)
        return round((q3-q1),3)

    def getUpperFence(self):
        nparr = self.npcolumn
        q33=self.getQ3()
        iqr1=self.getIQR()
        paddedIQR=(1.5*iqr1)
        upperFence=q33+paddedIQR
        return round(upperFence,3)

    def getLowerFence(self):
        nparr = self.npcolumn
        q11 = self.getQ1()
        iqr2 = self.getIQR()
        paddedIQR = (1.5 * iqr2)
        lowerFence = q11 - paddedIQR
        return round(lowerFence,3)

    def getZscores(self):
        nparr = self.npcolumn
        return stats.zscore(nparr)


    def getAllOutliers(self):
        nparr = self.npcolumn
        outliers = [x for x in nparr if x < self.getLowerFence() or x > self.getUpperFence()]
        #print('Identified outliers : ', outliers)
        return outliers

    def removeAllOutliers(self):
        nparr = self.npcolumn
        col_with_outliers_removed = [x for x in nparr if x >= self.getLowerFence() and x <= self.getUpperFence()]
        return col_with_outliers_removed


    def getPearsonCorrelationBetweenColumns(self,nparrcolumn1,nparrcolumn2):
        corr = stats.pearsonr(nparrcolumn1,nparrcolumn2)
        #print("correlation coefficient:\t\t", corr[0])
        return round(corr[0],3)

    def getPValueBetweenColumns(self,nparrcolumn1,nparrcolumn2):
        corr = stats.pearsonr(nparrcolumn1,nparrcolumn2)
        #print("p-value:\t", corr[1])
        return round(corr[1],3)

    def getCovarianceBetweenGroups(self,nparrcolumn1,nparrcolumn2):
        cov_mat = np.stack((nparrcolumn1,nparrcolumn2), axis=0)
        covar=np.cov(cov_mat)[0][1]
        #print("covariance :\t ",covar)
        return round(covar,3)

    def drawPie(self,column):
        '''
        To be used ideally only for categorical data , i.e < 10 distinct values
        :param nparr: numpy array column
        :return: none
        '''
        nparr = np.array(column)
        uniqueValues, occurCount = np.unique(nparr, return_counts=True)
        uniqueCount = len(uniqueValues)
        totalCount = np.sum(occurCount)
        print("Unique Values : ", uniqueValues)
        print("Occurrence Count : ", occurCount)
        print("Total count :", totalCount)
        # print ("# of unique values :",len(uniqueValues))

        if (uniqueCount >= 10):
            print(" Too many values : not suited for pie chart ")
        else:
            labels = uniqueValues
            sizes = occurCount

            explode = (0, 0.1, 0, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
            fig1, ax1 = plt.subplots()
            ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
                    shadow=True, startangle=90)
            ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
            plt.show()

    def drawBarChart(self, column, chartName, xlabel, ylabel):
        nparr = np.array(column)
        uniqueValues, occurCount = np.unique(nparr, return_counts=True)
        uniqueCount = len(uniqueValues)
        totalCount = np.sum(occurCount)
        print("Unique Values : ", uniqueValues)
        print("Occurrence Count : ", occurCount)
        print("Total count :", totalCount)
        print("# of unique values :", uniqueCount)
        figureObject, axesObject = plt.subplots()
        categories = np.arange(uniqueCount)

        # Customize bar properties
        barWidth = 0.4
        barOpacity = 0.5
        errorConfig = {'ecolor': '0.2'}

        barChart = plt.bar(categories, occurCount, barWidth, alpha=barOpacity,
                           color='blue', label=chartName)

        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(chartName)
        plt.xticks(categories, uniqueValues)
        plt.legend()

        plt.tight_layout()
        plt.show()


