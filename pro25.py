def le(li,n) : 
    m=1 
    l=1 
    for i in range(1,n) :
        if (li[i]>li[i-1]) : 
            l=l+1 
        else : 
            if (m<l)  : 
                m=l     
            l=1
    if (m<l) : 
        m=l  
    return m
n=int(input())     
li=list(map(int,input().split()))  
print(le(li,n)) 
