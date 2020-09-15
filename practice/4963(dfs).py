import sys

sys.stdin=open("input.txt","r")

def dfs(x,y):
    visited[x][y]=True

    for i in range(8):
        dx=x+lx[i]
        dy=y+ly[i]
        if 0<=dx<h and 0<=dy<w:
            if visited[dx][dy]==False and l[dx][dy]==1:
                dfs(dx,dy)

lx=[1,-1,0,0,1,1,-1,-1]
ly=[0,0,1,-1,1,-1,1,-1]



while(True):
    count=0
    w,h=map(int,input().split())
    visited=[[False]*w for _ in range(h)]
    if w==0 and h==0:
        break
    l=[]
    for _ in range(h):
        l.append(list(map(int,input().split())))
    for i in range(h):
        for j in range(w):
            if l[i][j]==1 and visited[i][j]==False:
                dfs(i,j)
                count+=1
    print(count)
