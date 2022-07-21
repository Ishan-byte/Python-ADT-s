from SinglyLinkedList import *

class Stack(SinglyLinkedList):

    def __init__(self):
        SinglyLinkedList.__init__(self)

    #push
    def push(self, Currency):

        newNode = LinkNode(Currency)

        if self.start == None:
           self.start = newNode 
        
        else:
            newNode.next = self.start
            self.start = newNode

    #pop
    def pop(self):
        if self.start == None:
            print("The List is empty")
            return
        else:
            curr = self.start
            if curr.next == None:
                self.start = None

                return
            else:
                curr = self.start.next
                self.start = curr

    #peek
    def peek(self):
        if self.start == None:
            print("The List is empty")
            return
        else:
            return self.start.Currency.getValue()

    #printStack
    def printStack(self):
        if self.start == None:
            print("The List is empty")
            return
        else:
            curr = self.start
            while (curr) :
                print(curr.Currency.getValue(), end = "    ")
                curr = curr.next
            print("")