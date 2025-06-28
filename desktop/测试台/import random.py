import random
for sb in range(0,50000):
    n=6;a=[0]*n;i=0
    while i<n:
        k=random.randint(1,10)
        if k%5==0:
            i-=1
        elif k%3==0:
            a[n-1]=k
            n=n-1;i+=1
        else:
            a[i]=k
        i=i+1
    if a==[8,0,0,8,1,9]:
        print ('yes')
    