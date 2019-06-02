n,q=map(int,input().split())
li=list(map(int,input().split()))
li1=[]
l=[]
k=[]
for i in range(0,q):
  u,v=map(int,input().split())
  for i in range(u,v+1):
    li1.append(li[i-1])
  l.append(sum(li1)) 
k.append(l[0])
for i in range(0,len(l)-1):
  s=l[i+1]-l[i]
  k.append(s)
for i in k:
  print(i)




