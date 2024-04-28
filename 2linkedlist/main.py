class ListaWiazana:
    def __init__(self):
        self.head = None

    def destroy(self):
        self.head = None

    def add(self, data):
        tmp = self.head
        self.head = Wezel(data, next)
        self.head.next = tmp

    def append(self, data):
        new = Wezel(data, next=None)
        if self.is_empty():
            self.head = new
        else:
            tmp = self.head
            while tmp.next is not None:
                tmp = tmp.next
            tmp.next = new

    def remove(self):
        if not self.is_empty():
            self.head = self.head.next

    def remove_end(self):
        if not self.is_empty():
            prev = self.head
            tmp = self.head
            while tmp.next is not None:
                prev = tmp
                tmp = tmp.next
            prev.next = None

    def is_empty(self):
        if self.length() == 0:
            return True
        else:
            return False

    def length(self):
        counter = 0
        tmp = self.head
        while tmp is not None:
            tmp = tmp.next
            counter += 1
        return counter

    def get(self):
        return self.head.data

    def __str__(self):
        string = ""
        tmp = self.head
        for _ in range(self.length()):
            string += "-> "
            string += "".join(str(tmp.data)) + "\n"
            tmp = tmp.next
        return string


class Wezel:
    def __init__(self, data, next):
        self.data = data
        self.next = next


def main():
    wszystkie = [('AGH', 'Kraków', 1919),
                ('UJ', 'Kraków', 1364),
                ('PW', 'Warszawa', 1915),
                ('UW', 'Warszawa', 1915),
                ('UP', 'Poznań', 1919),
                ('PG', 'Gdańsk', 1945)]

    uczelnie = ListaWiazana()
    uczelnie.append(wszystkie[0])
    uczelnie.append(wszystkie[1])
    uczelnie.append(wszystkie[2])
    uczelnie.add(wszystkie[3])
    uczelnie.add(wszystkie[4])
    uczelnie.add(wszystkie[5])
    print(uczelnie)
    print(uczelnie.length())
    uczelnie.remove()
    print("\n", uczelnie.get(), "\n")
    uczelnie.remove_end()
    print(uczelnie)
    uczelnie.destroy()
    uczelnie.remove()
    uczelnie.remove_end()


if __name__ == '__main__':
    main()
