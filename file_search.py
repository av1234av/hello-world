import re
import pandas as pd
p = re.compile('APPSRVReport|EQRFReport')
pp = re.compile('[0-9]\.[0-9]')
with open('C:\\Temp\\Sample.txt') as f:
    ll=[]
    for line in f:
        if p.match(line):
            l=line.split()
            mem=pp.search(l[4]).group()
            ll.append([l[0],l[2],l[3],mem])
    df=pd.DataFrame(ll,columns=['Report','PID','Request','Mem'],dtype=float)


print df