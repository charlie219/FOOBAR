#Akash Kumar Bhagat (akay_99)

def min_henchmen(n):
    an=1;i=0;count=0
    while(count<n):
        an*=2
        count+=an
        i+=1
    return i
def max_henchmen(a,b,n,i):
    #print(a,i,n)
    if(a>n):
        return i
    return max_henchmen(b,a+b,n-a,i+1)
    
def solution(total_lambs):
    a=max_henchmen(0,1,total_lambs,-1)
    b=min_henchmen(total_lambs)
    #print(a,b)
    return a-b

#------------------------DRIVER CODE----------------------------------------------
for _ in range(int(input())):
    print(solution(int(input())))
