a=input()
b=list(a.strip().split())
c=[]
for i in range(len(b)):
    if(b[i].isalpha()):
        c.append(i)
print(c)
