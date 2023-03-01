'''Data Structures
A specialized format for organizing,processing,retrieving and sorting data. While there are several basic and advanced structure types,any data structure is designed to arrange data to suit a specific purpose so that it can be accessed and worked with appropriate ways.
array has the base address present in it.
arr=[23,45,56,67,78]
base address and indices =0 have the same value.
base address +size*number of values or indices.
Specifications
1)organizing data
2)accessing methods
3)degree of associativity
4)processing alternatives for information
Two Types
1)Linear=stacks,queues
2)Non-linear= graphs,trees
PRIMITIVE DATA STRUCTURES= integer,float,character,pointer
NON-PRIMITIVE DATA STRUCTURES= array,lists,files
LISTS= Linear Lists, Non-linear lists
Algorithms
Time Complexity:-
Big-0=worst case
Omega-0= best case
Thetha-0=average case
LINKED LISTS=elements can be dynamically allocated.
1)Singly Linked List= collection of nodes where each node holds two fields; head and tail
1-->Insertion,deletion,traversing,searching
2)Doubly LInked List= we can traverse in both the directions. takes more time to insert or delete as both the previous and the next address needs to be updated.
2--->insertion,deletion,traversing,searching
APPLICATIONS
1)implements stacks,queues,binary trees and graphs of pre-defined size.
2)implements dynamic memory management functions of operating system.
.next=address
.data= data
asymptotic time complexity to add a element in the list=0(n).'''

#------------data structures------------------
'''class Node:
    def __init__(self,dataval=None):
        self.dataval=dataval
        self.nextval=None
class SlinkedList:
    def __init__(self):
        self.headval=None
list1=SlinkedList()
list1.headval=Node("Mon")
e2=Node("Tue")
e3=Node("Wed")
list1.headval.nextval=e2
e2.nextval=e3'''


#----
'''def Atbeggining(self,newdata):
        NewNode=Node(newdata)
        NewNode.nextval=self.headval
        self.headval= 
        '''
#----program to print the largest palindrome number that can be traversed in the list.----------------
#--------------------------------------program to reverse a linked list------------------------------
#---------------------insertion in doubly linked list------------------------------------------------
'''def append(self,new_data):
    new_node=Node(data=new_data)
    last=self.head
    new_node.next=None
    if self.head is None:
        new_node.prev=None
        self.head=new_node
        return
    while(last.next is not None):
        last=last.next
    last.next=new_node
    new_node.prev=last'''
#---------------program for linear search on tuples---
'''arr=(input().split())
y=tuple(arr)
key=input()
for i in range(len(y)-1):
    if y[i]==key:
        print("found at index:-",i)'''

#----python program convert a given string list tot a tuple
'''strr=input()
listt=[]
for i in strr:
    listt.append(i)
print(tuple(listt))'''


'''strr=input().replace(" ","")
listt=[]
for i in strr:
    listt.append(i)
print(tuple(listt))'''


'''def quicksort(arr):
    if len(arr)<=1:
        return arr
    else:
        pivot=arr[0]
        less=[x for x in arr[1:]if x<=pivot]
        greater=[x for x in arr[1:]if x>pivot]
        return quicksort(less) +[pivot] + quicksort(greater)
    
arr=[99,22,1,2,5,3]
sorted_arr=quicksort(arr)
print(sorted_arr)'''
 #find the sum of all the items in a dictionary
#take values in numeric type(n>0)
s=0
for i in dict.values():
    s +=i
print(s)
