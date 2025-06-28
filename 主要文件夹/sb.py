n='15867239012'
s=0
for x in n:
    if int(x)%2==0:
        continue
    elif s==14:
        break
    s+=int(x)
print(s)
