import sys

sys.stdin=open("input.txt","r")

n=int(input())
m=list(map(int,input().split(' ')))

m_value=1
m_index=[1 for _ in range(len(m))]

for i in range(n):
    for j in range(i+1):
        if m[i]>m[j]:
            m_index[i]=max(m_index[i],m_index[j]+1)

print(max(m_index))
