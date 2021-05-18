# filterGraph1.py re-written as an object
# and cleaned up a bit.
# just pass graphData a filename to fileIn arg
# newGraph = graphData(fileIn="myglucosereadings.txt")
# 

import matplotlib
import matplotlib.pyplot as plt
from matplotlib.dates import DayLocator, HourLocator, DateFormatter, drange

import numpy as np

from datetime import date, time, datetime

class graphData:
    
    def graphQuery(self,filterList):
        
        print("\n")
        graphFile = input("Please enter a file name for graph: ")
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
        plt.show()
    
    def timeFilter(self, filterList):
    # will filter by datetime
        queryList = []
        print("Please Select a Filtering Parameter", "\n",
                "1: Year", "\n", "2: Month", "\n", "3: Day", "\n")
        choice = input(":---> ")
        choice = int(choice)

        if choice == 1:

            myYear = input("Enter a year: ")

            for i in range(len(filterList)):
                if filterList[i][0].year == int(myYear):
            #    print(filterList[i])
                    queryList.append(filterList[i])

        elif choice == 2:

            myMonth = input("Enter a month: ")
            myYear = input("Enter a year: ")

            for i in range(len(filterList)):
                if filterList[i][0].year == int(myYear):
                    if filterList[i][0].month == int(myMonth):
             #      print(filterList[i])
                        queryList.append(filterList[i])

        elif choice == 3:

            myYear = input("Enter Year: ")
            myMonth = input("Enter Month: ")
            myDay = input("Enter Day: ")

            for i in range(len(filterList)):
                if filterList[i][0].year == int(myYear):
                    if filterList[i][0].month == int(myMonth):
                        if filterList[i][0].day == int(myDay):
              #          print(filterList[i])
                            queryList.append(filterList[i])

        return self.graphQuery(queryList)

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

     

    def __init__(self, fileIn):
        # fileIn = name of file with readings
        # graphOut = select name for graph image file to be generated
        self.allReadings = []
        self.dates = []
        self.times = []
        self.bloodSugar = []
        self.fileIn = fileIn
        self.fileClean()

#TESTS
newGraph = graphData(fileIn = "patreading.txt")



