class Node(object):
    def __init__(self,val):
        self.next = None
        self.val = val


class LinkedList(object):
    def __init__(self):
        self.head=None

    def add(self,n):
        if not self.head:
            self.head = n
            return

        p = self.head
        while p.next:
            p=p.next
        p.next = n

    def traverse(self):
        p = self.head
        while p:
            print p.val
            p = p.next

    def find_mid_point(self):
        p1=self.head
        p2=self.head
        while p2.next:
            p1=p1.next
            p2=p2.next.next
        print 'midpoint {}'.format(p1.val)
        return p1

    def interweave(self):
        p=self.head
        p1=self.find_mid_point()
        while p1.next:
            t=p1.next
            p1.next=p.next
            p.next=p1
            p1=t

        self.traverse()
if __name__ == '__main__':
    n1 = Node(10)
    n2 = Node(3)
    n3 = Node(45)
    n4 = Node(2)
    n5 = Node(67)

    ll = LinkedList()
    ll.add(n1)
    ll.add(n2)
    ll.add(n3)
    ll.add(n4)
    ll.add(n5)

    ll.traverse()
    ll.find_mid_point()
    ll.interweave()