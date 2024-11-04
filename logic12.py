a= int(input())
num=0
while(a>0):
    rev=a%10
    if (rev%2==1):
        num=num+rev
    a=int(a/10)
print(num)