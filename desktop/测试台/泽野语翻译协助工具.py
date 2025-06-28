from random import randint
from random import random
sawano_dictionary={'A':['Ă','Â','Ä','Å','Ä','À','A'],'a':['ă','â','ä','å','ä','à','α','a']}
i=0 #记录位置
st=0
wn=['furry'] #敏感词，采用人工翻译，同一词大小写不同
end=''
def sawano_mode(translate):
    i=0
    end=''
    while i<len(translate):
        if translate[i:i+len(wn[1])] in wn:
            end=end+'###WARNING###'+translate[i+i+len(wn[1])]+'####'
        else:
            if translate[i] in sawano_dictionary:
                ch=randint(0,len(sawano_dictionary[translate[i]])-1)
                end=end+sawano_dictionary[translate[i]][ch]
            i=i+1
    return end
def A_a_mode(translate):
    i=0
    end=''
    while i<len(translate):
        if translate[i:i+len(wn[i])] in wn:
            end=end+translate[i:i+len(wn[1])]
            i=i+len(wn[1])
        else:
            if 'A'<translate[i]<'Z':
                ch=random(1,2)
                if round(ch)==1:
                    continue
                else:
                    end=end+chr(32+ord(translate[i]))
            elif 'a'<translate[i]<'z':
                ch=random(1,2)
                if round(ch)==1:
                    continue
                else:
                    end=end+chr(ord(translate[i])-32)
            else:
                continue
    return end
t=input('请输入原文翻译')
t=A_a_mode(t)
t=sawano_mode(t)
print (t)