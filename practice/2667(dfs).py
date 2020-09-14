import sys
from collections import deque

sys.stdin=open("input.txt","r")

n=int(input())

l=[]

lx=[1,-1,0,0]
ly=[0,0,1,-1]

visited=[[False]*n for _ in range(n)]

for _ in range(n):
    a=list(input())
    l.append(a)

def dfs(x,y):
    global count
    visited[x][y]=True
    count+=1
    for i in range(4):
        dx=x+lx[i]
        dy=y+ly[i]
        if dx>=0 and dy>=0 and dx<n and dy<n:
            if l[dx][dy]=='1' and visited[dx][dy]==False:
                dfs(dx,dy)


count=0
result=[]

for i in range(n):
    for j in range(n):
        if l[i][j]=='1'and visited[i][j]==False:
            dfs(i,j)
            result.append(count)
            count=0

result.sort()
print(len(result))
for i in result:
    print(i)




        
        

