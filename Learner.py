import DataSplitter

rawData = DataSplitter.wholeDataSet
length2 = DataSplitter.length
rowsNumber2 =DataSplitter.rowsNumber
# displays the number of >50K and <50K in the data from the last column
lastColumn = [row[length2-1] for row in rawData]
lastUniqueValues = list(set(lastColumn))
lastUniqueValuesLength = len(lastUniqueValues)
lastTotalUnique = []
i = 0
while i is not lastUniqueValuesLength:
    lastTotalUnique.append(lastColumn.count(lastUniqueValues[i]))
    i = i + 1


# iterator for total number of columns
a = 0
# Method to display the number of data from the columns
def counter():
    singleColumn1 = [row[a] for row in rawData]
    print(singleColumn1)
    uniqueValues1 = list(set(singleColumn1))
    print(uniqueValues1)
    uniqueValuesLength1 = len(uniqueValues1)
    print(uniqueValuesLength1)
    # iterator for unique values
    b = 0
    # iterate through number of unique values
    while b is not uniqueValuesLength1:
        print(b)
        c = uniqueValues1[b]
        print(c)
        # iterator for total number of rows
        i = 0
        # iterate through number of rows
        while i is not rowsNumber2:
            print(rawData[0][0])
            if rawData[i][0] is c and rawData[i][length2-1] is lastUniqueValues[0]:
                print("is <=50K")
            elif rawData[i][0] is c and rawData[i][length2-1] is lastUniqueValues[1]:
                print("is >50K")
            i = i+1
        b = b+1

counter()
# print([row[0] for row in rawData])
# print(totalUniqueValues)
# print(uniqueValues)
# print(uniqueValuesLength)
# print(length2)