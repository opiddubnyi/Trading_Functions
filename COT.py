
#
# сurrentDate = datetime.datetime.today().strftime('%d-%b-%Y')
# oi = []
# cotCom = []
# cotLargeTraders = []
# cotSpeculative = []
#
#
# # downloading file - no output
# def downloadFile(func_url):
#     req = requests.get(func_url)
#     filename = req.url[func_url.rfind('/') + 1:]
#
#     with open(filename, 'wb') as f:
#         for chunk in req.iter_content(chunk_size=8192):
#             if chunk:
#                 f.write(chunk)
#     try:
#         if filename:
#             pass
#         else:
#             filename = req.url[func_url.rfind('/') + 1:]
#
#         with requests.get(func_url) as req:
#             with open(filename, 'wb') as f:
#                 for chunk in req.iter_content(chunk_size=8192):
#                     if chunk:
#                         f.write(chunk)
#             return filename
#     except Exception as e:
#         print(e)
#         return None
#
#
# # renaming downloaded file - no output
# def renameFile(fileName):
#     req = requests.get(fileName)
#     newName = req.url[fileName.rfind('/') + 1:]
#     os.rename('D:\\Python\\Projects\\' + str(newName),
#               'D:\\Python\\Projects\\' + str(newName[:-4]) + '_' + str(сurrentDate) + '.htm')
#
#
# # converting downloaded UP to DATE file into not formatted array by URL name of the file -> array[]
# def getFile(urlName):
#     req = requests.get(urlName)
#     newName = req.url[urlName.rfind('/') + 1:]
#     string = 'D:\\Python\\Projects\\' + str(newName[:-4]) + '_' + str(сurrentDate) + '.htm'
#     with open(string) as file:
#         array = [row.strip() for row in file]
#         return array
#
#
# # Locating smaller  SubArray by the name of the symbol -> output array with symbol Data
# def searchMe(array, keyWord):
#     for el in array:
#         if el.__contains__(keyWord):
#             startRow = array.index(el)
#             return array[startRow - 3:startRow + 13]
#
#
# # removing all ',' symbols from spreadsheet so we can manipulate it as int
# def removeChar(string):
#     return string.replace(',', '')
#
#
# # returning COT commercial data for formatted symbol list
# def getCOTcommercial(list):
#     currentDate = datetime.datetime.today().strftime('%d-%b-%Y')
#
#     stringCOT = removeChar(list[6])
#     currentCOT = stringCOT.split()
#     cotCom = int(currentCOT[1]) + int(currentCOT[3]) - int(currentCOT[4]) - int(currentCOT[2])
#
#     return cotCom
#
#
# # returning OI data from a formatted symbol list
#
# def getOI(list):
#     currentDate = datetime.datetime.today().strftime('%d-%b-%Y')
#     stringOI = removeChar(list[4])
#     currentOI = stringOI.split()
#     oi = currentOI[6]
#
#     return oi
#
#
# # returning COT Large Trader data for formatted symbol list
# def getCOTlargeTraders(list):
#     stringCOTlarge = removeChar(list[6])
#     currentCOTlarge = stringCOTlarge.split()
#     cotLargeTraders = int(currentCOTlarge[6]) - int(currentCOTlarge[7])
#
#     return cotLargeTraders


# Returning a list of strings for specific cftcCode of symbol. Contains full year data


def getSymbolData(fileAddress, cftcCode):
    """Returning a list of strings for specific cftcCode of symbol
    :rtype: object
    """

    symbolYearlyData = []
    # reading txt file and writing its content into a list                txt -> list of strings
    with open(fileAddress) as file:
        array = [row.strip() for row in file]
    # get all that contain cftcCODE
    for lines in range(len(array)):
        if array[lines].__contains__(cftcCode):
            symbolYearlyData.append(array[lines])
            continue
    return symbolYearlyData
