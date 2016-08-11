
A polygon is a closed shape with three or more sides. For example, triangles are polygons. A polygon is non-degenerate if it has no overlapping sides (and no sides of zero length).

You have  sticks with positive integer lengths, . You want to create a polygon using all  sticks. Because this is not always possible, you can cut one or more sticks into two smaller sticks (they do not necessarily need to be of integer length) and repeat the process of trying to create a polygon using all the sticks. Given the lengths of all  sticks, find and print the minimum number of cuts necessary to make a non-degenerate polygon.


n = int(raw_input().strip())
a = map(int,raw_input().strip().split(' '))

if n<3:
    print 3 - n

elif n == 3:
    if a[0] + a[1] <= a[2] or a[0] + a[2] <= a[1] or a[1] + a[2] <= a[0]:
        print 1
          
    else:
        print 0
else:
    print 0
