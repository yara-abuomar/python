#Update Values in Dictionaries and Lists
x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]
x[1][0]=15
print(x)
students[0]['last_name']='Bryant'
print(students)
sports_directory['soccer'][0]='Andres'
print(sports_directory)
z[0]['y']=30
print (z)
#----------------------------3
#Iterate Through a List of Dictionaries
def iterateDictionary(stu):
    for s in range(len(stu)):
       for key ,val in stu[s].items():        
        print(key ,"-", val )

students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}]


iterateDictionary(students)
#----------------------------------------2

def iterateDictionary2(key_name, some_list):
   for f in range(len(some_list)):
        text = ""
        for k,v in some_list[f].items(): 
            text+=k + ":"+ v  +", "       
        print(text)

iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)

#----------------------

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printInfo(do):
    
    for k, v in dojo.items():
        print(len(v),k ,": ")
        # print(v)
        for i in range(len(v)):
            print(v[i])
printInfo(dojo)
  