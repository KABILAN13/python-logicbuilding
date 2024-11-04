num=list(map(int,input().split()))
sum=0
for i in num:
    sum+=i
average=sum/len(num)
print(average)