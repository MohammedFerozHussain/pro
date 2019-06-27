N = 0
E = 1
S = 2
W = 3
def c(s): 
    x = 0
    y = 0
    d = N 
    for i in range(len(s)):
        m = s[i]
        if m == 'R': 
            d = (d + 1)%4
        elif m == 'L': 
            d = (4 + d - 1)%4
        else:    
            if d == N: 
                y += 1
            elif d == E: 
                x += 1
            elif d == S: 
                y -= 1
            else: 
                x -= 1
    return (x == 0 and y == 0) 
s=input()
if c(s): 
    print ("yes")
else: 
    print ("no")
