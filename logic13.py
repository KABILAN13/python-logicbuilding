a=int(input())
b=int(input())
c=int(input())
for i in range(a,b+1):
    if i%c != 0:
        print(i,end=" ")