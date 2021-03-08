""" Implement Queue using stacks. """

import sys
class Queue(object):
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self,item):
        self.stack1.append(item)
        print ("Current queue: %s" % self.stack1)

    def dequeue(self):
        if self.stack2:
            value = self.stack2.pop()
        else:
            for _ in range(0, len(self.stack1)):
                self.stack2.append(self.stack1.pop())
            if self.stack2:
                value=self.stack2.pop()
            else:
                value = -1*float('inf')

            for _ in range(0, len(self.stack2)):
                self.stack1.append(self.stack2.pop())

        print("Current queue: %s" % self.stack1)

        return value

if __name__ == "__main__":
    q=Queue()
    q.enqueue(4)
    q.enqueue(6)
    q.enqueue(3)
    print(q.dequeue())
    q.enqueue(7)
    print (q.dequeue())
    q.enqueue(2)
    q.enqueue(9)
    print (q.dequeue())
    print (q.dequeue())
    print (q.dequeue())
    print (q.dequeue())
    print (q.dequeue())