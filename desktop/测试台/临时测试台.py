import random
for sb in range(0,2000000):
    a=[0]*6
    for i in range(6):
        x=int(random.random()*10)+1
        if i%2==1:
            a[i]=2*x+1
        elif x%2==0:
            a[i]=x//2
        else:
            a[i]=x-14
    if [3,11,4,19,2,13]==a:
        print('YES')