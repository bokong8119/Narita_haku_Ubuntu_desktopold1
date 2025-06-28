#number=[2]
#number_sum=0
#i=int(input('请输入你想要的数'))
#for a in range(i-1):
#    for b in range(len(number)):
#        number_sum+=number[b]
#    sum=number_sum+number[a]+(a+1)/2
#    c=sum-number_sum
#    number.append(c)
#print (number[a+1])
a=[2]
b=[1]
for i in range(1000):
    aa=a[i]+1
    a.append(aa)
for i in range(1000):
    bb=b[i]*2
    b.append(bb)
#print(a)
#print('------------------------------------------------------------------------------------------------------------------------')
#print(b)
sum=0
for c in range(10):
    d=b[c]
    sum+=a[d]
print(sum)