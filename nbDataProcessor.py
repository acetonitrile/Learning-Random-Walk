#we will use the data from the current tick and the 4 previous ones as 
#features of the price of the next tick
from math import log10
import csv
with open('IVE_tickbidask.txt', 'r') as datafile, open('IVEfeatures.txt', 'w') as featuresfile, open('IVEtarget.txt', 'w') as targetfile:
#the list are used to store the last 5 tick's data
    pPrice=[None, None, None, None, None]
    pBid=[None, None, None, None, None]
    pAsk=[None, None, None, None, None]
    pVol=[None, None, None, None, None]
    i=0
    featureswriter=csv.writer(featuresfile, delimiter=',')
    for line in datafile:
        data=line.split(",")
        price=float(data[2])
        bid=float(data[3])
        ask=float(data[4])
        vol=float(data[5])
#The data have some errors/anomalies, so we exclude ticks that have a
#bid or ask that is zero
        if bid==0 or ask==0: continue
#The assumption made here is that the price of a security follows a 
#lognormal distribution during a short period of time 
        price=log10(price)
#We are also assuming that the bid and the ask is also lognormally distributed
#and so the between the logarithm of the bid and price and ask and price 
#is also normally distributed
        bid=log10(bid)-price
        ask=log10(ask)-price
        i+=1
        pPrice.append(price)
        pBid.append(bid)
        pAsk.append(ask)
        pVol.append(vol)

        pPrice.pop(0)
        pBid.pop(0)
        pAsk.pop(0)
        pVol.pop(0)

        row=pPrice[:]
#begin writing the data after the list have started to be filled up
        if i >4:
            row.extend(pBid)
            row.extend(pAsk)
            row.extend(pVol)
            featureswriter.writerow(row)
            targetfile.write(str(price))
            targetfile.write(',')
        if i >45000:
            break
