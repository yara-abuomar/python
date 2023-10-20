BiggieSize=[-1, 3, 5, -5]
def big(x):
  for m in range(0,len(x)):
    if x[m]>0 :
      x[m]="big"
  return x

z=big(BiggieSize)
print(z)

#------------------------
pos_list=[1,6,3,-4,-2,-7,-2]
def Positives (l):
  count=0
  for d in range(len(l)):
    if l[d]>0:
     count+=1
  l.pop()
  l.append(count)
  return l

e=Positives(pos_list)
print(e)

#--------------------
sum_list=[6,3,-2]
def sum(p):
  sum=0
  for y in range(len(p)):
    sum+=p[y]
  return sum
n=sum(sum_list)
print(n)

#------------------
avg_list=[1,2,3,4]
def avg(k):
  sum=0
  for g in range(len(k)):
    sum+=k[g]
    av=sum/(len(k))
  return av
d=avg(avg_list)
print(d)
#--------------------
len_list=[6,8]
def lingth(s):
  return len(s)
e=lingth(len_list)
print(e)
#-----------------min
min_list=[5,7,9,0,-3,-9,-11]
def min(v):
  if len(v)==0:
     return False
  else:
     r=v[0]
     for g in range(len(v)):
      if r>v[g]:
       r=v[g]
     return r 
dd=min(min_list)
print(dd)      
 
 #----------------max
max_list=[5,7,9,0,-3,-9,-11,65]
def max(j):
  if len(j)==0:
     return False
  else:
     u=j[0]
     for k in range(len(j)):
      if u<j[k]:
        u=j[k]
     return u
yy=max(max_list)
print(yy) 

 #---------------------------------
ullist=[2,3,4,5,0]
def UltimateAnalysis(ul):
  
  ssum=0
  avgg=0
  length=len(ul)
  min=ullist[0]
  max=ullist[0]
  for q in range(len(ul)):
    ssum+=ul[q]
    if ul[q]>max:
      max=ul[q]
    if ul[q]<min:
      min=ul[q]

  avgg=ssum/(len(ul))
  uldic={
    "sumTotal": ssum,
    "avg": avgg,
    "length": length ,
    "minimum": min ,
    "maxmum" : max 
  }
  print(uldic)

UltimateAnalysis(ullist)
#-----------------reverse list 
r_list=[6,7,8,0,1]
def reverselist(x):
    for i in range(int(len(x)/2)):
        x[i],x[len(x)-1-i]=x[len(x)-1-i],x[i]
    return x
re=reverselist(r_list)
print(re)
