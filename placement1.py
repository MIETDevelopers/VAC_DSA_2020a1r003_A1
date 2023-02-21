'''ch="aaa"
adi="ooo"
print("Aditya Raina\n19\nCSE")
#print(ch+ '\n'+ adi)
print(ch,adi,sep="-") #seperate function
print(ch,adi,end="miet")'''
#---------python program to take input of a number,name and print both the vairables in 2 different lines------------
'''x='adi'
y=19
print(x,y, sep='\n',end='\n')
print(type(x))
print("adi'tya")'''
#------------write a python program to take the input of 5 numbers in a single line-----------------------------------
'''print(type(y))
variable= list(map(int,input().split('.')))
print(variable)
print(type(variable))'''
#-------------program to take input of an IP address and seperate the domain as well as the last part------------------
'''n=input("enter IP address").split('.')
print(*n, sep='\n')'''
'''s=[True, 67, 90.7,'aditya',3+5j]
print(type(s))
print(6**5)'''
#------------write a program to print 1 if number is even and 0 if false.
'''ch=int(input("enter the number"))
print(ch%2)
print(7>0)'''
'''x=[1,2,3,4,5,7]
print(2 in x)
y=[2,3,4,5,6]
print([2,3,4,5,6] is y)'''
'''print(3==3 and 6==6)
print(4 or 5)
print((8 and 48))
print(8==0 and 8>90)'''

#--------------write a program to take input of the marks and print 1 if 40<marks<80 or else print 0.

'''marks=int(input("enter the marks: "))
print(marks>40 and marks<80)
print(13|14)# OR operation.
print(13^14)'''

#------------write a program to check if a given number is even or not using bit manipulation.
'''ch=int(input("enter the number"))
if ch & 1:
    print("odd")
else:
    print("even")'''
#-------------write a program to toggle kth  bit of a binary number---------------------------





#--------------write a program to find the total number of unset bits in a given number--------
'''ch=10010101
print(ch & ch-1)'''
#-------------------------------------sample question-----------------------------------------
'''current_wizard= input()
count=1
fights= int(input())
for i in range(fights):
    duo= input().split()
    if duo[1] is current_wizard:
        current_wizard= duo[0]
        count+=1
print(current_wizard,count,sep ='\n')'''
#---------------------------------------left_shift----------------------------------------------
'''6>>1 --0110'''

#------------write a program to take three numbers as inputs and print the largest and smallest numbers-------
'''x=input("enter 1st number")
y=input("enter 2nd number")
z=input("enter 3rd number")
list=[x,y,z]
print("largest number is",max(list))
print("smallest number is ",min(list))'''


#------------write a program to design a calculator----------------------
'''ch=int(input("select the operation:"))'''





#-----------write a program to take input of marks, roll number, name and print all these as colon seperated values.----
marks= input("enter marks").split()
roll_no= input("enter roll number").split()
name= input("enter your name").split()
print(marks,roll_no,name,sep=':')