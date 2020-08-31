import sys

sys.stdin=open("input.txt","r")

n=int(input())

tmp=[0 for _ in range(n+1)]
tmp[1]=1
tmp[2]=2

r=3

while(n>=r):
    tmp[r]=tmp[r-1]+tmp[r-2]
    r+=1
print(tmp[n]%10007)
       
        


