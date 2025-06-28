sum=0
s=''
from random import *
for sb in range(0,100):
    s=''
    for i in range(1,4):
        k=int(random()*3+1)
        c=chr(96+k)
        if i%2==k%2:
            s=s+c
        else:
            s=c+s
    if s=='bbc' and sum==0:
        print ('bbc'==s)
        sum=5
