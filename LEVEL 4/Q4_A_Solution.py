#Akash Kumar Bhagat (akay_99)

graph={};n=0;ent={};exi={}
temp=[];visited=[]
ans2=0
def dfs(cur,nex,w):
    #print(cur,nex,visited)
    visited[cur][nex]=True
    if(w==0):
        return w
    if(nex in exi.keys()):
        return w
    wig=[]
    for i in graph[nex].keys():
        wig.append((graph[nex][i],i))
    wig=sorted(wig)[::-1]
    for i in wig:
        if(visited[nex][i[1]]):
            continue
        x=dfs(nex,i[1],min(i[0],w))
        #print(x,nex,i[1])
        if(x):
            graph[nex][i[1]]-=x
            return x
        break
    return 0
    
def cal(cur,nex,w):
    global visited
    ans2=0
    visited=[[False for  i in range(n)] for j in range(n)]
    x=dfs(cur,nex,w);
    #print(visited)
    while(x!=0):
        #print(x,graph)
        ans2+=x
        w-=x
        x=dfs(cur,nex,w)
    return ans2
def make_graph(path,en,ex):
    for i in range(n):
        graph[i]={}
        for j in range(n):
            if path[i][j]>0:
                graph[i][j]=path[i][j]
    for i in en:
        ent[i]=1
    for i in ex:
        exi[i]=1
        
def ActualSolution():
    global temp
    global ans2;global weight;global ne;global cu
    for i in ent:
        for j in graph[i]:
            temp.append((graph[i][j],i,j))
    temp=sorted(temp,reverse=True)
    ans=0
    #print(temp)
    for i in temp:
        del graph[i[1]][i[2]]
        x=cal(i[1],i[2],i[0])
        ans+=x
        #print(x,graph)
    return ans
def solution(entrances, exits, path):
    global n
    n=len(path)
    make_graph(path,entrances, exits)
    return ActualSolution()

#-----------------------------------------DRIVER CODE----------------------------------------
ex=[];en=[]
for i in input().split():
    en.append(int(i))
for i in input().split():
    ex.append(int(i))
node=int(input())
a=[[int(i) for i in input().split()] for j in range(node)]
print(solution(en,ex,a))

'''
0
5
6
0 1 1 0 0 0
0 0 0 1 1 0
0 0 0 1 1 0
0 0 0 0 0 2
0 1 1 0 0 0
0 0 0 0 0 0
0 1
4 5
6
0 0 4 4 0 0
0 0 0 12 0 0
0 0 0 0 4 4
0 0 0 0 8 8
0 0 0 0 0 0
0 0 0 0 0 0
0 1
4 5
6
0 0 4 6 0 0
0 0 5 2 0 0
0 0 0 0 4 4
0 0 0 0 6 6
0 0 0 0 0 0
0 0 0 0 0 0
0
3
4
0 7 0 0
0 0 6 0
0 0 0 8
9 0 0 0
'''

    
