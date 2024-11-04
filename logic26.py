a=input()
b=list(map(int,a.split()))
f=int(input())
d=b[1]-b[0]
c=[b[0]]
e=b[0]
for i in range(10):
    e=e+d
    c.append(e)


k=f-1
g=c[k]
print(g)

'''string=input()
x,y,z=string.split(" ")
n=int(input())
x,y,z=int(x),int(y),int(z)
print(x+(n-1)*abs(y-z))'''
