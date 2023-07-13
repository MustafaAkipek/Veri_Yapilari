# Big(O) Notation -> Represent Worst Case Scenario
# Time Complexity(Zaman Karmaşıklığı) - Space Complexity(Alan Karmaşıklığı)
# Time Complexity yazılan algoritmanın çalışma süresi
# Space Complexity yazılan algoritmanın bellekte tuttuğu yer

# Big(O) Complexity Chart From Good to Bad
# O(1) - O(log n) - O(n) - O(n log n) - O(n^2) - O(2^n) - O(n!)

def bigon(n):
    for i in range(0, n):
        print(i)

def bigon2(n):
    for i in range(0, n):
        for j in range(0, n):
            print(i, j)

def bigon3(n):
    for i in range(0, n):
        for j in range(0, n):
            for k in range(0, n):
                print(i, j, k)

import math

def logn(n):
    while n > 1:
        n = math.floor(n/2)
        print(n)

def nlogn(n):
    lim = n
    while n > 1:
        n = math.floor(n/2)
        for i in range(1, lim):
            print(i)

def nfactorial(n):
    if n == 0:
        print("1")
    else:
        for i in range(0, n):
            print(i)
            nfactorial(n-1) # recursive

def actualFactorial(n):
    if (n == 1 or n == 0):
        return 1
    else:
        return (n * actualFactorial(n-1))
    
