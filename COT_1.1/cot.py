def getSymbolData(fileAddress, cftcCode):
    """Returning a list of strings for specific cftcCode of symbol
    :rtype: object
    """

    symbolYearlyData = []
    array = []
    # reading txt file and writing its content into a list                txt -> list of strings
    with open(fileAddress) as file:
        for line in file:
            array.append(line.strip('\n'))

    # get all that contain cftcCODE
    for lines in range(len(array)):
        if array[lines].count(cftcCode) >= 1:
            symbolYearlyData.append(array[lines])
    return symbolYearlyData


