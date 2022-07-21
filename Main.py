from re import A
from SinglyLinkedList import *
from Stack import *
from Queue import *
from Currency_.Dollar import *

def main():
    
    #Welcome Message
    print("\n")
    print("Welcome to the Lab 3 Program that the demonstrates the usage of differnt ADTS")

    #Dollars
    Dollars = [57.12, 23.44, 87.43, 68.99, 111.22, 44.55, 77.77, 18.36, 543.21, 20.21, 345.67, 36.18, 48.48, 101.00, 11.00, 21.00, 51.00, 1.00, 251.00, 151.00]

    #Currency array
    Currency = []

    #Creating dollar objects
    for d in Dollars:
        obj = Dollar(d)
        Currency.append(obj)

    #Creation of objects
    List = SinglyLinkedList()
    stack = Stack()
    queue =  Queue()

    print("\n")
     #LinkedList Operations
    print("Linked List operations: ")
    #A
    temp=[]
    for i in range(7):
       temp.append(Currency[i]) 
    temp.reverse()
    for i in range(7):
        List.addCurrency(temp[i], i )

    List.printList()

    #B
    print("Index of $87.43 is: ")
    List.findCurrency(87.43)
    print("Index of $44.55 is: ")
    List.findCurrency(44.55)

    #C
    List.RemoveCurrency(Dollar(111.22)) 
    List.RemoveCurrency(2)

    #D
    print("Contents of List after Operation C ")
    List.printList()

    #E
    c = 9
    for c in range(c, c + 4):
        List.addCurrency(Currency[c], c % 5)

    # #F
    index1 = (List.countCurrency() % 6)
    List.RemoveCurrency(index1)

    index2 = List.countCurrency() % 7
    List.RemoveCurrency(index2)
    
    #G
    print("Contents of List after Operation F")
    List.printList()


    print("\n")
    #Stack Operations

    print("Stack operations: ")

    #A
    i = 13
    for i in range(i, len(Currency)):
        stack.push(Currency[i])

    print("Peeking in the Stack: ")
   #B
    print(stack.peek())


    #C
    for i in range(3):
        stack.pop()

    
    print("Contents of stack after Operation C")
    #D
    stack.printStack()


    #E
    for i in range(5):
        stack.push(Currency[i])


    #F
    for i in range(2):
        stack.pop()


    print("Contents of stack after Operation F")
    #G
    stack.printStack()

    print("\n")

    #Queue Operations

    print("Queue operations: ")

    #A
    a = 5
    for a in range(a, a + 14):
        if a % 2 != 0:
            queue.enqueue(Currency[a]) 

    #B
    print("Front of the queue")
    print(queue.peekFront())
    print("Rear of the queue")
    print(queue.peekRear())

    #C
    for i in range(2):
        queue.dequeue()

    #D
    print("Contents of Queue after Operation C")
    queue.printQueue()

    #E
    b = 10
    for b in range(b, b+5):
        queue.enqueue(Currency[b])
    
    queue.printQueue()

    #F
    for i in range(3):
        queue.dequeue()

    #G
    print("Contents of Queue after Operation G")
    queue.printQueue()

    print("\n")

    print("***Thank you. The program ends here***")


main()