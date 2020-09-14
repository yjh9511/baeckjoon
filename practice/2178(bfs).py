import sys

sys.stdin=open("input.txt","r")

from collections import deque

n,m=map(int,input().split())

l=[]

lx=[1,-1,0,0]
ly=[0,0,1,-1]

q=deque()

visited=[[0]*m for _ in range(n)]

for _ in range(n):
    a=list(input())
    l.append(a)

def bfs():
    while(q):
        a=q.popleft()
        x=a[0]; y=a[1];
        if x==n-1 and y==m-1: #도착지점에 
            print(visited[x][y])
            break
        for i in range(4):
            dx=x+lx[i]
            dy=y+ly[i]
            if 0<=dx<n and 0<=dy<m:
                if visited[dx][dy]==0 and l[dx][dy]=='1':
                    visited[dx][dy]=visited[x][y]+1  #1씩더한다
                    q.append((dx,dy))

q.append((0,0))
visited[0][0]=1
bfs()
