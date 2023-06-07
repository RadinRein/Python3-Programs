def comphcf(x,y):
    while(y):
        x,y=y,x%y
    return x

a,b=map(int,input("Enter two numbers :").split())
print("HCF : "+str(comphcf(a,b))+" and LCM : "+str(a*b/comphcf(a,b)))
