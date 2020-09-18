import sys
sys.stdin=open("input.txt","r")
from collections import deque

def bfs():
    while(q):
        a,b=q.popleft()
        
        if a==m:
            print(b)
            break
        #세가지 경우 추가
        if 2*a<=100000 and visited[a*2]==False:
            q.appendleft([2*a,b])
            visited[2*a]=True
        if a+1<=100000 and visited[a+1]==False:
            visited[1+a]=True
            q.append([a+1,b+1])
        if a-1>=0 and visited[a-1]==False:
            visited[a-1]=True
            q.append([a-1,b+1])
        
            

n,m=map(int,input().split())

visited=[False for _ in range(100001)]
q=deque()
q.append([n,0]) #초기 위치와 횟수저장
visited[n]=True
if n>=m:
    print(n-m)
else:
    bfs()
