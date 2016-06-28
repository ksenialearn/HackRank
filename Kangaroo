'''
There are two kangaroos on an x-axis ready to jump in the positive direction (i.e, toward positive infinity). 
The first kangaroo starts at location  and moves at a rate of  meters per jump. 
The second kangaroo starts at location  and moves at a rate of  meters per jump. 
Given the starting locations and movement rates for each kangaroo, can you determine if they'll ever 
land at the same location at the same time?

x2>x1

'''

import sys


x1,v1,x2,v2 = raw_input().strip().split(' ')
x1,v1,x2,v2 = [int(x1),int(v1),int(x2),int(v2)]

p1= x1
p2= x2

if v1< v2:
    print "NO"
    
    
else:
    while True:
        p1+= v1
        p2+= v2
        if p1> p2:
            print "NO"
            break
        elif p1== p2:
            print "YES"
            break
