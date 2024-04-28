import random
import time


class Node:
    def __init__(self, priority, value=None):
        self.__priorytet = priority
        self.__dane = value

    def __lt__(self, other):
        return self.__priorytet < other.__priorytet

    def __gt__(self, other):
        return self.__priorytet > other.__priorytet

    def __repr__(self):
        return f"{self.__priorytet} : {self.__dane}"


class Queue:
    def __init__(self, elements=None):
        if elements is None:
            self.queue = []
            self.size = 0
        else:
            self.queue = elements
            self.size = len(self.queue)
        for i in range(self.parent(len(self.queue)), -1, -1):
            self.heapify(i)

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
        if self.is_empty():
            return None
        result = self.peek()
        self.size -= 1
        self.queue[0], self.queue[self.size] = self.queue[self.size], self.queue[0]
        self.heapify(0)
        return result

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


def swap_sort(lst):
    for i in range(len(lst)):
        min = i
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[min]:
                min = j
        lst[i], lst[min] = lst[min], lst[i]
    return lst

def shift_sort(lst):
    for i in range(len(lst)):
        min = i
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[min]:
                min = j
        elem = lst.pop(min)
        lst.insert(i, elem)
    return lst


if __name__ == "__main__":
    dane = [(5,'A'), (5,'B'), (7,'C'), (2,'D'), (5,'E'), (1,'F'), (7,'G'), (5,'H'), (1,'I'), (2,'J')]
    elements = []
    for element in dane:
        elements.append(Node(element[0], element[1]))
    queue = Queue(elements)
    queue.print_tab()
    queue.print_tree(0, 0)

    while not queue.is_empty():
        queue.dequeue()
    queue.print_tab() # jest stabilne

    dane1 = [int(random.random() * 100) for _ in range(10000)]
    t_start = time.perf_counter()

    queue1 = Queue(dane1)
    while not queue1.is_empty():
        queue1.dequeue()

    t_stop = time.perf_counter()
    print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))

    dane2 = [int(random.random() * 100) for _ in range(10000)]

    dane_swap = dane2.copy()
    dane_shift = dane2.copy()

    t_start = time.perf_counter()
    swap_sort(dane_swap)
    t_stop = time.perf_counter()
    print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))

    t_start = time.perf_counter()
    shift_sort(dane_shift)
    t_stop = time.perf_counter()
    print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))
