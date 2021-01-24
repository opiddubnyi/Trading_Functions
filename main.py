import time
import random
import string
import requests
import datetime
import os
import numpy as np
import pandas as pd
# from COT import downloadFile
# from COT import renameFile
# from COT import getFile
# from COT import searchMe
# from COT import removeChar
# from COT import getCOTcommercial
# from COT import getOI
# from COT import getCOTlargeTraders

# metalsURL = 'https://www.cftc.gov/dea/futures/other_sf.htm'
# # energyURL = 'https://www.cftc.gov/dea/futures/petroleum_sf.htm'
# # gasURL = 'https://www.cftc.gov/dea/futures/nat_gas_sf.htm'
from COT import getSymbolData

wheat = "001602"
data2010 = 'D:\\Trading\\COT project\\annual2010.txt'
data2011 = 'D:\\Trading\\COT project\\annual2011.txt'
data2012 = 'D:\\Trading\\COT project\\annual2012.txt'
data2013 = 'D:\\Trading\\COT project\\annual2013.txt'
data2014 = 'D:\\Trading\\COT project\\annual2014.txt'
data2015 = 'D:\\Trading\\COT project\\annual2015.txt'
data2016 = 'D:\\Trading\\COT project\\annual2016.txt'
data2017 = 'D:\\Trading\\COT project\\annual2017.txt'
data2018 = 'D:\\Trading\\COT project\\annual2018.txt'
data2019 = 'D:\\Trading\\COT project\\annual2019.txt'
data2020 = 'D:\\Trading\\COT project\\annual2020.txt'
data2021 = 'D:\\Trading\\COT project\\annual2021.txt'


def getSymbolData(fileAddress, cftcCode):
    """Returning a list of strings for specific cftcCode of symbol
    :rtype: object
    """

    symbolYearlyData = []
    array = []
    # reading txt file and writing its content into a list                txt -> list of strings
    with open(fileAddress) as file:
        for line in file:
            array.append(line.strip())

    # get all that contain cftcCODE
    for lines in range(len(array)):
        if array[lines].__contains__(cftcCode):
            symbolYearlyData.append(array[lines])
            continue
    return array



def makeDictionary(symbolName, dataList):
    weeklyData = []
    result = [[]]
    for lines in range(len(dataList)):
        weeklyData = dataList[lines].split(',')
        result.append(weeklyData)

    return result
    # outDictionary = {symbolName: weeklyData}
    # return outDictionary


# w = getSymbolData(data2018, wheat)
# for weeks in w:
#     print(w)


def test(fileAddress, cftcCode):
    f = open(fileAddress)
    wr = open('test.txt')
    out =[]
    for lines in f:
        out.append((f.readlines()))
    return out


print(getSymbolData(data2010, wheat))

# print(makeDictionary(wheat, w))

