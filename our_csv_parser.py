#!/usr/bin/env python

import os

myfilename = "housing.data.txt"

# homework 1
# start with empty list for cleaned values to concatenate to
list1=[]

with open(myfilename, 'r') as file_handle:
    for line in file_handle.readlines():
        line_clean = line.replace('   ', ' ').replace('  ', ' ')
        line_clean = line_clean.strip()
        values = line_clean.split(' ')

        for value in values:
            try:
                list1+=[int(value)]
            except:
                list1+=[float(value)]

print(list1)

# reach homework
# start with empty lists for each to append to
col1 = []
col2 = []
col3 = []
col4 = []
col5 = []
col6 = []
col7 = []
col8 = []
col9 = []
col10 = []
col11 = []
col12 = []
col13 = []
col14 = []

# append elements to list of specified column
for idx in range(0, len(list1), 14):
    col1.append(list1[idx])

for idx in range(1, len(list1), 14):
    col2.append(list1[idx])

for idx in range(2, len(list1), 14):
    col3.append(list1[idx])

for idx in range(3, len(list1), 14):
    col4.append(list1[idx])

for idx in range(4, len(list1), 14):
    col5.append(list1[idx])

for idx in range(5, len(list1), 14):
    col6.append(list1[idx])

for idx in range(6, len(list1), 14):
    col7.append(list1[idx])

for idx in range(7, len(list1), 14):
    col8.append(list1[idx])

for idx in range(8, len(list1), 14):
    col9.append(list1[idx])

for idx in range(9, len(list1), 14):
    col10.append(list1[idx])

for idx in range(10, len(list1), 14):
    col11.append(list1[idx])

for idx in range(11, len(list1), 14):
    col12.append(list1[idx])

for idx in range(12, len(list1), 14):
    col13.append(list1[idx])

for idx in range(13, len(list1), 14):
    col14.append(list1[idx])

# print newly formed lists
print(col1)
print(col2)
print(col3)
print(col4)
print(col5)
print(col6)
print(col7)
print(col8)
print(col9)
print(col10)
print(col11)
print(col12)
print(col13)
print(col14)

print('finished!')
