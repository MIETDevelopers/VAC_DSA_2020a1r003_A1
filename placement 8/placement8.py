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
