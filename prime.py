a=int(input())
flag=False
if(a==0) or (a==1):
    print("NO")
elif(a>1):
    for i in range(2,a):
        while(a%i==0):
            flag=True
            break
    if flag:
        print("NO")
    else:
        print("YES")