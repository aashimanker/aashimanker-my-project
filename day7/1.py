#stack 
#stack implmentation using a list

stack = []
stack.append('a')
stack.append('b')
stack.append('c')

#print("stack contents: ",stack)

# print("Popped element: ",stack.pop())
# print("Popped element: ",stack.pop())

#deque approach
from collections import deque

#create stack 
stack = deque()

stack.append('a')
stack.append('b')
stack.append('c')

# print("stack contents: ",stack)

# print("Popped element: ",stack.pop())
# print("Popped element: ",stack.pop())

#queue is a linear data structure 
#it follows fifo principle
#enqueue: insertion of data to the queue
#dequeue: deletion of data from the queue

#creating a queue
queue = deque()

#enqueuing elements
queue.append('a')
queue.append('b')
queue.append('c')

# print("Queue contents: ",queue)

#dequeueing operarion
# print("Dequeued element: ",queue.popleft())
# print("Dequeued element: ",queue.popleft())

#Simple queue
class SimpleQueue:
    def __init__(self):
        self.que = deque()

    def enqueue(self,item):
        self.que.append(item)
        print(f"Enque: {item}")

    def dequeue(self):
        if not self.is_empty():
            element = self.que.popleft()
            print(f"Deque: {element}")
        else:
            print("Queue is empty")
    def is_empty(self):
        return len(self.que) == 0

    def size(self):
        return len(self.que)

#q = SimpleQueue()
#enqueueing 
# q.enqueue("A")
# q.enqueue("B")
# q.enqueue("C")
# q.enqueue("D")
# print(q.size())

# #dequeuing
# q.dequeue()
# q.dequeue()
# print(q.size())

#priority queue
import heapq

class PriorityQueue:
    def __init__(self):
        self.que = []

    def enqueue(self,item,priority):
        heapq.heappush(self.que,(priority,item))
        print("enqueue: ",item)

    def dequeue(self):
        if not self.is_empty():
            priority,item = heapq.heappop(self.que)
            print(f"Dequeu: {item} with priority {priority}")
        else:
            print("Queue is empty")
    def is_empty(self):
        return len(self.que)==0
    def size(self):
        return len(self.que)

#que = PriorityQueue()

# que.enqueue("task a",2)
# que.enqueue("task b",1)
# que.enqueue("task c",3)

# que.dequeue()
# que.dequeue()

#Double ended queue : elements are allowed to be added or deleted from both the ends
class Deque:
    def __init__(self):
        self.deque = deque()

    def enqueueF(self,item):
        self.deque.appendleft(item)
        print(f"Enque from front: {item}")

    def enqueueR(self,item):
        self.deque.append(item)
        print(f"Enque from rear: {item}")

    def dequeueF(self):
        if not self.is_empty():
            element = self.deque.popleft()
            print(f"Deque from front: {element}")
        else:
            print("Queue is empty")
    def dequeueR(self):
        if not self.is_empty():
            element = self.deque.pop()
            print(f"Deque from rear: {element}")
        else:
            print("Queue is empty")

    def is_empty(self):
        return len(self.deque) == 0

    def size(self):
        return len(self.deque)

deq = Deque()

# deq.enqueueF("A")
# deq.enqueueF("B")
# deq.enqueueF("c")

# deq.dequeueF()
# deq.dequeueR()

#circular queue

class CircularQueue:
    def __init__(self,limit):
        self.que = [None]*limit
        self.front = -1  
        self.rear = -1
        self.limit = limit

    def enqueue(self,item):
        if (self.rear+1)%self.limit == self.front:
            print("Queue is full")
        elif self.front == -1:
            self.front = 0
            self.rear = 0
            self.que[self.rear] = item
            print(f"Enqueued: {item}")
        else:
            self.rear = (self.rear+1)%self.limit  
            self.que[self.rear] = item
            print(f"Enqueued: {item}")

    def dequeue(self):
        if self.front == -1:
            print("Queue is empty")
        elif self.front == self.rear :
            temp = self.que[self.rear]
            self.front = -1
            self.rear = -1
            print(f"Dequeued: {temp}")
        else:
            temp = self.que[self.front]
            self.front = (self.front+1)%self.limit
            print(f"Dequeued: {temp}")

    def size(self):
        if self.front <= self.rear:
            print(self.rear - self.front +1)
        elif self.front>= self.rear:
            print(self.limit-self.front+self.rear+1)
        elif self.front == -1:
            print("Queue is empty")

que = CircularQueue(5)
# que.enqueue(1)
# que.enqueue(2)
# que.enqueue(3)
# que.size()

# que.dequeue()
# que.dequeue()

#Q1: infix to postfix expression using stack
#i/p: a+b
#o/p: ab+

def in2po(expr):
    prec = {'+':1,'-':1,"*":2,"/":2,"^":3}
    stack = []
    postfix = []

    for char in expr:
        if char.isalnum():
            postfix.append(char)
        elif char=="(":
            stack.append(char)
        elif char==")":
            while stack[-1]!="(":
                postfix.append(stack.pop())
            stack.pop()
        else:
            while stack and prec[stack[-1]]<=prec[char]:
                postfix.append(stack.pop())
            stack.append(char)

    while stack:
        postfix.append(stack.pop())

    return "".join(postfix)

print(in2po("a+b"))            

#Q2: prefix to infix
#i/p: +ab
#o/p: a+b

def prefix2infix(expr):
    operators = ['+','-','*','/','^']

    stack = []
    expr = expr[::-1] # to avoid popping from empty stack 

    for char in expr:
        if char in operators:
            op1 = stack.pop()
            op2 = stack.pop()
            stack.append(f"{op1}{char}{op2}")
        else:
            stack.append(char)

    return stack[-1]

print(prefix2infix("+ab"))

#Q3: prefix to postfix expression

def prefix2postfix(expr):
    operators = ['+','-','*','/','^']

    stack = []
    expr = expr[::-1]

    for char in expr:
        if char in operators:
            op1 = stack.pop()
            op2 = stack.pop()
            stack.append(f"{op1}{op2}{char}")
        else:
            stack.append(char)

    return stack[-1]
print(prefix2postfix("+ab"))