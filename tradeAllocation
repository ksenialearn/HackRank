#Fixed-Income Security Trade Allocation
#BlackRock CodeSprint

numPort= int(raw_input())
minimum_trade_size, increment, available_units = map(int,raw_input().strip().split())

portfolioID = []
portfolioOrder = {}

for i in range(0,numPort):    
    inp = raw_input().strip().split()
    portfolioID.append(inp[0])
    portfolioOrder[inp[0]]= int(inp[1])

def orderSize(pid): return portfolioOrder[pid]

if available_units >= sum(portfolioOrder.values()):
    for i in range(0, numPort):
        print portfolioID[i], int(portfolioOrder[portfolioID[i]])
                          
else:
    portfolioIDcopy= portfolioID[:]
    portfolioID.sort(key = lambda i : (portfolioOrder[i], i))
    totalOrder= sum(map(orderSize, portfolioID))
    
    portAlloc= {}
    
    for i in range(numPort):
        portOrder= portfolioOrder[portfolioID[i]]
        allocation= round(portOrder*1.0/totalOrder * available_units,0)
        portAlloc[portfolioID[i]]= 0

        
        if allocation < minimum_trade_size:
            if allocation > minimum_trade_size/2:
                if (portOrder- minimum_trade_size- minimum_trade_size)%increment== 0:
                    portAlloc[portfolioID[i]]= minimum_trade_size #check is possible, else allocate nothing
        
        else:
            if allocation >= portOrder:
                portAlloc[portfolioID[i]]= portOrder
                
            else:
                while (allocation - minimum_trade_size)%increment !=0:
                    allocation-=1
                    
                if(portOrder - allocation - minimum_trade_size)%increment == 0:
                    portAlloc[portfolioID[i]]= allocation
                    
        
        
        totalOrder-= portOrder 
        available_units-= portAlloc[portfolioID[i]]
        
for i in range(numPort):
    print portfolioIDcopy[i], portAlloc[portfolioIDcopy[i]]
                
