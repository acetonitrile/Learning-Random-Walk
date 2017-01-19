from math import log10
with open('IVE_tickbidask.txt', 'r') as datafile, open('IVEtargettrain.txt', 'w') as traintargetfile, open('IVEtargettest.txt', 'w') as testtargetfile:
    i=0
    for line in datafile:
        data=line.split(",")
        price=float(data[2])
        if float(data[4])==0 or float(data[3])==0: continue 
        price=log10(price)
        i+=1

        if i >5 and i <20006:#the target is the tick ahead by 1
            traintargetfile.write(str(price))
            traintargetfile.write(',')
        if i >= 20006:
           testtargetfile.write(str(price))
           testtargetfile.write(',')
        if i >= 40006: break
