import sys

sys.stdin=open("input.txt","r")

n=int(input())
m=list(map(int,input().split(' ')))

m_value=m[0]
result=0

for j in range(len(m)):
    if result+m[j]<0:
        m_value=max(m_value,m[j])
        result=0
        continue
    result=result+m[j]
    m_value=max(m_value,result)
print(m_value)
