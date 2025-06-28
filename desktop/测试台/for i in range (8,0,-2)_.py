
def sawano_tidy(x):
    number=0
    for i in x:
        if i>='a' or i<='z':
            number+=1
        elif i>='A' or i<='Z':
            number+=1
        elif i>=0 or i<=1:
            number+=1
        else:
            x=x[:number]+i+x[number+1:]
    return x
shuru=''
end=''
while True:
    shuru=input()
    if shuru=='exit' or shuru=='EXIT':
        break
    else:
         end=sawano_tidy(shuru)+end
print(end)
