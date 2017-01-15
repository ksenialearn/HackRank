'''
Colleen is turning n years old! She has n candles of various heights on her cake, and candle i has height h. Because the taller candles
tower over the shorter ones, Colleen can only blow out the tallest candles.

Given the  for each individual candle, find and print the number of candles she can successfully blow out.

Input Format

The first line contains a single integer, , denoting the number of candles on the cake. 
The second line contains  space-separated integers, where each integer  describes the height of candle .
'''

import sys


n = int(raw_input().strip())
height = map(int,raw_input().strip().split(' '))

candles = {}
tall = 0

for i in range(n):
    candle= height[i]
    
    if candle in candles:
        candles[candle] += 1
    else:
        candles[candle] = 1
    
    if candle > tall:
        tall = candle

print candles[tall]
