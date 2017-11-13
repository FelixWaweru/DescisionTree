import os
i = 0
rowsNumber = 8
wholeDataSet = []

fileOpen = open('adult.data.txt','r')
while i is not rowsNumber:
    dataRow = fileOpen.readline()
    dataRow = dataRow.split(', ')
    wholeDataSet.append(dataRow)
    i = i+1

length = len(dataRow)
fileOpen.close()
print(wholeDataSet)