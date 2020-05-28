#Akash Kumar Bhagat (akay_99)
boo=True
def cal(x,y):
    global boo
    ans=0;i=0
    while(1):
        if(y<=0 or x<=0):
            boo=False
            break
        if(y==1):
            ans+=x-1
            break
        ans+=(x//y)
        x,y=y,x%y
        i+=1
    #print(i)
    return ans

def solution(x, y):
    global boo
    boo=True
    ans=cal(int(x),int(y))
    if(boo):  ans=str(ans)
    else:   ans="impossible"
    return ans

#-----------------------------DRIVER CODE------------------------------------------


for i in range(int(input())):
    a,b=input().split()
    print(solution(a,b))





'''
#To study the generation tree

n=7
li=[[1,1]];i=0
while(i<20):
    i+=1
    temp=[]
    while(len(li)>0):
        x=li[0];li.pop(0)
        if(min(x[1],x[0])==n):
            print(x,end=" ")
        temp.append([x[0],x[0]+x[1]])
        temp.append([x[0]+x[1],x[1]])
    li=temp
    print()
    print(i,end='--->')

'''
