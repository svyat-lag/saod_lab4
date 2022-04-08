import Stack

with open('files/Ex4-5.txt', 'r') as file:

    for line in file:
        text_string = line[:-1]

        # Creating stack
        balance = Stack.Stack()
        balance_broken = False

        # We're going throw symbols in each string. If the current symbol is '(',
        # we add it to the stack. If it's ')', we delete one from stack. If we're
        # trying to delete, but the stack is empty, we can say that balance is broken.
        for i in text_string:
            if i == "(":
                balance.push(i)
            elif i == ")":
                cur_symbol = balance.pop()
                if cur_symbol is None:
                    balance_broken = True
                    break

        # If the string is over but stack still has smth inside, then balance was broken
        if balance.size() != 0:
            balance_broken = True
            break

    if balance_broken:
        print("Balance is broken")
    else:
        print("Balance is fine")
