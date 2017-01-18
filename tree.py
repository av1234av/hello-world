class Node(object):
    def __init__(self,val):
        self.right = None
        self.left = None
        self.val = val


class Tree(object):

    def __init__(self):
        self.root = None

    def get_root(self):
        return self.root

    def add(self, val):
            if not self.root:
                self.root = Node(val)
            else:
                self._add(val, self.root)

    def _add(self, val, node):
        if val < node.val:
            if node.left:
                self._add(val, node.left)
            else:
                node.left = Node(val)

        else:
            if node.right:
                self._add(val, node.right)
            else:
                node.right = Node(val)

    def find(self, val):
        if self.root:
            self._find(val, self.root)
        else:
            return None

    def _find(self, val, node):
        if node.val == val:
            return node
        elif val < node.val and node.left is not None:
            self._find(val, node.left)
        elif val > node.val and node.right is not None:
            self._find(val, node.right)

    def print_tree(self):
        if not self.root:
            return 'No more nodes'
        else:
            self._print_tree(self.root)

    def _print_tree(self, node):
        if node:
            self._print_tree(node.left)
            print node.val+' '
            self._print_tree(node.right)

if __name__ == '__main__':
    t=Tree()
    t.add(5)
    t.add(6)
    t.add(3)
    t.add(7)
    t.print_tree()
