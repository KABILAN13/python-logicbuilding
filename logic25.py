n=int(input())
l=[]
for i in range(0,n):
    t=int(input())
    l.append(t)
count=0
a=min(l)
for i in range(2,a+1):
    c=0
    for j in range(0,n):
        if l[j]%i==0:
            c+=1
        else:
            continue
    if(c==n):
        count+=1
print(count)
