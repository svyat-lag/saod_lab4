import Deque

deque = Deque.Deque()
res_deque = Deque.Deque()
with open('files/Ex1.txt', 'r') as file:
    # Filling the deque with content from file
    for line in file:
        deque.add_last(line[:-1])

    #   Imagine if our deque is a wheel, so we can connect
    # the beginning with the end  Then we can compare the
    # first and the last elements. We should "turn" the wheel
    # every time after we compared two elements.
    #   When the wheel makes a full turn, the minimum element
    # is at the end of the deque. We should move it to the
    # second deque.
    #   At the end first deque will contain only one element,
    # and we should move it to the second deque without comparing.
    for i in range(deque.size()-1):
        for j in range(deque.size()):
            el1 = deque.remove_first()
            el2 = deque.remove_last()
            if el1 > el2:
                deque.add_last(el1)
                deque.add_last(el2)
            else:
                deque.add_last(el2)
                deque.add_last(el1)
        res_deque.add_last(deque.remove_last())
    res_deque.add_last(deque.remove_last())

    for i in range(res_deque.size()):
        print("{}) {}".format(i+1, res_deque.remove_first()))
