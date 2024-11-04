a=int(input())
b=int(input())
count=0
for i in range(a,b+1):
    flag=0
    for j in range(2,i):
        if(i%j==0):
            flag=1
            break
    if(flag==0 and not(i==1)):
            count+=1
print(count)