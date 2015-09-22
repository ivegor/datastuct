class Queue:
    """
    data structure - queue  with max size
    base - list
    add to end O(1), remove from front O(n)
    """

    def __init__(self, max_size=0):
        self.max_size = max_size
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, *i):
        for item in i:
            if self.max_size and self.max_size <= self.size():
                self.dequeue()
                self.items.append(item)
            else:
                self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

    def m_size(self):
        if self.max_size:
            return self.max_size
        return None

    def __str__(self):
        return str(self.items)

    def __add__(self, other):
        self.enqueue(other)

    def __iter__(self):
        return iter(self.items)


if __name__ == '__main__':
    q1 = Queue(4)
    q1.enqueue(13,2)
    print(q1.dequeue())
    q1.enqueue(7)
    q1.enqueue(1)
    q1.enqueue(2,4)
    q1.enqueue(3)
    q1+2
    print(q1)
    print(2 in q1)


