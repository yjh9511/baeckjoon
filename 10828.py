import sys
from collections import deque
 
sys.stdin=open("input.txt","r")

n=int(input())
test=[]
for _ in range(n):
    test.append(input())

q=deque()

for i in test:
    if 'push' in i:
        a=i.split(' ')
        q.append(int(a[-1]))
    elif i=='pop':
        if not q:
            print(-1)
        else:
            print(q.pop())
    elif i=='size':
        print(len(q))
    elif i=='empty':
        if not q:
            print(1)
        else:
            print(0)
    elif i=='top':
        if not q:
            print(-1)
        else:
            print(q[-1])
