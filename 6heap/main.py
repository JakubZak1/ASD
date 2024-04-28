class Node:
    def __init__(self, value, priority):
        self.__priorytet = priority
        self.__dane = value

    def __lt__(self, other):
        return self.__priorytet < other.__priorytet

    def __gt__(self, other):
        return self.__priorytet > other.__priorytet

    def __str__(self):
        return f"{self.__priorytet} : {self.__dane}"


class Queue:
    def __init__(self):
        self.queue = []
        self.size = 0

    def is_empty(self):
        if self.size == 0:
            return True
        return False

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.queue[0]

    def dequeue(self):
        if self.size == 0:
            return None
        else:
            item = self.peek()
            self.size -= 1
            self.queue[0] = self.queue[-1]
            self.queue = self.queue[:-1]
            self.heapify(0)
            return item

    def enqueue(self, node):
        self.queue.append(node)
        idx = self.size
        self.size += 1
        while idx > 0 and self.queue[self.parent(idx)] < self.queue[idx]:
            self.queue[idx], self.queue[self.parent(idx)] = self.queue[self.parent(idx)], self.queue[idx]
            idx = self.parent(idx)

    def heapify(self, idx):
        left_idx = self.left(idx)
        right_idx = self.right(idx)
        largest = idx
        if left_idx <= self.size - 1 and self.queue[left_idx] > self.queue[largest]:
            largest = left_idx
        if right_idx <= self.size - 1 and self.queue[right_idx] > self.queue[largest]:
            largest = right_idx
        if largest != idx:
            self.queue[idx], self.queue[largest] = self.queue[largest], self.queue[idx]
            self.heapify(largest)

    def left(self, idx):
        return 2 * idx + 1

    def right(self, idx):
        return 2 * idx + 2

    def parent(self, idx):
        return (idx - 1) // 2

    def print_tab(self):
        print('{', end=' ')
        print(*self.queue, sep=', ', end=' ')
        print('}')

    def print_tree(self, idx, lvl):
        if idx < self.size:
            self.print_tree(self.right(idx), lvl + 1)
            print(2 * lvl * '  ', self.queue[idx] if self.queue[idx] else None)
            self.print_tree(self.left(idx), lvl + 1)


if __name__ == "__main__":
    kopiec = Queue()
    priorytety = [7, 5, 1, 2, 5, 3, 4, 8, 9]
    wartosci = "GRYMOTYLA"
    for i in range(len(priorytety)):
        kopiec.enqueue(Node(wartosci[i], priorytety[i]))
    kopiec.print_tree(0, 0)
    kopiec.print_tab()
    dana = kopiec.dequeue()
    print(kopiec.peek())
    kopiec.print_tab()
    print(dana)
    while True:
        if not kopiec.is_empty():
            print(kopiec.dequeue())
        else:
            break
    kopiec.print_tab()
