class EmptyListException(Exception):
    def __init__(self, message="The list is empty."):
        super().__init__(message)


class Node:
    def __init__(self, value):
        self._value = value
        self._next = None

    def value(self):
        return self._value

    def next(self):
        return self._next



class LinkedList:
    def __init__(self, values=None):
        self._head = None
        self._length = 0
        if values:
            for value in values:
                self.push(value)


    def __iter__(self):
        current = self._head
        while current:
            yield current.value()
            current = current.next()

    def __len__(self):
        return self._length

    def head(self):
        if self._head is None:
            raise EmptyListException()
        return self._head

    def push(self, value):
        new_nod = Node(value)
        new_nod._next = self._head
        self._head = new_nod

        print(self._head.value(), self._head.next())
        self._length += 1


    def pop(self):
        if self._head is None:
            raise EmptyListException()

        removed_nod = self._head
        self._head = self._head.next()
        self._length -= 1
        return removed_nod.value()

    def reversed(self):
        new_list = LinkedList()
        for i in self:
            new_list.push(i)
        return new_list

def print_result():
    values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    linked_list = LinkedList(values)
    length = len(linked_list)
    print(length)
    for i in linked_list:
        print(i)
    for i in linked_list.reversed():
        print(i)

if __name__ == '__main__':
    print_result()