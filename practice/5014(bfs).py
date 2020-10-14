import sys
from collections import deque
sys.stdin=open("input.txt","r")

input=sys.stdin.readline

n,m=map(int,input().split())
l=[]
for _ in range(n):
    l.append(list(input()))

visited=[[0]*m for _ in range(n)]

dx=[1,-1,0,0]
dy=[0,0,1,-1]

def bfs():
    w=0
    s=0
    while(q):
        x,y=q.popleft()
        if l[x][y]=='v':
            w+=1
        elif l[x][y]=='o':
            s+=1
        
        for i in range(4):
            lx=dx[i]+x
            ly=dy[i]+y

            if 0<=lx<n and 0<=ly<m and visited[lx][ly]==0:
                if l[lx][ly]!='#':
                    visited[lx][ly]=1
                    q.append([lx,ly])
    if s>w:
        return s,0
    else:
        return 0,w
q=deque()
s_v=0
w_v=0
for i in range(1,n-1):
    for j in range(1,m-1):
        if l[i][j]!='#' and visited[i][j]==0:
            q.append([i,j])
            visited[i][j]=1
            tmp,tmp2=bfs()
            s_v+=tmp
            w_v+=tmp2
print(s_v,w_v)
