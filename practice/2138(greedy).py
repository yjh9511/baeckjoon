import sys
sys.stdin=open("input.txt","r")

n=int(input())


a=list(input())
b=list(input())

c=a.copy()

def change(x):
    if x==0:
        for i in range(0,2):
            if a[i]=='1':
                a[i]='0'
            else:
                a[i]='1'
    elif x==n-1:
        for i in range(x-1,x+1):
            if a[i]=='1':
                a[i]='0'
            else:
                a[i]='1'
    else:
        for i in range(x-1,x+2):
            if a[i]=='1':
                a[i]='0'
            else:
                a[i]='1'

result1=0
for i in range(n-1):
    if a[i]!=b[i]:
        change(i+1)
        result1+=1
if a[n-1]!=b[n-1]:
    result1=-1

a=c.copy()
change(0)
result2=1

for j in range(n-1):
    if a[j]!=b[j]:
        change(j+1)
        result2+=1
if a[n-1]!=b[n-1]:
    result2=-1

if result1==-1 and result2==-1:
    print(-1)
elif result1==-1:
    print(result2)
elif result2==-1:
    print(result1)
else:
    print(min(result1,result2))

