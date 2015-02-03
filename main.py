from DictSort import *
from pprint import pprint;

def main():
    zipDict = dict();

    zipDict['98075'] = 100000000000000000000
    zipDict['98029'] = 1000000000000
    zipDict['98052'] = 10000
    mySort = sortByValue(zipDict)
    pprint(mySort)


main();