import random
def randInt(min= 0  , max=100   ):
    if min>max or max<0: 
       return False
    else:
      if min==0 and max==100:
        num = random.random()*100
        num=round(num)
      elif min==0:
        num=random.random()*max
        num=round(num)
      elif max==100:
        num=random.random()*min+min
        num=round(num)
      elif min!=0 and max !=100:
       num=random.random()*(max-min) +min
       num=round(num)
      return num
#print(randInt()) 		    # should print a random integer between 0 to 100
#print(randInt(max=50)) 	    # should print a random integer between 0 to 50
#print(randInt(min=50)) 	    # should print a random integer between 50 to 100
print(randInt(min=50, max=500))    # should print a random integer between 50 and 500