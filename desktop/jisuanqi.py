'''print("Welcome to the calculator, 'The Honest Student'.")
print("This calculator can calculate the four operations of addition, subtraction, multiplication and division (not squares, which do not have this function).")
print('Also, we have configured the correct detection.')
print("We will add the calculation of quadratic equations later, so stay tuned.")'''
'''def size(s):
    number_temp1=[] #数字定位（符号前）
    number_temp2=[] #数字定位（符号后）
    yx2=[] #加减符号定位
    yx1=[] #乘除符号定位
    dingwei_temp=[]
    dingwei={} #总
    setup=0
    for i in range (len(s)):
        if 0<=s[i]<=9 and setup==0:
            number_temp1.append(i)
        elif s[i] in ['*','/']:
            yx1.append(i)
            setup+=1
        elif s[i] in ['+','-']:
            yx2.append(i)
            setup+=1
        elif 0<=s[i]<=9 and setup==1:
            number_temp2.append(i)
        if setup==2:
            setup=0
            dingwei_temp.append(number_temp1)
            dingwei_temp.append(number_temp2)
            if yx1!=[]:
                dingwei[yx1]=dingwei_temp'''
def jiajian(s):
    for i in range(len(s)):
        
