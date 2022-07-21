from SinglyLinkedList import *

class Queue(SinglyLinkedList):
    
    def __init__(self):
        SinglyLinkedList.__init__(self)

    #enqueue
    def enqueue(self, Currency):
        newNode = LinkNode(Currency)
        if self.start == None:
            self.start = newNode
            return 
        else:
            temp = self.start
            while(temp.next  != None):
                temp = temp.next    
            temp.next = newNode
            self.end = newNode

    #dequeue
    def dequeue(self):
        if self.start == None:
            print("The Queue is empty")
            self.end = None
            return
        else:
            temp = self.start
            self.start = temp.next
            return temp.Currency.getValue()

    #peekFront
    def peekFront(self):
        if self.start == None:
            print("The Queue is empty")
            self.end = None
            return
        else:
            return self.start.Currency.getValue()


    #peekRear
    def peekRear(self):
        if self.start == None:
            print("The Queue is empty")
            self.end = None
            return
        else:
            temp = self.start
            while(temp.next != None):
                temp = temp.next
            return temp.Currency.getValue()

    #printQueue
    def printQueue(self):
        if self.start == None:
            print("The Queue is empty")
            self.end = None
            return
        else:
            curr = self.start
            print("Front to End: ")
            while(curr):
                print(curr.Currency.getValue(), end = "    ")
                curr = curr.next
            print("")