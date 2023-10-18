#Basic 
for x in range(151):
    print(x)

#Multiples of Five
for i in range(5,1001):
    print(i*5)

#Counting, the Dojo Way
for y in range(1,101):
    if  y % 10==0 and y%5==0:
        print("Coding Dojo")
    elif y % 5==0:
        print("Coding")
    else:
        print(y)

#Whoa. That Sucker's Huge
sum=0
for y in range(500001):
    if y % 2 !=0:
     sum +=y
    
print (sum)

#Countdown by Fours 
for a in range(2018,0,-4):
   print(a)

#Flexible Counter
lowNum=2
highNum=10
mult=2
for m in range(lowNum , highNum+1):
    if m%mult==0:
       print(m)
   
 








