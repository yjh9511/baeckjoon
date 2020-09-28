import sys

sys.stdin=open("input.txt","r")

input=sys.stdin.readline

n=int(input())

dp=[0 for _ in range(101)]
dp[1]=1; dp[2]=2; dp[3]=3; dp[4]=4; dp[5]=5

for i in range(6,n+1):
    for j in range(i-3,0,-1):
        dp[i]=max(dp[i],dp[j]*(i-j-1))
print(dp[n])
