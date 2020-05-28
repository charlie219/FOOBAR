import itertools
rows=0
def convert_to_path(x):
    x = [0] + list(x) + [-1]
    path = []
    for i in range(1, len(x)):
        path.append((x[i - 1],x[i]))
    return path

def BellmanFord(time):
    
    for k in range(rows):
        for i in range(rows):
            for j in range(rows):
                if time[i][j] > time[i][k] + time[k][j]:
                    time[i][j] = time[i][k] + time[k][j]
                    
    return time

def solution(time, time_limit):
    global rows
    rows = len(time)
    bunnies = rows - 2
    
    time=BellmanFord(time)
    for r in range(rows):                       #Negative Cycle
        if time[r][r] < 0:
            return [i for i in range(bunnies)]
    
    for i in reversed(range(bunnies + 1)):
        for perm in itertools.permutations(range(1, bunnies + 1), i):
            total_time = 0
            path = convert_to_path(perm)
            for start, end in path:
                total_time += time[start][end]
            if total_time <= time_limit:
                return sorted(list(i - 1 for i in perm))
    return None
#----------------------------DRIVER CODE-----------------------------

x,y=map(int,input().split())
a=[[int(j) for j in input().split()] for  i in range(y+2)]
print(solution(a,x))
