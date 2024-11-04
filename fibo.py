'''a=int(input())
b=0
c=[]
for i in range(a+1):
    b+=i
    c.append()
print(b,end=" ")'''

n = int(input())
num1 = 0
num2 = 1
count=0
if(n==0):
    print("enter fibo number")
else:
    while(count<n):
        print(num1,end=" ")
        nextnum=num1+num2
        num1=num2
        num2=nextnum
        count+=1