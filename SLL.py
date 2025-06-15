#Assignment 2:--

class Node:
    def __init__(self, val):
        self.val = val
        self.nxt = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new = Node(data)
        if self.head is None:
            self.head = new
            return
        walker = self.head
        while walker.nxt:
            walker = walker.nxt
        walker.nxt = new

    def prepend(self, data):
        node = Node(data)
        node.nxt = self.head
        self.head = node

    def insert_after(self, target, data):
        curr = self.head
        while curr:
            if curr.val == target:
                node = Node(data)
                node.nxt = curr.nxt
                curr.nxt = node
                return
            curr = curr.nxt
        raise Exception("Target not found")

    def remove_nth(self, pos):
        if self.head is None:
            raise Exception("Empty list")
        if pos <= 0:
            raise Exception("Position should be >= 1")
        if pos == 1:
            self.head = self.head.nxt
            return
        idx = 1
        curr = self.head
        while curr and idx < pos - 1:
            curr = curr.nxt
            idx += 1
        if curr is None or curr.nxt is None:
            raise Exception("Position out of bounds")
        curr.nxt = curr.nxt.nxt

    def delete_first(self):
        if self.head:
            self.head = self.head.nxt

    def delete_last(self):
        if self.head is None:
            return
        if self.head.nxt is None:
            self.head = None
            return
        curr = self.head
        while curr.nxt.nxt:
            curr = curr.nxt
        curr.nxt = None

    def remove_val(self, value):
        if self.head is None:
            return
        if self.head.val == value:
            self.head = self.head.nxt
            return
        curr = self.head
        while curr.nxt:
            if curr.nxt.val == value:
                curr.nxt = curr.nxt.nxt
                return
            curr = curr.nxt

    def show(self):
        ptr = self.head
        while ptr:
            print(ptr.val, end=" -> " if ptr.nxt else "\n")
            ptr = ptr.nxt

    def size(self):
        cnt = 0
        ptr = self.head
        while ptr:
            cnt += 1
            ptr = ptr.nxt
        return cnt

    def find(self, value):
        ptr = self.head
        idx = 1
        while ptr:
            if ptr.val == value:
                return idx
            ptr = ptr.nxt
            idx += 1
        return -1

    def __iter__(self):
        self._curr = self.head
        return self

    def __next__(self):
        if self._curr is None:
            raise StopIteration
        result = self._curr.val
        self._curr = self._curr.nxt
        return result

# Example use
chain = LinkedList()
chain.append(10)
chain.append(20)
chain.append(30)
chain.append(40)
chain.prepend(5)
chain.insert_after(20, 25)
chain.show()

chain.remove_nth(3)
chain.show()

chain.remove_val(25)
chain.show()

chain.delete_first()
chain.delete_last()
chain.show()

print("Found 30 at:", chain.find(30))
print("Total nodes:", chain.size())

for val in chain:
    print("Next item:", val)
