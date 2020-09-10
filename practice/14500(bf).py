import sys

sys.stdin=open("input.txt","r")

n,m=map(int,input().split(' '))
l=[]
for _ in range(n):
    l.append(list(map(int,input().split(' '))))


dx=[-1,1,0,0]
dy=[0,0,1,-1]
def dfs(x,y,visited,sumv,count):
    global maxv
    if count==4:
        maxv=max(maxv,sumv)
        return

    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]

        if nx>=0 and ny>=0 and nx<n and ny<m:
            if visited[nx][ny]==False:
                visited[nx][ny]=True
                dfs(nx,ny,visited,sumv+l[nx][ny],count+1)
                visited[nx][ny]=False

def fuck(x,y):
    global maxv

    if (x==0 and y==0) or (x==0 and y==m-1) or (x==n-1 and y==0) or (x==n-1 and y==m-1):
        return
    elif x==0:
        maxv=max(maxv,l[x][y]+l[x][y-1]+l[x][y+1]+l[x+1][y])
    elif x==n-1:
        maxv=max(maxv,l[x][y]+l[x][y-1]+l[x][y+1]+l[x-1][y])
    elif y==0:
        maxv=max(maxv,l[x][y]+l[x-1][y]+l[x+1][y]+l[x][y+1])
    elif y==m-1:
        maxv=max(maxv,l[x][y]+l[x-1][y]+l[x+1][y]+l[x][y-1])
    else:
        sumlist=[]
        sumlist.append(l[x][y]+l[x-1][y]+l[x][y-1]+l[x][y+1])
        sumlist.append(l[x][y]+l[x+1][y]+l[x][y-1]+l[x][y+1])
        sumlist.append(l[x][y]+l[x-1][y]+l[x+1][y]+l[x][y+1])
        sumlist.append(l[x][y]+l[x-1][y]+l[x+1][y]+l[x][y-1])
        maxv=max(maxv,max(sumlist))
    return

maxv=0
visited=[[False]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        fuck(i,j)
        
        visited[i][j]=True
        dfs(i,j,visited,l[i][j],1)
        visited[i][j]=False

print(maxv)






        
        

