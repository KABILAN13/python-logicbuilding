a=list(input().strip())
a.sort
a=a[::-1]
b=""
for i in a:
    if i not in b:
        b+=i
print(b)
