def lis(l): 
    lis = [1]*n 
    for i in range (1, n): 
        for j in range(0, i): 
            if l[i] > l[j] and lis[i]< lis[j] + 1 : 
                lis[i] = lis[j]+1
    m = 0 
    for i in range(n): 
        m = max(m, lis[i])
    return m 
n=int(input())
l=list(map(int,input().split()))
print (lis(l)) 
