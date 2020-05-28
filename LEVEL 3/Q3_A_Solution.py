#Akash Kumar Bhagat (akay_99)


def solution(l):
    li={};a={}
    for i in range(len(l)):
        temp=[]
        if(l[i]==0):
            li[i]=[]
            continue
        for j in range(i+1,len(l)):
            if(l[j]%l[i]==0):
                temp.append(j)
        li[i]=temp
        a[i]=len(temp)
    print(li)
    ans=0
    for i in range(len(l)):
        for j in li[i]:
            ans+=a[j]
            
    return ans
#------------------------------DRIVER CODE------------------------------------------

for _ in range(int(input())):
    print(solution([int(i) for i in input().split()]))


'''
7
1 3 2 4 6 2 4
3 6 2 6
1 3 4 2 6 2
1 2 3 4 5 6
1 1 1 1
2 2 4 2 6 4 3
'''
