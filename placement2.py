#-----------conditionals----------------------------------
#-- write a program to give the grade to students criteria is marks<40 if marks 50<marks<60:B; 40<marks<50: C and greater than 60 A
'''marks=int(input("enter the marks"))
if marks<=40:
    print("student has failed")
elif 40<marks<50:
    print("grade is C")
elif 50<marks<60:
    print("grade is B")
elif marks>60:
    print("Grade is A")
else:
    print("exam not given")'''
#----write a program to check if the given digits of the number are even or odd--
'''x=int(input("enter the number: "))
c=x%10 #extracting digits of a  number.
d=x//10
if c%2==0:
    print("even")
else:
    print('odd')
if d%2==0:
    print("even")
else:
    print('odd')'''

#--- write a program to take 5 subject marks as the input and calculate the percentage and also allocate a grade to students.
#--criteria: all marks>33 to pass, overall percentage>40 to pass.
#--grade:

'''subject_marks=list(map(int,input("enter marks: ").split(" ")))
a,b,c,d,e=subject_marks  #packing and unpacking of data sequence
x=sum(subject_marks)
total_marks=500
percentage=x/total_marks*100
print(percentage)
if a>33 and b>33 and c>33 and d>33 and e>33 and percentage>40:
    print("pass")
    if 40<percentage<60:
        print("grade is 2nd")
    elif 60<percentage<80:
        print("grade is 1st")
    elif percentage>80:
        print("grade is excellent")
else:
    print("chal paar")'''
#------------------------------Looping------------------------------------------------
'''i=1
while i<=10:
    print(i)
    i+=1'''
#-----write a program to print the digits of a given number------------------------------
'''number=int(input("enter the number: "))
while number:   #important factor
    rem=number%10
    number//=10
    print(rem)'''
#-------write a program to run a palindrome or not--------------------------------------
'''number=int(input("enter: "))
temp=number
total=0
while number:
    rem= number%10
    number//=10
    total=total*10+rem
if total==temp:
    print("palindrome hai")
else:
    print("nahi hai")'''
 #----write a program to find the absolute difference between summation of odd and even digits--
'''number=int(input("enter: "))
even_digits_sum=0
odd_digits_sum=0
difference=1
total=0
while number:
    rem= number%10   #4567
    if rem%2==0:
        print("even")
        even_digits_sum+=rem
    
    else:
        print("odd")
        odd_digits_sum+=rem
    number//=10
print(abs(even_digits_sum-odd_digits_sum))'''

#---program to check whether a number is armstrong or not using while loop------------
'''num=int(input("enter the number"))
size= len(num)'''




#----------------------For Loop------------------------------------

#range(start,end point,stop)
'''for i in range(34,45,2):
    print(i,end="--")'''

#--------write a program to find the perfect numbers between 1 to n------






#----write a program  to display "hello",if a number is multiple of 5 and "bye" if its not---
'''ch=int(input("enter the number: "))
if ch%5==0:
    print("hello")
else:
    print("bye")'''
#---write a program to print the below to given age:-->
#i).age<18 "sorry you are a minor"
#ii) age between 18 and 21 "congrats you are major but not for marriage"
#iii)age>21 congrats you can marry.

'''age=int(input("enter the age: "))
if age<18:
    print("sorry you are a minor!")
elif 18<age<21:
    print("you are a major but not eligible for marriage!")
elif age>21:
    print("you can marry!!")'''

#-----write a greeting program that shows a message depending on what time of the day---
#--it is morning,afternoon,evening or night(time in 24 hours format)
'''x=int(input("enter the time of the day"))
if x<=1200:
    print("good morning!")
elif 1200<=x<=3000:
    print("good afternoon!")
elif x>3000:
    print("Good evening!")'''

#write a program to calculate the electricity bill(unit from user)according to the following criteria:
'''unit       price
first 100       no charge
next 100 unit   6rs per unit
after 200 unit  8rs per unit
fix charge of rs40 is applicable to all'''
'''unit =int(input("enter the unit"))
price=0
fix=40
if unit<100:
    print("no charge",)
    price= fix
    print(price)
elif 100<unit<200:
    print("charge is:-")
    price1= fix +6*(unit-100)
    print(price)
elif unit>200:
    print("charge is")
    price= (fix + 8*(unit-100)-200)
    print(price)'''
#------program to calculate sum of three numbers, if values are equal,return 3 times there sum--
'''ch=list(map(int,input("enter the number: ").split()))
a,b,c=ch
print(a,b,c)
if a==b==c:
    print(3*(a+b+c))
else:
    print((a+b+c))'''

#----write a program  to test whether m is a factor of n------
'''n=int(input("enter the number: "))
m=int(input("enter the testing number: "))
if n%m==0:
    print("yes, its a factorial")
else:
    print("no")'''
#---A student grade is calculated as A if the score is 90 and above,'B'if the score is 75 to 89,'C' if 60 to 74 and Dif less than 60.
'''marks=int(input("enter your marks:  "))
if marks>=90:
    print("Grade A")
elif 75<=marks<=89:
    print("Grade B")
elif 60<=marks<=74:
    print("Grade C")
elif marks<=60:
    print("Grade D")'''

#----write a program to display congratulations if garde is A or B, work hard if C and try next time if D

'''grade=(input("enter your grade: "))
if grade=='A' or grade=='B':
    print("congratulations")
elif grade=='C':
    print("Work hard!")
elif grade=='D':
    print("Try hard next time")'''
#---write a program to remove the last digit from the given integer number-------
'''ch=int(input("enter the number"))
x=ch//10
print(x)'''

#write a program to check if the given number is negative or positive-------------
'''ch=int(input("enter the number: "))
if ch>=0:
    print("positive")
if ch<0:
    print("negative")'''

#program to print odd number sequence below N----------------
'''i=0
number=int(input("enter the number: "))
for i in range(1,number):
    if i%2!=0:
        print(i)'''

#program to print even number sequence below N---------------
'''i=0
number=int(input("enter the number: "))
for i in range(1,number):
    if i%2==0:
        print(i)'''
#program to write fibbonaci series upto N---------------------
'''x= int(input("enter the number: "))
i=0
n1,n2=0,1
print(n1,n2)
for i in range(2,x):
    n3=n1+n2
    n1=n2
    n2=n3
    print(n3)'''

#program to check whether a year is leap year or not.
'''year=int(input("enter the year"))
if year%4==0:
    print("its a leap year")
else:
    print("not a leap year")

#program to find factorial of n'''
n=int(input("enter the number: "))
i=0
while i<=n:
    fact=i
    fact=fact*fact-1
    print(fact)  