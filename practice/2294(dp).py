import sys

sys.stdin=open("input.txt","r")

input=sys.stdin.readline

n,m=map(int,input().split())


dp=[10001 for _ in range(10001)]

l=sorted([int(input()) for _ in range(n)])

dp[0]=0

for i in l:
    for j in range(i,m+1):
        dp[j]=min(dp[j],dp[j-i]+1)

if dp[m]==10001:
    print(-1)
else:
    print(dp[m])
