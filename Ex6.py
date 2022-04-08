import Stack

# Function to check if the symbol is a number
def isdigit(string):
    for i in string:
        if i not in "1234567890":
            return False
    return True

# Function to check if the symbol is a letter
def isletter(string):
    string.lower()
    for i in string:
        if i not in "abcdefghijklmnopqrstuvwxyz":
            return False
    return True


with open('files/Ex6.txt', 'r') as file:

    # General stack is a stack for all characters in the text
    general_stack = Stack.Stack()

    # Here we have three stacks: The first one is for numbers,
    # the second onr is for letters, and the third one is for
    # other characters
    numbers_stack = Stack.Stack()
    letters_stack = Stack.Stack()
    symbols_stack = Stack.Stack()

    for line in file:
        text_string = line[:-1]

        # Firstly we're writing down all symbols to the general stack
        for symbol in text_string:
            general_stack.push(symbol)

    for i in range(general_stack.size()):
        cur_symbol = general_stack.pop()

        # Here we define to which category the current symbol belongs to
        if isdigit(cur_symbol):
            numbers_stack.push(cur_symbol)
        elif isletter(cur_symbol):
            letters_stack.push(cur_symbol)
        else:
            symbols_stack.push(cur_symbol)

    numbers_string = ""
    for i in range(numbers_stack.size()):
        numbers_string += numbers_stack.pop()
    print(numbers_string)

    letters_string = ""
    for i in range(letters_stack.size()):
        letters_string += letters_stack.pop()
    print(letters_string)

    symbols_string = ""
    for i in range(symbols_stack.size()):
        symbols_string += symbols_stack.pop()
    print(symbols_string)
