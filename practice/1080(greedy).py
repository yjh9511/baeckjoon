import sys
sys.stdin=open("input.txt","r")

n,m=map(int,input().split())
a=[]; b=[]

result=0

def change(i,j):
    if i+2<n and j+2<m:
        for x in range(i,i+3):
            for y in range(j,j+3):
                if a[x][y]=='1':
                    a[x][y]='0'
                else:
                    a[x][y]='1'

for _ in range(n):
    a.append(list(input()))
for _ in range(n):
    b.append(list(input()))

for i in range(n):
    for j in range(m):
        if a[i][j]!=b[i][j]:
            change(i,j)
            result+=1
        if a==b:
            print(result)
            sys.exit()
print(-1)
