#Akash Kumar Bhagat (akay_99)
dic={};k=0;base=3
def conv(num):
    convStr = "0123456789"
    if num<base:
        return convStr[num]
    else:
        return conv(num//base) + convStr[num%base]
    
def new(n):
    y="".join(sorted(n));x=y[::-1]
    #print(x,y)
    a=int(x,base);b=int(y,base)
    temp=conv(a-b)
    #print(a,b,temp)
    while(len(temp)<k):
        temp='0'+temp
        
    return temp    
def solution(n, b):
    global k;global base;global dic
    dic[n]=1
    k=len(n)
    base=b;count=1
    temp=new(n);i=1
    while(temp not in dic.keys()):
        
        count+=1
        dic[temp]=i
        temp=new(temp)
        if(int(temp,base)<=1):
            return 1
        i+=1
    #print(dic)
    return i-dic[temp]

#-----------------------DRIVER CODE-----------------------------------------------

for _ in range(int(input())):
    n,b=input().split()
    print(solution(n,int(b)))

'''
2
210022 3
1211 10
'''















            
