#write a python program to convert a list into a list of dictionaries---------------
'''strr=input().split()
strr1=input().split()
listt=[]
for i in range(len(strr)):
    listt.append({strr[i]:strr1[i]})
print(listt)'''
#--hacker rank----------------------------------
'''d1,m1,y1=list(map(int,input().split()))
d2,m2,y2=list(map(int,input().split()))
if y1==y2:
    if m1==m2:
        if d1==d2:
            print("timely return!")
        else:
            print(abs(d1-d2)*15)
    else:
        print(abs(m1-m2)*500)
else:
    print(10000)'''
#Recursive functions:-when a function calls itself in the code, it s a recursive function.
'''def rec_func(x,y):
    pass
    rec_func(20,30) #called inside the function.'''
#recursive functions use stack data structures for its use.

#write a program to calculate the factorial of a number using recursion---------
'''x=int(input("enter the number: "))
def fact(x):
    if x==1:
        return 1
    else:
        x=x*fact(x-1)
    return x
print(fact(x))'''
#write a program to find prime numbers between 1 to 100 using recursion
'''x=int(input("enter the number: "))
def prime(n,i=2):
    if n==i:
        return True
    elif n%i==0:
        return False
    else:
        prime(n,i+1)'''
#oops 
#classes and objects----------------------------------------------------
def miet(y):
    global x
    x=10
miet(9)
x=23
print(x)
#write a program to create a class CSE and in that class create methods as name and data.
'''class Miet:
    def __init__(self,name,branch):
        self.name=name
        self.branch=branch
    def data(self):
        print("marks=20")

    def dictt(self):
        dictt={self.name:self.branch}
        print(dictt)
ob1=Miet("aditya","CSE")
print(ob1.name,ob1.branch)
x=ob1.data()
y=ob1.dictt()
print(x)
print(y)'''
#--------------------------------
#--given a list,write a python program ot print the index number of the strings present.
'''x=['Navya', 98, 'Hema','siroj','tarun',78,90,'Ramya']
for i in range(len(x)):
    if str(x[i]).isdigit():
        pass
    else:
        print([i])'''

#-------------------------------------------------------------
'''x=(input().split())
for i in range(len(x)):
    if str(x[i]).isdigit():
        pass
    else:
        print([i])'''
#---prorgam to remove the common elements in the list----------------------
'''x=list(map(int,input().split()))
y=list(map(int,input().split()))
for i in range(0,len(x)+1):
    if i in y:
        x.remove(i)
        y.remove(i)
print(x)
print(y)'''

#--------tele-marketer---------------------------------------------------------------------
'''phone_number= input("enter your mobile number: ")
if phone_number[0]=='8' or phone_number[0]=='9' and phone_number[3]=='7' or phone_number[3]=='8' and  phone_number[1]==phone_number[2]:
    print("yes its a telemarketer!!")
else:
    print("no, its not a telemarketer!!")'''

#----python program to reverse a range in the list----------------
'''listt=list(map(int,input().split()))'''



#---program to remove all tuples with all none values---
x=input().split()
tuplle=()
for i in range(len(x)):
    if x[i]==None:
        pass
    else:
        tuplle.append([i])
#---a vendor supplies three types of toys:
#battery based toys, key-based toys,electrical charging based toys
#discount 10% on orders of battery based toys
#if more than 1000 or more tha n