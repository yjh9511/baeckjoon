import sys
from collections import deque
sys.stdin=open("input.txt","r")

input=sys.stdin.readline

n=int(input())
l=list(input().split())

min_v=9999999999
max_v=0

result=[0,0]

def check(x,y):
    tmp=len(x)
    if l[tmp-1]=='<':
        if int(x[-1])<y:
            return True
    else:
        if int(x[-1])>y:
            return True
  
def dfs(c_lst,count):
    global min_v
    global max_v
    global result
    visited[int(c_lst[-1])]=True
    if  count==len(l)+1:
        if min_v>int(c_lst):
            min_v=int(c_lst)
            result[1]=c_lst
        if max_v<int(c_lst):
            max_v=int(c_lst)
            result[0]=c_lst
        return
    for i in range(10):
        if visited[i]==False:
            if check(c_lst,i):
                dfs(c_lst+str(i),count+1)
                visited[i]=False
for i in range(10):
    visited=[False for _ in range(10)]
    dfs(str(i),1)
    

print(result[0])
print(result[1])
