#Akash Kumar Bhagat (akay_99)

#I used bellow article as refference, so you must
#https://math.stackexchange.com/questions/2052179/how-to-find-sum-i-1n-left-lfloor-i-sqrt2-right-rfloor-a001951-a-beatty-s



#Recursive Approch
#S(n)=x*n+[n*(n+1)/2]-[x*(x+1)//2]-S(x)
#Here x=floor((sqrt(2)-1)*n)

from math import sqrt
root2m1=4142135623730950488016887242096980785696718753769480731766797379907324784621070388503875343276415727
#print(len(root2))
def cal(n):
    if(n==1):
        return 1
    if(n==0):
        return 0
    x=(root2m1*n)//(10**(100))
    return int(x*n+n*(n+1)/2-x*(x+1)/2-cal(x))
    
def solution(s):
    n=int(s)
    ans=cal(n)
    return str(ans)

#--------------------------------DRIVER CODE--------------------------------------------------------
for i in range(int(input())):
    print(solution(int(input())))
