# graphClass modified  
# for GUItools
# 
 
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.dates import DayLocator, HourLocator, DateFormatter

from datetime import date, time, datetime

class graphData:
    
    def getFig(self):
        return self.figOut
    
    def getDate(self):
        #self.fileClean()
        ln = len(self.dateFilter)
        if ln == 3:
            return f"{self.dateFilter[1]}/{self.dateFilter[2]}/{self.dateFilter[0]}"
        if ln == 2:
            return  f"{self.dateFilter[1]}/{self.dateFilter[0]}"
        if ln == 1:
            return f"{self.dateFilter[0]}" 
    
    def getList(self):
        temp = []
        filterList = self.queryList
        for i in range(len(filterList)):
            filterList[i][0] = (filterList[i][0]).strftime("%m/%d/%Y, %H:%M:%S") 
           # temp.append(f"{filterList[i][0]}, {filterList[i][1]}")
             
        return filterList

    def returnFig(self, filterList):
        
        graphFile = self.fileGraph
        graphFile = graphFile + ".png"
        myDates = []
        mySugars = []
        for i in range(len(filterList)):
            myDates.append(filterList[i][0])
            mySugars.append(float(filterList[i][1]))
        
        x = matplotlib.dates.date2num(myDates)
        y = mySugars

        fig = matplotlib.pyplot.figure()
        matplotlib.pyplot.plot_date(x, y, 'o-', label="mg/dl")
        fig.autofmt_xdate()

        fig.savefig(graphFile)
        #plt.show()
        self.figOut = fig
       # return fig    

    def timeFilter(self, filterList):
    # will filter by datetime
    # determines choice by length of array passed in 
    # instantiation of the class
        queryList = []
        choice = int(len(self.dateFilter))
        
        myYear = self.dateFilter[0]

        if choice == 1:

            for i in range(len(filterList)):
                if filterList[i][0].year == int(myYear):
                    queryList.append(filterList[i])

        elif choice == 2:

            myMonth = self.dateFilter[1]

            for i in range(len(filterList)):
                if filterList[i][0].year == int(myYear):
                    if filterList[i][0].month == int(myMonth):
                        queryList.append(filterList[i])

        elif choice == 3:
            
            myMonth = self.dateFilter[1]
            myDay = self.dateFilter[2]

            for i in range(len(filterList)):
                if filterList[i][0].year == int(myYear):
                    if filterList[i][0].month == int(myMonth):
                        if filterList[i][0].day == int(myDay):
                            queryList.append(filterList[i])
        self.queryList = queryList
        self.returnFig(queryList)

    def filterList(self):

            # creates new list of lists with 2 indices
            # myList[n][0] datetime object
            # myList[n][1] blood glucose reading
        myList = self.allReadings
        tempList = []

        for i in range(len(myList)):
            tempDate = date.fromisoformat(str(myList[i][0]))
            tempTime = time.fromisoformat(str(myList[i][1]))
            tempDateTime = datetime.combine(tempDate, tempTime)
            tempList.append([tempDateTime, myList[i][2]])

        return self.timeFilter(tempList)


    def fileClean(self):
        
        file = self.fileIn

        edit = open(file, "r")
        edit.seek(0,0)

        for line in edit:
            lin = edit.readline()

            try:
                reading = [lin[1]]

                for i in range(2,11):
                    reading[0] = reading[0] + lin[i]

                self.dates.append(reading[0])
                reading.append(lin[12])

                for i in range(13,20):
                    reading[1] = reading[1] + lin[i]

                self.times.append(reading[1])
                reading.append(lin[23])

                for i in range(24,28):
                    reading[2] = reading[2] + lin[i]

                self.bloodSugar.append(reading[2])

                self.allReadings.append(reading)

            except IndexError:
                print("Processing Completed")
           #break
                return self.filterList()

     

    def __init__(self, fileIn, fileGraph, dateFilter):
        # fileIn = name of file with readings
        # fileGraph = select name for graph image file to be generated
        # dateFilter, filtering parameters Year, month ,day in list.
        self.allReadings = []
        self.dates = []
        self.times = []
        self.bloodSugar = []
        self.fileGraph = fileGraph
        self.fileIn = fileIn
        self.dateFilter = dateFilter
        self.figOut = None
        self.queryList = []          
        self.fileClean()
         
#TESTS
# newGraph = graphData(fileIn = "patreading.txt", fileGraph="clitest1", dateFilter=[2021,3,25])



