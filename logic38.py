'''a=input()
d=[]
for i in range(a):
    c=input()
    b=c.split()
    d.append(b)
print(d)'''

num=int(input())
li=[]
for ele in range(num):
    name,maths,physics,chemistry=map(str,input().split(":"))
    total=int(maths)+int(physics)+int(chemistry)
    li.append([total,int(maths),int(physics),int(chemistry),name])
li.sort(reverse=True)
print(li[0][-1])