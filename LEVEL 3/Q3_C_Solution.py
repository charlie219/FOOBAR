#Akash Kumar Bhagat (akay_99)


graph=[];li=[]
n=0;m=0
N=[-1,1,0,0];M=[0,0,-1,1]
def bfs():
    visited=[[False for i in range(m)] for j in range(n)]
    visited[0][0]=True
    q=[([0,0],1)]
    while(len(q)!=0):
        cur=q[0]
        q.pop(0)
        x=cur[0][0];y=cur[0][1]
        #print(cur,q)
        if(x==n-1 and y==m-1):
            return cur[1]
        for i in range(0,4):
            row=x+N[i]
            col=y+M[i]
            if(0<=row<n and 0<=col<m and graph[row][col]==0 and not visited[row][col]):
                visited[row][col]=True
                q.append(([row,col],cur[1]+1))
    return -1
            
def change(prev,nex):
    graph[nex[0]][nex[1]]=0
    if(prev!=[0,0]):
        graph[prev[0]][prev[1]]=1

def ActualSolution():
    ans=bfs();cur=[0,0]
    for i in li:
        change(cur,i)
        cur=i
        temp=bfs()
        if(temp!=-1):
            ans=min(ans,temp)
    return ans
        
        
def find(grid):
    for i in range(n):
        for j in range(m):
            if(grid[i][j]==1):
                li.append([i,j])
                
def solution(grid):
    global n;global m;global graph
    graph=grid
    n=len(grid);m=len(grid[0])
    find(grid)
    return ActualSolution()


#-----------------------------------DRIVER CODE---------------------------------


for _ in range(int(input())):
    n,m=map(int,input().split())
    a=[[int(i) for i in input().split()] for j in range(n)]
    print(solution(a))

'''
2
4 4
0 1 1 0
0 0 0 1
1 1 0 0
1 1 1 0
6 6
0 0 0 0 0 0
1 1 1 1 1 0
0 0 0 0 0 0
0 1 1 1 1 1
0 1 1 1 1 1
0 0 0 0 0 0
'''

















    
