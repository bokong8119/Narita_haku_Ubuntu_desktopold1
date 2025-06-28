import random
a=['A']
s=''
i=0
for sb in range(10000000):
    while len(a)>0 and i<=10:
        m=random.randint(0,10)
        if m%2==0:
            a.append(chr(ord(a[-1])+1))
        else:
            s=s+a.pop()
        i+=1
    print (s)
    if s=='ABC':
        print ('1')