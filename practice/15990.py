import sys

sys.stdin=open("input.txt","r")

n=int(input())

test=[[0]*3 for _ in range(100000)]
test[0][0]=1; test[1][1]=1; test[2][1]=1; test[2][0]=1; test[2][2]=1

m=4
while(m<=100000):
    test[m-1][0]=(test[m-2][1]+test[m-2][2])%1000000009; test[m-1][1]=(test[m-3][0]+test[m-3][2])%1000000009; test[m-1][2]=(test[m-4][0]+test[m-4][1])%1000000009
    m+=1


#(a+b)mod m= ((a mod m) +(b mod m) ) mod m
for _ in range(n):
    tmp=int(input())
    print(sum(test[tmp-1])%1000000009)
