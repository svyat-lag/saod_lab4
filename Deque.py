class Deque:
    def __init__(self):
        self.list = []

    def add_first(self, val):
        self.list = [val] + self.list[:]

    def add_last(self, val):
        self.list = self.list[:] + [val]

    def remove_first(self):
        if self.list is not []:
            temp = self.list[0]
            self.list = self.list[1:]
            return temp
        else:
            print("Stack is empty.")

    def remove_last(self):
        if self.list is not []:
            temp = self.list[-1]
            self.list = self.list[:-1]
            return temp
        else:
            print("Stack is empty.")

    def get_first(self):
        if self.list is not []:
            return self.list[0]
        else:
            print("Stack is empty.")

    def get_last(self):
        if self.list is not []:
            return self.list[-1]
        else:
            print("Stack is empty.")

    def size(self):
        return len(self.list)

    def is_empty(self):
        if self.list is []:
            return True
        else:
            return False


# deq = Deque()
# deq.add_first(1)
# deq.add_first(4)
# deq.add_last(5)
# deq.remove_last()
# deq.remove_first()
# c = 1
