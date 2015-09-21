class BinaryHeap:

    def __init__(self):
        self.heap_list = [0]
        self.current_size = 0

    def is_empty(self):
        return not self.current_size

    def size(self):
        return len(self.heap_list)-1

    def perc_up(self, i):
        while i // 2 > 0:
            if self.heap_list[i] < self.heap_list[i // 2]:
                self.heap_list[i], self.heap_list[i // 2] = \
                    self.heap_list[i // 2], self.heap_list[i]
            i //= 2

    def insert(self, item):
        self.heap_list.append(item)
        self.current_size += 1
        self.perc_up(self.current_size)

    def perc_down(self, i):
        while (i * 2) <= self.current_size:
            mc = self.min_child(i)
            if self.heap_list[i] > self.heap_list[mc]:
                self.heap_list[i], self.heap_list[mc] = \
                    self.heap_list[mc], self.heap_list[i]
            i = mc

    def min_child(self, i):
        if i * 2 + 1 > self.current_size:
            return i * 2
        else:
            if self.heap_list[i*2] < self.heap_list[i*2+1]:
                return i * 2
            else:
                return i * 2 + 1

    def del_min(self):
        temp = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.current_size]
        self.current_size -= 1
        self.heap_list.pop()
        self.perc_down(1)
        return temp

    def build_heap(self, list):
        i = len(list) // 2
        self.current_size = len(list)
        self.heap_list = [0] + list[:]
        while i > 0:
            self.perc_down(i)
            i -= 1

    def __str__(self):
        if self.is_empty():
            return str("Heap is empty")
        i = 1
        temp = []
        count=1
        while i <= self.current_size:
            temp.append("\n%s%slvl   %s" % ('\t'*count, count, str(self.heap_list[i])))
            for item in self.heap_list[i+1:i*2]:
                temp.append(' '+str(item))
            i *= 2
            count += 1
        return str(''.join(temp))

    def __repr__(self):
        return str(self.heap_list)

if __name__ == "__main__":
    from random import shuffle
    l = [i for i in range(70)]
    shuffle(l)
    heap = BinaryHeap()
    print(heap)
    for i in l:
        heap.insert(i)
    print(heap)
