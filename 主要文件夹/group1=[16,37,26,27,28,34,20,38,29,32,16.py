group1=[16,37,26,27,28,34,20,38,29,32,16,31]
group2=[8,24,2,18,46,44,10,7,5,39,22,40]
group3=[11]
group4=[1,42,6,30,14,49,12,21,33,35,41,48]
group5=[19,45,17,3,9,13,23,47,36,4,43,25]
# 输入各个区域的学号
group = group1+group2+group3+group4+group5
print(group)
sum=0
for i in group:
    flag=False
    for a in range(1,50):
        if a==i:
            print('a')
            flag=True
            sum+=1
            break
    if flag==False:
        print(a)
print(sum)