#若该同学没有被查到，请将该框留空
#没写的也可以留空
#请在excel第一行加入00学号，以统计作业量
import pandas as pd
df=pd.read_excel('作业统计.xlsx')
number_total=len(df.index)-1
print (df)
def h_count(df):
    df1=df.iloc[0]
    print(df1)
    temp=df1.count()
    return temp
homework_total=h_count(df)
def js_cczs(df, number_total, homework_total):
    check_total = [0]
    for i in range(1, number_total+1):
        temp_int = 0
        for j in range(1, homework_total+1):
            temp_int += df.at[i, '作业'+str(j)]  # 修改这里的at方法的参数格式
        check_total.append(temp_int)
    return check_total
def js_nhck(df):  #成田波空抽查情况
    temp=[0]
    for i in range(1,number_total+1):
        temp_int=0
        for j in range(1,homework_total+1):
            temp_int+=df.at[i]['NH查'+str(j)]
        temp.append(temp_int)
    return temp
def js_last(df):  #最终完成情况
    temp=[0]
    for i in range(1,number_total+1):
        temp_int=0
        for j in range(1,homework_total+1):
            temp_int+=df.at[i]['完成'+str(j)]
        temp.append(temp_int)
    return temp
def bfb_cc(df): #抽查百分比
    temp=[0]
    for i in range(1,number_total+1):
        if df.at[i]['抽查总数']!=0:
            temp_int=float(((df.at[i]['抽查总数']/homework_total)*100),4)
            temp.append(temp_int)
        else:
            temp.append(0.0)
    return temp
def bfb_nc(df): #成田波空抽查百分比
    temp=[0]
    for i in range(1,number_total+1):
        if df.at[i]['NH检查']!=0:
            temp_int=float(((df.at[i]['NH检查']/df.at[i]['抽查总数'])*100),4)
            temp.append(temp_int)
        else:
            temp.append(0.0)
    return temp
def bfb_end(df): #完成百分比
    temp=[0]
    for i in range(1,number_total+1):
        if df.at[i]['最终完成数']!=0:
            temp_int=float(((df.at[i]['最终完成数']/df.at[i]['抽查总数'])*100),4)
            temp.append(temp_int)
        else:
            temp.append(0.0)
    return temp
def del_N(df): #空列表删除
    list=['作业','NH查','完成']
    for i in range (homework_total+1,7+1):
        for j in list:
            j=j+str(i)
            df=df.drop(j,axis=1)
    return df
df = df.fillna(0)
df=del_N(df)
print(js_cczs(df)) #!!!!!!!!!!!!!!!!!!!!!!!!!!!!
df["抽查总数"]=check_total
NH_check=js_nhck(df,number_total, homework_total)
df['NH检查']=NH_check
check_end=js_last(df)
df['最终完成数']=check_end
bfb_check_total=bfb_cc(df)
df['抽查百分比']=bfb_check_total
bfb_nc_number=bfb_nc(df)
df['NH查率']=bfb_nc_number
bfb_end_number=bfb_end(df)
df['完成率']=bfb_end_number
print (df)