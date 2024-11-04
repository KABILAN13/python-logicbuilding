a=int(input())
count=0
c=[]
for i in range(a):
    b=list(input().split(','))
    c.append(b)
d= max(c,key=lambda x: int(c[1]))

print(d[0])