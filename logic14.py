a=int(input())
b=int(input())
i=a
j=b
while(b>=i) and (a<=j):
    if(i%2!=0):
        print(i,end=" ")
    i+=1
    if(j%2==0):
        print(j,end=" ")
    j-=1