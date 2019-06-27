import string 
a=set(string.ascii_lowercase) 
def p(string): 
    return set(string.lower())>=a 
s=input()
if(p(s) == True): 
    print("yes") 
else: 
    print("no") 
