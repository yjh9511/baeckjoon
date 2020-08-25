import sys
from collections import deque
 
sys.stdin=open("input.txt","r")

n=int(input())
test=[]
for _ in range(n):
    a=list(input().split(' '))
    for i in a:
        b=list(i)
        for j in range(len(b)-1,-1,-1):
            print(b[j],end='')
        print(' ',end='')
    print()
