import Stack

with open('files/Ex8.txt', 'r') as file:

    # General deque is a deque for all numbers in the text
    general_stack = Stack.Stack()

    for line in file:
        text_string = line[:-1].split(' ')

        for word in text_string:
            general_stack.push(word)

    string = ''
    for i in range(general_stack.size()):
        string += general_stack.pop()
        string += ' '

    with open('files/Ex8_test.txt', 'w') as f:
        f.write(string)
