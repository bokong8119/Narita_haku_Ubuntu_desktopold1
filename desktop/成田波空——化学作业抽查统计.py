week=int(input('请输入周'))-13
import pandas as pd
df=pd.read_excel('统计.xlsx',sheet_name=week)
renshu=len(df.index)
zuoyeliang=(len(df.columns)-1)//3
def chugao(df):
    temp=[]
    for i in range(renshu):
        for s in range(1,zuoyeliang+1):
            temp_txt='作业'+str(s)
            temp_number=0
            temp_number+=df.at[i,temp_txt]
        temp.append(int(temp_number))
    print(df)
    df['抽查总计']=temp
    print(df)
    df1=df[df['抽查统计']!=0] #有被抽查到的
    df2=df[df['抽查统计']==0] #未被抽查到的
    return df1,df2
df1,df2=chugao(df)
print (df1)
print (df2)