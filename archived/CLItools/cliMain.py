import argparse
from cliGraph import graphData

#TESTS
#newGraph = graphData(fileIn = "patreading.txt", fileGraph="clitest1", dateFilter=[2021,3,25])
parser = argparse.ArgumentParser(description="populates graph from specified parameters")

parser.add_argument('-f', '--fileIn', type=str, help="file name to be processed")
#parser.add_argument('-g', '--fileGraph', type=ascii, help="filename to output graph")
parser.add_argument('-y', '--year', type=int, required=True, help="Year")
parser.add_argument('-m', '--month', type=int,required=False, help="Month")
parser.add_argument('-d', '--day', type=int, required=False, help="Day")
args = parser.parse_args()



def graphBuild(fileIn, fileGraph, dateFilter):

    newGraph = graphData(fileIn = fileIn, fileGraph = fileGraph, dateFilter = dateFilter)

if __name__ == '__main__':
    
    fileGraph = input("Please enter a filename for the graph: ")
    if args.day:
        dateFilter = [args.year, args.month, args.day]
        graphBuild(args.fileIn, fileGraph, dateFilter)
    elif args.month:
        dateFilter = [args.year, args.month]
        graphBuild(args.fileIn, fileGraph, dateFilter)
    else:
        dateFilter = [args.year]
        graphBuild(args.fileIn, fileGraph, dateFilter)
