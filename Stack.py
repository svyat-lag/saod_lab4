class Stack:
    def __init__(self):
        self.list = []

    def is_empty(self):
        if self.list is []:
            return True
        else:
            return False

    def push(self, val):
        self.list.append(val)

    def pop(self):
        if len(self.list) == 0:
            return None
        else:
            temp = self.list[-1]
            del self.list[-1]
            return temp

    def size(self):
        return len(self.list)

    def print_stack(self):
        print(self.list)



# st = Stack()
# st.push(2)
# st.push(4)
# st.push(8)
# print(st.pop())
