import pandas as pd
df=pd.read_excel('3U3510.xlsx')
df=df.drop('Time',axis=1)
for i in range(len(df)):
    aa=str(df.at[i,'UTC TIME'])
    print (aa[11:19])
    df.at[i,'UTC TIME']=aa
print (df)