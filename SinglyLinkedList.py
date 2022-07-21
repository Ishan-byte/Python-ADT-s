from LinkNode import *

class SinglyLinkedList:

    def __init__(self, count = 0):
        count = count
        self.start= None
        self.end = None

    def counter(self):
        count = 0
        temp = self.start
        while(temp):
            temp = temp.next
            count += 1
        return count

    #printList method
    def printList(self):
        temp = self.start
        while(temp):
            print(temp.Currency.getValue(), end= " ")
            temp = temp.next
        print("")
   
    # Add Currency method
    def addCurrency(self, Currency, index):
        
        limit = self.counter()
        
        if(limit < index):
            print("The linked list does not include that specific index")

        else:
            newNode = LinkNode(Currency)

            curr = self.start
            if index == 0:
                newNode.next = self.start
                self.start = newNode
                return

            for i in range(index-1):
                if curr and curr.next:
                    curr = curr.next
                else:
                    return
            temp = curr.next
            curr.next = newNode
            newNode.next = temp


    # Remove Currency method by taking Currency object
    def RemoveCurrency(self, value):
        curr = self.start

        if isinstance(value, Currency):
            if curr.Currency.getValue() == value.getValue():
                self.start = curr.next
                return
            while curr.next.Currency.getValue() != value.getValue():
                curr = curr.next
                if curr.next == None:
                    return
            curr.next = curr.next.next


        else:
            index  = 0
            limit = self.counter()
            if(limit < value):
                return
            else:
                curr = self.start
            
                if(value == 0):
                    self.start = curr.next
                    return 
                else:
                    for i in range(value-1):
                        curr = curr.next

                    curr.next = curr.next.next

    #Find Currency method that takes currecny object as parameter
    def findCurrency(self, value):
        index = 0
        curr = self.start
        if curr.Currency.getValue() == value:
            return 0
        while curr.Currency.getValue() != value:
            curr = curr.next
            index+=1
            if curr.next == None:
                return
        print (index)
        return index
            

    #getCurrency method that takes index values as parameters and returns Currency object
    def getCurrency(self, index):

        limit  = self.counter()

        if limit > index: 
            curr = self.start
            if(index == 0):
                print(curr.data)
                return
            else:
                for i in range(index):
                    curr = curr.next
            print(curr.data) 
            return curr.data 

        else:
            print('The linked list is not long enough for this index')



    #isListEmpty method
    def isListEmpty(self):
        if self.start == None:
            print("the List is empty")
        else:
            print("the List is not empty")


   #count currency method 
    def countCurrency(self):
        result = self.counter()
        return result