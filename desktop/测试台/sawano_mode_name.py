from random import randint
last_name=''
last_name_A=''
first_name=''
number_change=''
number=0
A_a_test=''
A_a_number=0
sawano_dictionary={'A':['Ă','Â','Ä','Å','Ä','À'],'a':['ă','â','ä','å','ä','à','α'],'B':[]}
def sawano_change_B_D(letter,number):
    if letter in sawano_dictionary:
        sawano_choose_number=randint(0,len(sawano_dictionary[letter])-1)
        name=first_name[0:number]+sawano_dictionary[letter][sawano_choose_number]+first_name[number_change+1:]
    return name
def A_a_change(name):
    for i in name:
        A_a_choose=randint(0,1)
        if A_a_choose==0:
            if 'a'<=i<='z':
                i=chr(ord(i)-32)
                last_name_A=name[0:A_a_number]+i+name[A_a_number+1:]
            elif 'A'<=i<='Z':
                i=chr(ord(i)+32)
                last_name_A=name[0:A_a_number]+i+name[A_a_number+1:]
        A_a_number=1+A_a_number
    return last_name_A

first_name=input('test')
A_a_test=first_name[0:5]
if A_a_test=='#YES#' or A_a_test=='#yes#':
    first_name=first_name[5:]
    first_name=A_a_change(first_name)
for i in first_name:
    i=sawano_change_B_D(i,number) 
    number=number+1
    end_name=end_name+i