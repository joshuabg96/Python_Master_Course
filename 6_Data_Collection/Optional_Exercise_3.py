# In a planification of a proyect a task list has been done.
# For every task a priority order has been assigned (small = high priority)
# Create a queue with all the task sorted byt without the order number

tasks = [
    [6, "Distribution"],
    [2, "Design"],
    [1,"Conception"],
    [7,"Maintenance"],
    [4, "Production"],
    [3, "Planification"],
    [5, "Test"]
]
print("Disorder Task")
for task in tasks:
    print(task[0], task[1])

from collections import deque
tasks.sort()

Q = deque()
for task in tasks:
    Q.append(task[1])

print("\nOrder Task")
for task in Q:
    print(task)