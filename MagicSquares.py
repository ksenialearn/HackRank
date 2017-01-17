'''
Consider a  matrix of integers in the inclusive range(1,9) . Any digit,a , can be changed to any other digit,b ,  at cost|a-b| .

Given matrix , convert it into a magic square by changing zero, one, or more of the digits. You must do this in such a way that 
the cost is minimal and then print the minimum possible cost on a new line.
'''


import sys

line1 = map(int, raw_input().strip().split(" "))
line2 = map(int, raw_input().strip().split(" "))
line3 = map(int, raw_input().strip().split(" "))


matrix = [line1, line2, line3]

magics = [[[8,1,6], [3,5,7], [4,9,2]],
[[6,1,8], [7,5,3], [2,9,4]],
[[4,9,2], [3,5,7], [8,1,6]],
[[2,9,4], [7,5,3], [6,1,8]]]



def transpose(matrix):
    out = [[8,1,6], [3,5,7], [4,9,2]]
    for row in range(0,3):
        for col in range(0,3):
            out[row][col] = matrix[col][row]         
    return out



for mat in range(0,4):
    magics.append(transpose(magics[mat]))
    


def countCost(magic, matrix):
    cost = 0
    
    for line in range(0,3):
        for num in range(0,3):
            
            current = matrix[line][num]
            new = magic[line][num]
            if new != current:
                cost += abs(current - new)
                
    return cost

lowestcost = sys.maxint

for magic in magics:
    lowestcost = min(lowestcost, countCost(magic,matrix))
    
    
print lowestcost
