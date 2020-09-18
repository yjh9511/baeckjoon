import sys
sys.stdin=open("input.txt","r")
from collections import deque

n=int(input())

def first(a):
    print(a,end='')
    if l[tmp.index(a)][1]!='.':
        first(l[tmp.index(a)][1])
    if l[tmp.index(a)][2]!='.':
        first(l[tmp.index(a)][2])

def second(a):
    
    if l[tmp.index(a)][1]!='.':
        second(l[tmp.index(a)][1])
    print(a,end='')
    if l[tmp.index(a)][2]!='.':
        second(l[tmp.index(a)][2])

def third(a):
    
    if l[tmp.index(a)][1]!='.':
        third(l[tmp.index(a)][1])
    if l[tmp.index(a)][2]!='.':
        third(l[tmp.index(a)][2])
    print(a,end='')



l=[]
tmp=[]
for i in range(n):
    l.append(list(input().split()))
    tmp.append(l[i][0])
    l[i][0]=i
first('A')
print()
second('A')
print()
third('A')
