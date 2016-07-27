'''
Gary is an avid hiker. He tracks his hikes meticulously, paying close attention to small details like topography. During his last hike, he took exactly  steps. For every step he took, he noted if it was an uphill or a downhill step. Gary's hikes start and end at sea level. We define the following terms:

A mountain is a non-empty sequence of consecutive steps above sea level, starting with a step up from sea level and ending with a step down to sea level.
A valley is a non-empty sequence of consecutive steps below sea level, starting with a step down from sea level and ending with a step up to sea level.
Given Gary's sequence of up and down steps during his last hike, find and print the number of valleys he walked through.

Input Format

The first line contains an integer, , denoting the number of steps in Gary's hike. 
The second line contains a single string of  characters. Each character is  (where U indicates a step up and D indicates a step down), and the  character in the string describes Gary's  step during the hike.

'''

num = int(raw_input())

inp = raw_input()

currentlevel = 0
start = False

valleys = 0

for i in range(0, num):
    step = inp[i]
    
    if step == "U":
        currentlevel += 1 
    else:
        currentlevel -= 1

        
    if currentlevel < 0:
        if start == False:
            start = True
    
    if currentlevel == 0:
        if start == True:
            start = False
            valleys += 1
        
print valleys
