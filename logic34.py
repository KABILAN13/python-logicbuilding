string=input()
c=0
l=list(string.strip().split())
for i in range(len(l)):
    x,y=l[i].split(":")
    h,m=int(x),int(y)
    if((h==10 and m>0)or h>10):
            c+=1
print(c)