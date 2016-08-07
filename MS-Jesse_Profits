'''
Jesse has started stock trading and loves it. He knows the prices of a share of a particular company over the next N days. He wants to analyze this data to build a model which can predict the best day to buy and sell the shares. Given an amount, he wants to know if the given desirable amount of profit can be made. If yes, he wants to know the minimum number of days in which it can be made. If there are multiple ways of buying and selling to achieve that profit, he wants to know the way which happens the earliest.
'''


numdays, numprofits = map(int,(raw_input().split()))
prices = map(int, raw_input().split())

for _ in range(numprofits):
    pricenearestday = {}
    profit = int(raw_input())
    leastdays = None
    out1 = None
    out2 = None
    
    for day in range(0, numdays):
        sellprice = prices[day]
        buyprice = sellprice - profit
        buyday = pricenearestday.get(buyprice, -1)
        
        if buyday >= 0:
            dayshold = day - buyday
            
            if leastdays == None or dayshold < leastdays:
                leastdays = dayshold
                out1, out2 = buyday+1, day+1
                
        pricenearestday[sellprice] = day
        
    if out1 == None:
        print -1
    else:
        print out1, out2
