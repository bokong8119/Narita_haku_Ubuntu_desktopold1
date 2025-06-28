import pandas as pd
dic={
    'SB':[1,20,3,4],
    '2B':[1,2,56,4]
}
S1=pd.DataFrame(dic,index=['SB1','SB2','SB3','SB4'], columns=['2B','SB'])
print (S1)
for i in S1.values:
    print (i)
s2=S1.T
print (s2)
s5=pd.Series([1,2,3,4])
print (s5.tail(2))
s5[114514]=4
print (s5)
s5[0]=456545646547886
print (s5)
print(S1[S1['SB']>2])
print(S1[S1.SB>2])
print(S1[(S1.SB>2)&(S1.SB==3)])