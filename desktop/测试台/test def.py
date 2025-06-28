import math
def jsu(x):
    if x>1:
        y=math.pow(x,2)
    else:
        y=math.pow(2,x)
    return y
x=float(input())
print (jsu(x))