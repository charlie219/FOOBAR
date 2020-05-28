#Akash Kumar Bhagat (akay_99)


graph=[];tl=0;useless=[0];last=0;t=0;bunny=[]
def next_node(x):
    ti=[]
    for i in range(len(graph)):
        if(graph[x][i]+graph[i][x]<0):
            return i
    for i in useless:
        if(x==i):
            continue
        ti.append((graph[x][i]+graph[i][last],i))
    ti=sorted(ti)
    if(len(ti)>0 and ti[0][0]<0):
        return ti[0][1]
    if(graph[x][last]<0):
        return last
    ti=[]
    for i in range(1,last):
        if(i not in useless):
            ti.append((graph[x][i]+graph[i][last],i))
    ti=sorted(ti)
    if(len(ti)>0 and t+ti[0][0]<=tl):
        return ti[0][1]
    else:
        return last

def ActualSolution():
    global t;ans=[]
    cur=0;t=0
    nex=next_node(cur)
    print(t,tl,cur,nex,graph[cur][nex])
    while(t<=tl):
        if(cur==nex==last):
            break
        if(t<=-10000):                               #Negative Cycle
            ans=[i-1 for i in bunny]
            break
        if(nex in bunny and nex not in useless):
            useless.append(nex)
            ans.append(nex-1)
        t+=graph[cur][nex]
        cur=nex;nex=next_node(cur)
        print("*",t,cur,nex,graph[cur][nex])
    return sorted(ans)

def solution(times, times_limit):
    global graph;global tl;global last;global bunny
    last=len(times)-1
    bunny=[i for i in range(1,last)]
    graph=times;tl=times_limit
    return ActualSolution()

#----------------------------DRIVER CODE-----------------------------

x,y=map(int,input().split())
a=[[int(j) for j in input().split()] for  i in range(y+2)]
print(solution(a,x))


'''
1 1
0 1 -1
1 0 1
1 1 0

2 2
0 1 1 1
1 0 1 1
1 -2 0 1
1 1 1 0

1 3
0 2 2 2 -1
9 0 2 2 -1
9 3 0 2 -1
9 3 2 0 -1
9 3 2 2 0

3 3
0 1 1 1 1
1 0 1 1 1
1 1 0 1 1
1 1 1 0 1
1 1 1 1 0

0 3
0 1 1 1 1
1 0 1 1 1
1 1 0 1 1
1 1 1 0 1
1 1 1 1 0
'''





    
