'''
Day 28: RegEx, Patterns, and Intro to Databases
Task 
Consider a database table, Emails, which has the attributes First Name and Email ID. Given  rows of data simulating the Emails table print an alphabetically-ordered list of people whose email address ends in 
'''

import sys
import re

N = int(raw_input().strip())

nameList= []
for a0 in xrange(N):
    firstName,emailID = raw_input().strip().split(' ')
    firstName,emailID = [str(firstName),str(emailID)]

    if re.search('@gmail.com$', emailID) is not None:
        nameList.append(firstName)
    
nameList.sort()
for word in nameList:
    print word







