import sys
sys.stdin=open("input.txt","r")
from collections import deque

lx=[1,-1,0,0]
ly=[0,0,1,-1]

def bfs():
    global min_v
    while(q):
        x,y=q.popleft()

        if x==m-1 and y==n-1:
            min_v=visited[x][y]
            break
        for i in range(4):
            dx=x+lx[i]
            dy=y+ly[i]

            if 0<=dx<m and 0<=dy<n and visited[dx][dy]==-1:
                if l[dx][dy]=='0':
                    q.appendleft([dx,dy])
                    visited[dx][dy]=visited[x][y]
                else:
                    q.append([dx,dy])
                    visited[dx][dy]=visited[x][y]+1



n,m=map(int,input().split())
min_v=n+m
l=[]
for _ in range(m):
    l.append(list(input()))
q=deque()
visited=[[-1]*n for _ in range(m)]

q.append([0,0])
visited[0][0]=0

bfs()
print(min_v)

