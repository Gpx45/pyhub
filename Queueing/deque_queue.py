# Importing the library
from collections import deque

#Creating a Queue
queue = deque([1,3,5,8,9])

#Enqueuing elements to the Queue
queue.append(7)

queue.append(10)

#Dequeuing elements from the Queue
queue.popleft()
queue.popleft()

