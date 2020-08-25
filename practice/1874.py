from collections import deque

n=int(input())
q=deque()
test=[]
result=[]
tmp=1
check=False

for _ in range(n):
    test.append(int(input()))

for i in test:
    if check==True:
        break
    if not q:
        q.append(tmp)
        result.append('+')
        tmp=tmp+1
    while(q):
        if q[-1]>n:
            print('NO')
            check=True
            break
        if q[-1]==i:
            q.pop()
            result.append('-')
            break
        q.append(tmp)
        result.append('+')
        tmp=tmp+1
if check==False:
    for j in result:
        print(j)
