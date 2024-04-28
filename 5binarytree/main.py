class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def parent(self, key):
        tmp = self.root
        if tmp is None:
            return None
        else:
            return self.parent_help(key, tmp)

    def parent_help(self, key, current):
        if key > current.key:
            if current.right.key == key:
                return current
            else:
                return self.parent_help(key, current.right)
        elif key < current.key:
            if current.left.key == key:
                return current
            else:
                return self.parent_help(key, current.left)
        else:
            if current.left is not None:
                return self.parent_help(key, current.left)
            if current.right is not None:
                return self.parent_help(key, current.right)

    def search(self, key):
        tmp = self.root
        if tmp is None:
            print('Nie ma elementu o tym kluczu')
            return None
        else:
            return self.search_help(key, tmp)

    def search_help(self, key, current):
        tmp = current
        if key == tmp.key:
            return tmp.value
        elif key > tmp.key:
            return self.search_help(key, tmp.right)
        elif key < tmp.key:
            return self.search_help(key, tmp.left)
        else:
            print('Nie ma elementu o tym kluczu')
            return None

    def insert(self, key, value):
        if self.root is None:
            self.root = Node(key, value)
        else:
            return self.insert_help(key, value, self.root)

    def insert_help(self, key, value, current):
        tmp = current
        if key > tmp.key:
            if tmp.right is None:
                tmp.right = Node(key, value)
            else:
                return self.insert_help(key, value, tmp.right)
        elif key < tmp.key:
            if tmp.left is None:
                tmp.left = Node(key, value)
            else:
                return self.insert_help(key, value, tmp.left)
        elif key == tmp.key:
            tmp.value = value
            return

    def delete(self, key):
        if self.root is None:
            print('Nie ma elementu o tym kluczu')
            return None

        parent = None
        current = self.root
        while current is not None and current.key != key:
            parent = current
            if key < current.key:
                current = current.left
            elif key > current.key:
                current = current.right

        if current is None:
            print('Nie ma elementu o tym kluczu')
            return None

        # deleting the root
        if parent is None:

            # no children
            if current.left is None and current.right is None:
                self.root = None

            # one child
            elif current.left is None:
                self.root = current.right
            elif current.right is None:
                self.root = current.left

            # two children
            else:
                child = current.right
                while child.left is not None:
                    parent = child
                    child = child.left
                if parent is not None:
                    parent.left = child.right
                    child.left = current.left
                    child.right = current.right
                    self.root = child
                else:
                    child.left = current.left
                    self.root = child
            return

        # no children
        if current.left is None and current.right is None:
            if parent.left == current:
                parent.left = None
            elif parent.right == current:
                parent.right = None

        # one child
        elif current.left is None:
            if parent.left == current:
                parent.left = current.right
            else:
                parent.right = current.right
        elif current.right is None:
            if parent.left == current:
                parent.left = current.left
            else:
                parent.right = current.left

        # two children
        else:
            child = current.right
            while child.left is not None:
                child = child.left
            parent = self.parent(child.key)
            if parent.left == child:
                parent.left = child.right
            else:
                parent.right = child.right
            current.key = child.key
            current.value = child.value

    def height(self):
        return self.height_help(self.root)

    def height_help(self, node):
        if node is None:
            return 0
        left_height = self.height_help(node.left)
        right_height = self.height_help(node.right)
        return max(left_height, right_height) + 1

    def print_tree(self):
        print("==============")
        self._print_tree(self.root, 0)
        print("==============")

    def _print_tree(self, node, lvl):
        if node is not None:
            self._print_tree(node.right, lvl + 5)

            print()
            print(lvl * " ", node.key, node.value)

            self._print_tree(node.left, lvl + 5)

    def print_sorted(self, current=None):
        if current is None:
            return self.print_sorted(self.root)
        if current.left:
            self.print_sorted(current.left)
        print('{}'.format(current.key), '{}'.format(current.value), end=',')
        if current.right:
            self.print_sorted(current.right)


def main():
    bst = BinaryTree()
    for i, j in {50: 'A', 15: 'B', 62: 'C', 5: 'D', 20: 'E', 58: 'F', 91: 'G', 3: 'H', 8: 'I', 37: 'J', 60: 'K',
                 24: 'L'}.items():
        bst.insert(i, j)
    bst.print_tree()
    bst.print_sorted()
    print()
    print(bst.search(24))
    bst.insert(20, 'AA')
    bst.insert(6, 'M')
    bst.delete(62)
    bst.insert(59, 'N')
    bst.insert(100, 'P')
    bst.delete(8)
    bst.delete(15)
    bst.insert(55, 'R')
    bst.delete(50)
    bst.delete(5)
    bst.delete(24)
    print(bst.height())
    bst.print_sorted()
    print()
    bst.print_tree()


if __name__ == '__main__':
    main()
