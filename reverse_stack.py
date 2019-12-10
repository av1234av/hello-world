class Stack(object):
    def __init__(self):
        self._stack=[]

    def push(self, item):
        self._stack.append(item)

    def pop(self):
        return self._stack.pop()

    def isEmpty(self):
        if self._stack:
            return False
        else:
            return True

    def reverse(self):
        pass