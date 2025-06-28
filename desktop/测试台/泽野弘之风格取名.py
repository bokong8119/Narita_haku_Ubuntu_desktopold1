from random import randint
global c_l
global change_number
change_number=0
c_l=''
def sawano_B_D(name):
    global c_l
    global change_number
    n1t=0
    for i in name:
        if i=='A':
            n1t=randint(0,6)
            if n1t==0:
                continue
            elif n1t==1:
                c_l='Ă'
                name=name[:change_number]+c_l+name[change_number+1:]
            elif n1t==2:
                c_l='Â'
                name=name[:change_number]+c_l+name[change_number+1:]
            elif n1t==3:
                c_l='Ä'
                name=name[:change_number]+c_l+name[change_number+1:]
            elif n1t==4:
                c_l='Å'
                name=name[:change_number]+c_l+name[change_number+1:]  
            elif n1t==5:
                c_l='À'
                name=name[:change_number]+c_l+name[change_number+1:]
            elif n1t==6:
                c_l='Ä'
                name=name[:change_number]+c_l+name[change_number+1:]
        elif i=='a':
            n1t=randint(0,7)
            if n1t==0:
                continue
            elif n1t==1:
                c_l='ă'
                name=name[:change_number]+c_l+name[change_number+1:]
            elif n1t==2:
                c_l='â'
                name=name[:change_number]+c_l+name[change_number+1:]
            elif n1t==3:
                c_l='ä'
                name=name[:change_number]+c_l+name[change_number+1:]
            elif n1t==4:
                c_l='å'
                name=name[:change_number]+c_l+name[change_number+1:]
            elif n1t==5:
                c_l='ä'
                name=name[:change_number]+c_l+name[change_number+1:]
            elif n1t==6:
                c_l='à'
                name=name[:change_number]+c_l+name[change_number+1:]
            elif n1t==7:
                c_l='α'
                name=name[:change_number]+c_l+name[change_number+1:]
        elif i=='B':
            n1t=randint(0,2)
            if n1t==0:
                continue
            elif n1t==1:
                c_l='β'
                name=name[:change_number]+c_l+name[change_number+1:]
        elif i=='E':
            n1t=randint(0,2)
            if n1t==0:
                continue
            elif n1t==1:
                c_l='È'
                name=name[:change_number]+c_l+name[change_number+1:]
            elif n1t==2:
                c_l='∃'
                name=name[:change_number]+c_l+name[change_number+1:]
        change_number=change_number+1
    return (name)
name=input('sawono mode')
x=sawano_B_D(name)
print (x)