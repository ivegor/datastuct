__author__ = 'air'


class Stack:

    def __init__(self):
        self.elements = []

    def is_empty(self):
        return self.elements == []

    def add(self, other):
        self.elements.append(other)

    def remove(self):
        return self.elements.pop()

    def size(self):
        return len(self.elements)

    def peek(self):
        return self.elements[-1]

    def __str__(self):
        return str(self.elements)

if __name__ == '__main__':
    g1 = Stack()
    g1.add(12)
    g1.add(5)
    g1.add(7)
    g1.remove()
    print(g1)
    print(g1.peek())