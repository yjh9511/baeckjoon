import sys
from collections import deque
sys.stdin=open("input.txt","r")

input=sys.stdin.readline

f,s,g,u,d=map(int,input().split())

visited=[0 for _ in range(f+1)]
q=deque()

lx=[u,-d]
def bfs():
    while(q):
        a,count=q.popleft()
        if a==g:
            print(count)
            exit(0)
        for i in range(2):
            x=lx[i]+a
            if 0<x<=f and visited[x]==0:
                visited[x]=1
                q.append([x,count+1])


q.append([s,0])
visited[s]=1
bfs()
print('use the stairs')



