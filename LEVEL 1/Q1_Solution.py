#Akash Kumar Bhagat (akay_99)


pri={};prime=[]
str_prime=""
def Sieve():
    n=300000
    prim=[True for i in range(n + 1)] 
    p=2
    while(p*p<=n): 
        if(prim[p] == True): 
            for i in range(p * 2, n + 1, p): 
                prim[i] = False
        p += 1
    prim[0]= False
    prim[1]= False
    for p in range(n + 1): 
        if prim[p]: 
            pri[p]=1
            prime.append(p)
def concat():
    global prime
    global str_prime
    for i in prime:
        str_prime+=str(i)
        if(len(str_prime)>=10000):
            print("*",i)
            break
def solution(i):
    Sieve()
    concat()
    return str_prime[i:i+5]

#-------------------DRIVER CODE-----------------------------------------------------------------
for _ in range(int(input())):
    print(solution(int(input())))
