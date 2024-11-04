a=[int(b) for b in input().split()]
x=int(input())
y=int(input())
net=0
for A in a:
    if(A%2==0):
        net+=x
    else:
        net-=y
print(net)