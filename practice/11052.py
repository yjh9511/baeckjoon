import sys

sys.stdin=open("input.txt","r")

n=int(input())

m=[0]+list(map(int,input().split()))

d=[0 for _ in range(len(m)+1)]


for i in range(1,len(m)):
    for j in range(1,i+1):
        d[i]=max(d[i],m[j]+d[i-j])
        #print(i,d[i])

print(d[len(m)-1])
