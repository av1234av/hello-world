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
            p = p.next
        p.next = n

    def traverse(self):
        p = self.head
        pp=[]
        while p:
            pp.append(p.val)
            p = p.next
        print pp

    def reverse(self):
        prev = None
        cur=self.head
        while cur:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node
        self.head = prev

    def find_mid_point(self):
        p1=self.head
        p2=self.head
        while p2 and p2.next:
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

    ll = LinkedList()
    for i in [10,3,45,2,67,89,3,77,65,34]:
        ll.add(Node(i))

    print "traversing a list"
    ll.traverse()
    ll.find_mid_point()

    print "reversing a list"
    ll.reverse()
    ll.traverse()
    # ll.interweave()