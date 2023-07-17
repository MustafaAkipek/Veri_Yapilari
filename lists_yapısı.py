# What Is a List in Python?
# 1- Lists are ordered
# 2- Lists are mutable
# 3- List elements do not need to be unique
# 4- Different data types

myList = [1, 2, 3, 4, 5]
otherList = [6, 7, 8]
myList.extend(otherList)

import sys

n = 30
myDynamicArray = []

for i in range(0, n):
    myLength = len(myDynamicArray)
    myByte = sys.getsizeof(myDynamicArray)
    print(f"Length: {myLength} Byte: {myByte}")
    myDynamicArray.append(n)