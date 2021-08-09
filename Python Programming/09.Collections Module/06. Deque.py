# Deque (Doubly Ended Queue) is the optimized list for
# quicker append and pop operations from both sides of
# the container. It provides O(1) time complexity for
# append and pop operations as compared to list with
# O(n) time complexity.


from collections import deque

# Declaring deque
queue = deque(["A", "B", "C"])

print(queue)

queue.append("D")
print("The deque after appending at right is : ")
print(queue)

queue.appendleft("E")
print(queue)

queue.pop()
print(queue)

queue.popleft()
print(queue)
