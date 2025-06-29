
import random as r #randint ka use karenge for random values

class node:
    def __init__(self,data):
        self.data=data # ismae main value hoga
        self.next=None
        self.prev=None # ismae address hoga next value ka jiska link banega
    
class linkedList:
    def __init__(self):
        self.head=None # ye hoga None but point karega starting ko,isko ni hilana  hai

    def display(self):
            try:
                if self.head is None: # agar head none yahi list empty
                    print(f"\n\nList is empty")
                    return
                current=self.head
                print("None",end="") # agar entries hai to ek pointer lelo
                while current: # jab tak data hai tab tak  print hoag and current ka value next wala address pe jayega
                    print(f"<= {current.data}",end=" =>")
                    current=current.next
                print(f"None")
            except Exception as e:
                print(f"\n\nError occured:{e}")
                ask=input(f"\nWanna to try again? [y]=> ")
                if ask=="y":
                    self.display()


    def insertFirst(self):
        while  True:
            try:
                data=int(input(f"\nenter data to insert=> "))
                newNode=node(data) # naya node with data
                newNode.next=self.head
                newNode.prev=None # node ke address mae none
                self.head=newNode # head karega node ke value ko refer
                print(f"\n{data} inserted in first place.")
                break
            except Exception as e:
                print(f"\nError occured:{e}")
                ask=input(f"\nwant to try again? [y]=> ")
                if ask!="y":
                    break
    
    def insertLast(self):
        while True:
            try:
                data=int(input(f"\nenter data to insert=> "))
                newNode=node(data) # node bana liya with data
                if self.head is None: # agar list khali
                    newNode.next=self.head 
                    newNode.prev=None# head yani none ka value node address pe
                    self.head=newNode # head ka value node ka data
                    print(f"\n{data} inserted is first place as no data is present.")
                    break
                current=self.head # agar data hai to current naam ka pointer lelo
                while current.next: # jab tak pointer none ni hota yani second last node pe janke rukega loop
                    current=current.next
                current.next=newNode
                newNode.prev=current #second last ka next address yani last element ka address ,usko new node ka address dekar link bana diya
                print(f"\n{data} inserted in last place.")
                break
            except Exception as e:
                print(f"\nError occured:{e}")
                ask=input(f"\nwant to try again? [y]=> ")
                if ask!="y":
                    break

    def insertRandom(self):
        while True:
            try:
                data=int(input(f"\nenter data to insert=> "))
                newNode=node(data) #naya node banaya with data
                if self.head is None: # agar node khali to new node ka address none and head point karega new node ko
                    newNode.next=self.head
                    self.head=newNode
                    newNode.prev=None
                    print(f"\n{data} inserted in random place.")
                    break
                current=self.head # agar data hai to current pointer banalo
                lenght=0 # ye lenght store karne ke liye hai
                while current: # jab tak value hai
                    lenght+=1 # tak tab ye plus hoga aur humko number of values dega ie lenght of whole list
                    current=current.next # current ko aage wale address pe move karte raho,if none to loop se bahar
                position=r.randint(0,lenght-1) # randint se random exclusive number le liya [start,end]
                if position==0 and self.head.next is  None and self.head.prev is None: # agar 0 hai to wahi new node ke address pe none fir head point to new node
                    newNode.next=self.head
                    self.head=newNode
                    newNode.prev=None
                    print(f"\n{data} inserted at index {position}")
                    break
                else:
                    current=self.head # agar dusra position hai toh current ka value reset to 1st node
                    for i in range(position-1): # 0 se lekar wo position ho jayega extra to position -1 to reach index of that node
                        current=current.next # current ko aake barhaya gaya                     previousnode-----x------->laternode
                    newNode.next=current.next
                    current.next.prev=newNode # current ka jo nexr address hai wo dal diya newnode mae   <-----newnode--->laternode]
                    current.next=newNode 
                    newNode.prev=current
                    # jo current address tha usmae new node ka address
                    print(f"\n{data} inserted at index {position}")
                    break
            except Exception as e:
                print(f"\nError occured:{e}")
                ask=input(f"\nwant to try again? [y]=> ")
                if ask!="y":
                    break

    def delFirst(self):
        while True:
            try:
                if self.head is None:
                    print(f"\nlist is empty")
                    break
                remItem=self.head.data
                self.head=self.head.next
                self.head.prev=None
                print(f"\n{remItem} removed from first: ")
                break
            except Exception as e:
                print(f"\nError occured:{e}")
                ask=input(f"\nwant to try again? [y]=> ")
                if ask!="y":
                    break
            
    def delLast(self):
        while True:
            try:
                if self.head is None:
                    print(f"\nlist is empty")
                    break
                current=self.head
                if self.head.next is None and self.head.prev is None:
                    remItem=self.head.data
                    
                    self.head=None
                    print(f"\n{remItem} removed from start as it\'s the only data")
                    break
                current=self.head
                while current.next.next:
                    current=current.next
                remItem=current.next.data
             
                current.next=None
                print(f"\n{remItem} removed from last")
                break
            except Exception as e:
                print(f"\nError occured:{e}")
                ask=input(f"\nwant to try again? [y]=> ")
                if ask!="y":
                    break

    def delRandom(self):
        while True:
            try:
                if self.head is None:
                    print(f"\nlist is empty")
                    break

                lenght=0
                current=self.head
                while current:
                    lenght+=1
                    current=current.next
                
                position=r.randint(0,lenght-1)
                if position==0 and self.head.prev is None and self.head.prev is None :
                    remItem=self.head.data
                    self.head=self.head.next
                    self.head.prev=None
                    print(f"\n{remItem} removed from start as it\'s the only data")
                    break
                current=self.head
                for i in range(position-1):
                    current=current.next
                remItem=current.next.data
                current.next.next.prev=current
                current.next=current.next.next
               
                print(f"\n{remItem} is deleted from random position")
                break
            except Exception as e:
                print(f"\nError occured:{e}")
                ask=input(f"\nwant to try again? [y]=> ")
                if ask!="y":
                    break
    def search(self):
        while True:
            try:
                if self.head is None:
                    print(f"\nlist is empty")
                    break
                element=int(input(f"enter data to search=> "))
                current=self.head
                flag=False
                position=0
                while current:
                    
                    if current.data==element:
                        flag=True
                        break
                    position+=1
                    current=current.next
                if flag:
                    print(f"\n{element} found at index {position}")
                    break    
            except Exception as e:
                print(f"\nError occured:{e}")
                ask=input(f"\nwant to try again? [y]=> ")
                if ask!="y":
                    break                   


        

def menu():
    ll=linkedList()
    while True:
        try:
            insert=int(input(f"\n1:insert at begining\n2:insert at end\n3:insert at random\n4:delete from start\n5:delete from last\n6:delete randomly\n7:display\n8:search\n0:exit\nenter your choice=> "))
            if insert==1:
                ll.insertFirst()
            elif insert==2:
                ll.insertLast()
            elif insert==3:
                ll.insertRandom()
            elif insert==4:
                ll.delFirst()
            elif insert==5:
                ll.delLast()
            elif insert==6:
                ll.delRandom()
            elif insert==7:
                ll.display()
            elif insert==8:
                ll.search()
            elif insert==0:
                print(f"\nExiting..")
                exit()
            else:
                print(f"\nPlease enter correct value.")
                continue
        except Exception as e:
            print(f"\nError occured:{e}")
            ask=input(f"\nwant to try again? [y]=> ")
            if ask!="y":
                break

menu()
