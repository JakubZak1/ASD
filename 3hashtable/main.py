class HashTable:
    def __init__(self, size, c1=1, c2=0):
        self.tab = [None for i in range(size)]
        self.size = size
        self.c1 = c1
        self.c2 = c2

    def search(self, key):
        for elem in self.tab:
            if elem is not None:
                if elem.key == key:
                    return elem.value
        return None

    def insert(self, key, data):
        idx = self.hash(key)
        for elem in self.tab:
            if elem is not None:
                if elem.key == key:
                    self.tab[idx] = Elem(key, data)
        if (self.tab[idx] is None) or (self.tab[idx] == key) or (self.tab[idx].key is None):
            self.tab[idx] = Elem(key, data)
        else:
            new = self.insert_col(idx, key)
            if new is not None:
                self.tab[new] = Elem(key, data)
            else:
                print('Brak miejsca')
                return None

    def insert_col(self, idx, key):
        hk = self.hash(key)
        for i in range(1, self.size + 1):
            idx = (hk + self.c1 * i + self.c2 * i ** 2) % self.size
            if self.tab[idx] is None:
                return idx
        return None

    def remove(self, key):
        idx = self.hash(key)
        for elem in self.tab:
            if elem is not None:
                if elem.key == key:
                    self.tab[idx] = None
            else:
                print('Brak danej')
                return None

    def __str__(self):
        result = '{'
        for i in range(self.size - 1):
            # print(i)
            if self.tab[i] is not None and self.tab[i] != Elem(None, None):
                result = result + '{}'.format(self.tab[i].key) + ':{}, '.format(self.tab[i].value)
            else:
                result = result + 'None, '
        if self.tab[self.size-1] is not None and self.tab[self.size-1] != Elem(None, None):
            result = result + '{}'.format(self.tab[self.size-1].key) + ':{}, '.format(self.tab[self.size-1].value)
        result += '}'
        result = result.replace(', }', '}')
        return result

    def hash(self, key):
        if isinstance(key, str):
            idx = 0
            for character in key:
                idx += ord(character)
            return idx % self.size
        if isinstance(key, int):
            return key % self.size


class Elem:
    def __init__(self, key, value):
        self.key = key
        self.value = value


def main():
    tablica = HashTable(size=13)
    tablica.insert(1, 'A')
    tablica.insert(2, 'B')
    tablica.insert(3, 'C')
    tablica.insert(4, 'D')
    tablica.insert(5, 'E')
    tablica.insert(18, 'F')
    tablica.insert(31, 'G')
    tablica.insert(8, 'H')
    tablica.insert(9, 'I')
    tablica.insert(10, 'J')
    tablica.insert(11, 'K')
    tablica.insert(12, 'L')
    tablica.insert(13, 'M')
    tablica.insert(14, 'N')
    tablica.insert(15, 'O')
    print(tablica)
    print(tablica.search(5))
    print(tablica.search(14))
    tablica.insert(5, 'Z')
    tablica.remove(5)
    print(tablica)
    print(tablica.search(31))
    tablica.insert('test', 'W')
    print(tablica)

def test2():
    tablica = HashTable(size=13)
    tablica.insert(1 * 13, 'A')
    tablica.insert(2 * 13, 'B')
    tablica.insert(3 * 13, 'C')
    tablica.insert(4 * 13, 'D')
    tablica.insert(5 * 13, 'E')
    tablica.insert(6 * 13, 'F')
    tablica.insert(7 * 13, 'G')
    tablica.insert(8 * 13, 'H')
    tablica.insert(9 * 13, 'I')
    tablica.insert(10 * 13, 'J')
    tablica.insert(11 * 13, 'K')
    tablica.insert(12 * 13, 'L')
    tablica.insert(13 * 13, 'M')
    print(tablica)

    tablica1 = HashTable(size=13, c1=0, c2=1)
    tablica1.insert(1 * 13, 'A')
    tablica1.insert(2 * 13, 'B')
    tablica1.insert(3 * 13, 'C')
    tablica1.insert(4 * 13, 'D')
    tablica1.insert(5 * 13, 'E')
    tablica1.insert(6 * 13, 'F')
    tablica1.insert(7 * 13, 'G')
    tablica1.insert(8 * 13, 'H')
    tablica1.insert(9 * 13, 'I')
    tablica1.insert(10 * 13, 'J')
    tablica1.insert(11 * 13, 'K')
    tablica1.insert(12 * 13, 'L')
    tablica1.insert(13 * 13, 'M')
    print(tablica1)

    tablica2 = HashTable(size=13, c1=0, c2=1)
    tablica2.insert(1, 'A')
    tablica2.insert(2, 'B')
    tablica2.insert(3, 'C')
    tablica2.insert(4, 'D')
    tablica2.insert(5, 'E')
    tablica2.insert(18, 'F')
    tablica2.insert(31, 'G')
    tablica2.insert(8, 'H')
    tablica2.insert(9, 'I')
    tablica2.insert(10, 'J')
    tablica2.insert(11, 'K')
    tablica2.insert(12, 'L')
    tablica2.insert(13, 'M')
    tablica2.insert(14, 'N')
    tablica2.insert(15, 'O')
    print(tablica2)
    print(tablica2.search(5))
    print(tablica2.search(14))
    tablica2.insert(5, 'Z')
    tablica2.remove(5)
    print(tablica2)
    print(tablica2.search(31))
    tablica2.insert('test', 'W')
    print(tablica2)


if __name__ == '__main__':
    main()
    test2()
