from random import randint
s=int(input('请输入要抽查的人数'))
group1=[16,37,26,27,28,34,20,38,29,32,16,31]
group2=[8,24,2,18,46,44,10,7,5,39,22,40]
group3=[11,0]
group4=[1,42,6,30,14,49,12,21,33,35,41,48]
group5=[19,45,17,3,9,13,23,47,36,4,43,25]
group_all=[]
group_all.append(group1)
group_all.append(group2)
group_all.append(group3)
group_all.append(group4)
group_all.append(group5)
def finder(number):
    for i in range(len(group_all)):
        for j in range(len(group_all[i])):
            if group_all[i][j]==number:
                return [i,j,number]
def printer(a):
    print('------------------------')
    for i in range(len(a)):
        for j in range(0,len(a[i]),2):
            print(a[i][j],a[i][j+1])
        print('------------------------')
def dw(a):
    list=[]
    for i in range(len(group_all)):
        length=len(group_all[i])
        list_temp=[0]*length
        list.append(list_temp)
    for i in range(len(a)):
        list[a[i][0]][a[i][1]]=a[i][2]
    return list
si=0
flag=[False]*49
while si<s:
    temp_int=randint(0,48)
    if flag[temp_int]==False:
        flag[temp_int]=True
        si+=1
student_cc=[]
for i in range(len(flag)):
    if flag[i]==True:
        student_cc.append(i+1)
student_information=[]
for c in range(len(student_cc)):
    student_information.append(finder(student_cc[c]-1))
list_end=dw(student_information)
print(printer(list_end))
print(student_cc)