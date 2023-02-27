#--------------------------hacker-rank-------------------------------------
'''people=5
days=int(input())
total=0
for i in range(days):
    total=total+people//2
    people=(people//2)*3
print(total)'''

#---write a program to print all the permutations for the string--------------
'''x=input()
def perm():'''



#---oops concepts----------
#class can be defined as a collection of objects. its a logical entity that has some specific attributes and methods.
'''class name():
    def __init__(self,rollno):
        self.rollno=rollno
        print(self.rollno)
    def print(self,x):
        print(self.x)

ob1=name(3)
ob1.print("jatt")'''
#class employee store data such as name, employee, address, mobile number under the method employee data. create one more method as salary calculation in which we will calculate the salary e
'''class Employee():
    def Employeedata(self,name,address,mobileno,salary):
        self.name=name
        self.address=address
        self.mobileno=mobileno
        self.salary=salary
        print("name:-",self.name,"address:-",address,"mobileno:-",mobileno)
    def salarycalc(self,days):
        print((self.salary//30)*days)
ob1=Employee()
ob1.Employeedata(name="Aditya",address="Jammu",mobileno=98784781,salary=90000)
y=ob1.salarycalc(34)'''

#---------------------------------------------Inheritance, polymorphism---------------------------------
#--linear search,binary search, jump search, interpolation search,sorting,bubble,selection,insertion
#-merge,quick,self,count,radix,shell-------------
#-----------linear search------------------------------------------------------------------
#worst case=  [f(0)=g(x)/f(x);x--> size of the data]
#while calculating complexity, the constants should be dropped.
#ex=x(cube)+x(square)+2x; 2x and x(square)will be dropped. answer will be x(cube).
#thetha=average case
'''listt=[23,34,4,5,56,67]
key=34
for i in listt:
    if i==key:
        print(listt.index(i))'''
#--------
'''strr=input()
l=sorted(strr)
strr1= "".join(l)
print(strr1,sep=" ")'''

#-----------------program to a4b3c1--------------
'''x=input()
listt=[]
for i in range(len(x)+1):
    if x[i].isalpha():
        print(listt.append(i))
    if x[i].isdigit():
        print(x[i]*listt)'''
#write a program to find the sum of digits of elements in a list
#----------------write a program to print fibbonaci series using recursive functions.----------------
#write a program to generate a list where next term square addition of the even digits of the previous terms
#default is list=[42]
'''x=input().split()
listt=[]
for i in range(1,x):
    if x[i]%2==0:'''
#write a progam to generate a lsit where every next element is power of place value of digits of the number.