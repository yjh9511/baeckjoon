import sys
from collections import deque
sys.stdin=open("input.txt","r")

input=sys.stdin.readline

while(True):
    n=int(input())
    if n==0:
        break
    else:
        dp=[[0]*(n+2) for _ in range(n+2)]
        dp[1][0]=1
        for i in range(1,n+1):
            for j in range(n+1):
                if i==n+1 and j==n+1:
                    break
                if i>j:
                    dp[i+1][j]+=dp[i][j]
                    dp[i][j+1]+=dp[i][j]
                elif i==j:
                    dp[i+1][j]+=dp[i][j]
                else:
                    break
        print(dp[n][n])

