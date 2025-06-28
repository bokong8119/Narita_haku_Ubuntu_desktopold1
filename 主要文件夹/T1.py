#本程序补丁仅满足大部分情况下，少部分不支持，本程序已经删除部分功能，在正式版发布后，应停止使用该程序
list=[[],[],[],[],[]]
from random import randint
group1=[16,37,26,27,28,34,20,38,29,32,16,31]
group2=[8,24,2,18,46,44,10,7,5,39,22,40]
group3=[11]
group4=[1,42,6,30,14,49,12,21,33,35,41,48]
group5=[19,45,17,3,9,13,23,47,36,4,43,25]
# 输入各个区域的学号
group = [group1, group2, group3, group4, group5]

# 输入要抽查的人数
s = int(input('请输入要抽查的人数(不超过49)'))
if s > 48:
    s = 48


def finder(number):  # 找到该学生在表中的位置
    w=-1
    for i in group:
        w+=1
        for j  in i:
            if j == number:
                return w

def printer(a):  # 位置打印
    print('------------------------')
    for region in a:
        for i in range(0, len(region)):
            print(region[i],end=',')
        print('------------------------')  # 防止混淆区域

def print_all(list):
    d=[]
    for c in list:
        d+=c
        for i in range(1,len(d)):
            for j in range(0,len(d)-1):
                if d[j]>d[j+1]:
                    d[j],d[j+1]=d[j+1],d[j]
si = 0  # 类似于索引
aaa=0
flag = [False] * 49
while si < s:  # 幸运抽奖（哪个学生要被检查）
    temp_int = randint(0, 48)
    if not flag[temp_int]:  # 如果该学生没有被选中
        flag[temp_int] = True
        si += 1
        temp=temp_int+1
        ##s=finder(temp)
        s=None
        print(aaa)
        list[s].append(temp)
        aaa+=1
        print(aaa)

printer(list)
print(print_all(list))
###print("抽取出的学生学号:", student_cc)
