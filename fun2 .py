
def Countdown(a):
    new_list=[]
    for x in range(a,-1,-1):
      if x >0 :
        new_list.append(x)
      else :
        new_list.append(0)
        return new_list

z=Countdown(3)
print(z)
#-------------------
my_list=[1,2]
def PrintandReturn(y):
   for z in range(len(y)):
      print(y[z])
      return y[z+1]

n=PrintandReturn(my_list)
print(n)
#------------------
ylist=[2,2,3,4,5,6]
def FirstPlusLength(n):
   z=len(ylist)+ylist[0]
   return z

u=FirstPlusLength(ylist)
print(u)

#-------------------
nlist=[5,2,3,2,1,4]
def greater(x):
    if len(x)<2:
        return False
    else:

      newlist=[]
      for i in range(0,len(x)):
        if x[i]>x[1]:
            newlist.append(x[i])
      return newlist
y=greater(nlist)
print(y)

#--------------
         
def value(v,l):
   zlist=[]
   for r in range(0,v):
      zlist.append(l)
   return zlist    
    
o=value(3,8)
print(o)

