__author__ = 'air'


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, new_data):
        self.data = new_data

    def set_next(self, new_next):
        self.next = new_next


class UnorderedList:

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def add(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.get_next()
        return count

    def search(self, item):
        if str(self.index(item)) == 'False':
            return False
        else:
            return True

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        try:
            while not found:
                if current.get_data() == item:
                    found = True
                else:
                    previous = current
                    current = current.get_next()
            if previous is None:
                self.head = current.get_next()
            else:
                previous.set_next(current.get_next())
        except AttributeError:
            print("no %s in list" % item)

    def append(self, item):
        if self.is_empty():
            self.add(item)
        else:
            current = self.head
            while current.get_next() is not None:
                current = current.get_next()
            temp = Node(item)
            current.set_next(temp)

    def insert(self, index, item):
        cur_index = 0
        current = self.head
        if index < 0:
            index = self.size() + index
            if index < 0:
                print("try another index")
                return False
        if index == 0:
            self.add(item)
        try:
            while cur_index < index:
                current = current.get_next()
                cur_index += 1
            temp = Node(item)
            temp.set_next(current.get_next())
            current.set_next(temp)
        except AttributeError:
            self.append(item)

    def index(self, item):
        current = self.head
        found = False
        index = 0
        while current is not None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()
                index += 1
        if found:
            return index
        else:
            return False

    def pop(self, index=None):
        current = self.head
        previous = None
        cur_index = 0
        while index is None or cur_index < index:
            if current.get_next() is None and index is None:
                if previous is None:
                    temp = current.get_data()
                    self.head = None
                    return temp
                else:
                    temp = current.get_data()
                    previous.set_next(None)
                    return temp
            cur_index += 1
            previous = current
            current = current.get_next()

        if previous is None:
            temp = current.get_data()
            self.head = current.get_next()
            return temp
        else:
            temp = current.get_data()
            previous.set_next(current.get_next())
            return temp


class OrderedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.get_next()
        return count

    def search(self,item):
        if str(self.index(item)) == 'False':
            return False
        else:
            return True

    def add(self,item):
        current = self.head
        previous = None
        while current is not None:
            if current.get_data() > item:
                break
            else:
                previous = current
                current = current.get_next()
        temp = Node(item)
        if previous == None:
            temp.set_next(self.head)
            self.head = temp
        else:
            temp.set_next(current)
            previous.set_next(temp)

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.get_data() == item:
                found = True
            elif current.get_data > item:
                print('no % in list' % item)
                return False
            else:
                previous = current
                current = current.get_next()
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

    def index(self, item):
        current = self.head
        found = False
        index = 0
        while current is not None and not found:
            if current.get_data() == item:
                found = True
            elif current.get_data > item:
                print('no % in list' % item)
                return False
            else:
                current = current.get_next()
                index += 1
        if found:
            return index
        else:
            return False

    def pop(self, index=None):
        current = self.head
        previous = None
        cur_index = 0
        while index is None or cur_index < index:
            if current.get_next() is None and index is None:
                if previous is None:
                    temp = current.get_data()
                    self.head = None
                    return temp
                else:
                    temp = current.get_data()
                    previous.set_next(None)
                    return temp
            cur_index += 1
            previous = current
            current = current.get_next()

        if previous is None:
            temp = current.get_data()
            self.head = current.get_next()
            return temp
        else:
            temp = current.get_data()
            previous.set_next(current.get_next())
            return temp

    def __str__(self):
        result =[]
        current = self.head
        while current is not None:
            result.append(current.get_data())
            current = current.get_next()
        return str(result)

if __name__ == '__main__':

    u1 = UnorderedList()
    u1.add(24)
    u1.add(9)
    u1.add(2)
    print(u1.size())
    print(u1.search(3))
    u1.remove(3)
    print(u1.size())
    u1.append(31)
    print(u1.size())
    u1.insert(3, 52)
    print(u1.size())
    u1.insert(5, 5)
    print(u1.index(5))
    print(u1.pop())
    print(u1.pop())
    print(u1.pop())

    o1 = OrderedList()
    o1.add(6)
    o1.add(4)
    o1.add(2)
    print(o1.size())
    print(o1.pop())
    print(o1)