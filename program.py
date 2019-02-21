def  int_num(x):
    a=abs(x)
    r=round(x)
    if (a-r)==0:
        print("true")
    else:
        print("false")
p=int(input("num"))
int_num(p)
