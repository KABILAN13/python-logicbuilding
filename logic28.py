a=int(input())
b=[]
for i in range(a):
    c=list(map(int,input().split()))
    b.append(c)
sum=b[0][0] + b[0][a-1]+b[a-1][0]+b[a-1][a-1]
print(sum)