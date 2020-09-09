import sys
import math

sys.stdin=open("input.txt","r")

n=int(input())
m=[]
for _ in range(n):
    m.append(list(input()))



def numOfBlock(ipt_lst):
    l=len(m)
    max_l=1
    tmp=1
    for i in range(l):
        for j in range(1,l):
            if ipt_lst[i][j-1]==ipt_lst[i][j]:
                tmp+=1
            else:
                max_l=max(tmp,max_l)
                tmp=1
        max_l=max(tmp,max_l)
        tmp=1
    for i in range(l):
        for j in range(1,l):
            if ipt_lst[j-1][i]==ipt_lst[j][i]:
                tmp+=1
            else:
                max_l=max(tmp,max_l)
                tmp=1
        max_l=max(tmp,max_l)
        tmp=1
    return max_l

result=1
for i in range(n):
    for j in range(1,n):
        #양옆 스왑
        tmp=m[i][j-1]; m[i][j-1]=m[i][j]; m[i][j]=tmp;
        result=max(numOfBlock(m),result)
        tmp=m[i][j-1]; m[i][j-1]=m[i][j]; m[i][j]=tmp;
        #위아래 스왑
        tmp=m[j-1][i]; m[j-1][i]=m[j][i]; m[j][i]=tmp;
        result=max(numOfBlock(m),result)
        tmp=m[j-1][i]; m[j-1][i]=m[j][i]; m[j][i]=tmp;

print(result)

        
        

