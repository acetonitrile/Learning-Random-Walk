datafile=open('IVE_tickbidask.txt', 'r')
pPrice=0
pBid=0
pAsk=0
pVol=0
cash=10000000.0
share=0.0
i=0
error=0
log=open('IVEDownlog.txt', 'w')
for line in datafile:
    data=line.split(",")
    price=float(data[2])
    bid=float(data[3])
    ask=float(data[4])
    if ask ==0 or bid==0 or ask < bid or  bid > ask or ask/bid >1.1 or bid/ask<0.9:
        error+=1
        continue
    vol=float(data[5])
    if price <= pPrice:
        share+=cash/ask
        cash=0.0
    else:
        cash+=share*bid
        share=0.0
    pPrice=price
    pBid=bid
    pAsk=ask
    pVol=vol
    if  i%1000 == 0:
        ret=data[0]+"return=" + str((cash + share*bid)/10000000.0-1)+'\n'
        log.write(ret);
    i+=1
cash+=share*pBid
print("return=", cash/10000000-1)
print("error rate=", error/4506160.0)
print("error count=", error)
