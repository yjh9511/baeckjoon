import sys
sys.stdin=open("input.txt","r")
from collections import deque
n=int(input())

def bfs():
    while(q):
        a=q.popleft()
        visited[a]=True

        for i in l[a]:
            if visited[i]==False:
                q.append(i)
                tmp[i]=a

l=[[] for _ in range(n+1)]
tmp=[0 for _ in range(n+1)]
visited=[False for _ in range(n+1)]

for _ in range(n-1):
    a,b=list(map(int,input().split()))
    l[a].append(b)
    l[b].append(a)

q=deque()
q.append(1)
bfs()
for i in range(2,n+1):
    print(tmp[i])
