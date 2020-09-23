import sys
import heapq
sys.stdin=open("input.txt","r")

n=int(input())
l=list(map(int,input().split()))

m=int(input())
k=list(map(int,input().split()))

result=[]
l.sort()


def check(x):
    start=0
    end=len(l)-1
    while end>=start:
        tmp=(end+start)//2
        if l[tmp]==x:
            return 1
        elif l[tmp]>x:
            end=tmp-1
        else:
            start=tmp+1
    return 0
for i in k:
    result.append(check(i))

for j in result:
    print(j,end=' ')
