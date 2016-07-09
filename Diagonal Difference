#Given a square matrix of size NxN , calculate the absolute difference between the sums of its diagonals.

import sys


n = int(raw_input().strip())
a = []
for a_i in xrange(n):
    a_temp = map(int,raw_input().strip().split(' '))
    a.append(a_temp)

mainDiagonal= 0
col= 0


for row in range(n):
    mainDiagonal+= a[row][col]
    col+=1
    
secondDiagonal= 0
col= 0

for row in range(n-1,-1,-1):
    secondDiagonal+= a[row][col]
    col+=1
    
out= abs(mainDiagonal - secondDiagonal)

print out
