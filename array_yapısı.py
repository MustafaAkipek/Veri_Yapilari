# What Is an Array in Python?
# Like lists, array are orderd, mutable, enclosed in square brackets, and able to store non-unique items.
# But when it comes to the array's ability to store different data types, the answer is not as straight.
# To use arrays in Python, you need to import either an array module or a NumPy package.

import array as arr

# Array module requires all array elements to be of the same type.
myArray = arr.array("i", [3, 6, 9, 12])
print(myArray, type(myArray))
