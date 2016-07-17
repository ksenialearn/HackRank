'''
Given an array  of  a elements, find the maximum possible sum of a

Contiguous subarray
Non-contiguous (not necessarily contiguous) subarray.
'''

numCases = int(raw_input())

for i in range(numCases):
    
    inpNum = int(raw_input())
    arrays = map(int, raw_input().split(" "))
    

    
    top= max(arrays)
    if top <= 0:
        print top, top
        continue
        
    cont = 0
    noncont = 0
    subtotal = 0 
    table = []
    
    for num in arrays:
        
        if num >= 0:
            noncont += num
            
        subtotal += num
            
        if subtotal > num:
            table.append(subtotal)
        
        else:
            table.append(num)
            subtotal = num
    
    cont= max(table)
           
    print cont, noncont
