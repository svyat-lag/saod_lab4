import Deque

with open('files/Ex7.txt', 'r') as file:

    # General deque is a deque for all numbers in the text
    general_stack = Deque.Deque()

    # Here we have two deque: The first one is for positive
    # numbers, and the second one is for negatives
    positive_numbers_stack = Deque.Deque()
    negative_numbers_stack = Deque.Deque()

    for line in file:
        text_string = line[:-1].split(' ')

        # Firstly we're writing down all numbers to the general deque
        for number in text_string:
            general_stack.add_first(number)

    for i in range(general_stack.size()):
        cur_number = general_stack.remove_first()

        # Here we define to which category the current number belongs to
        if int(cur_number) >= 0:
            positive_numbers_stack.add_first(cur_number)
        else:
            negative_numbers_stack.add_first(cur_number)

    positive_numbers_string = ""
    for i in range(positive_numbers_stack.size()):
        positive_numbers_string += positive_numbers_stack.remove_first()
        positive_numbers_string += " "
    print(positive_numbers_string)

    negative_numbers_string = ""
    for i in range(negative_numbers_stack.size()):
        negative_numbers_string += negative_numbers_stack.remove_first()
        negative_numbers_string += " "
    print(negative_numbers_string)
