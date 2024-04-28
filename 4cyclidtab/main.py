class CyclicTab:
    def __init__(self):
        self.tab = [None for i in range(5)]
        self.size = len(self.tab)
        self.front = 0
        self.rear = 0

    def realloc(tab, size):
        oldSize = len(tab)
        return [tab[i] if i < oldSize else None for i in range(size)]

    def is_empty(self):
        if self.front == self.rear:
            return True
        else:
            return False

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.tab[self.front]

    def dequeue(self):
        if self.is_empty():
            return None
        else:
            val = self.tab[self.front]
            self.tab[self.front] = None
            self.front = (self.front + 1) % self.size
            return val

    def enqueue(self, data):
        # self.tab[self.rear] = data
        # self.rear = (self.rear + 1) % self.size
        if self.tab[0] is None:
            for i in range(1, self.size):
                tmp = self.tab[i]
                self.tab[i - 1] = tmp
            self.rear = (self.rear - 1) % self.size
            self.front = (self.front - 1) % self.size

        self.tab[self.rear] = data
        self.rear = (self.rear + 1) % self.size

        if self.is_empty():
            self.tab = CyclicTab.realloc(self.tab, 2 * self.size)
            self.rear = self.size
            self.size = self.size * 2

    def print_tab(self):
        print(self.tab)

    def __str__(self):
        if self.is_empty():
            string = '[]'
        else:
            idx = self.front
            string = '['
            while idx != (self.rear - 1) % self.size:
                string += '{}, '.format(self.tab[idx])
                idx = (idx + 1) % self.size
            string += '{}]'.format(self.tab[idx])
        return string


def main():
    queue = CyclicTab()
    for i in range(1, 5):
        queue.enqueue(i)
    print(queue.dequeue())
    print(queue.peek())
    print(queue)
    for i in range(5, 9):
        queue.enqueue(i)
    queue.print_tab()
    item = queue.dequeue()
    while item is not None:
        print(item)
        item = queue.dequeue()
    print(queue)


if __name__ == '__main__':
    main()
