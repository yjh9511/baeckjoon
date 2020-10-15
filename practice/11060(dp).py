import sys
from collections import deque
import itertools

sys.stdin=open("input.txt","r")

input=sys.stdin.readline

n=int(input())

l=list(map(int,input().split()))

dp=[1001 for _ in range(len(l)+1)]
dp[0]=0
for i in range(1,n):
    for j in range(i):
        if j+l[j]>=i:
            dp[i]=min(dp[i],dp[j]+1)

if dp[n-1]==1001:
    print(-1)
else:
    print(dp[n-1])

