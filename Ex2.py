import Deque

text = Deque.Deque()
key = Deque.Deque()
decoded_text = Deque.Deque()

alphabet = "abcdefghijklmnopqrstuvwxyz"
for i in alphabet:
    key.add_last(i)

print("\n" + "====Lyrics================")

with open('files/Ex2.txt', 'r') as file:
    # Filling the deque with content from file
    for line in file:
        text_string = line[:-1]
        for i in text_string:
            text.add_last(i)

        # We're going throw the text and picking up the symbols
        for i in range(text.size()):
            text_symbol = text.remove_first()
            if text_symbol in [" ", "'", ",", "?"]:
                decoded_text.add_last(text_symbol)
                continue
            # We're searching for the needed symbol in keys
            while True:
                key_symbol = key.remove_last()
                # If the key-symbol is the same as the text one,
                # we should "turn the wheel" twice
                if key_symbol != text_symbol:
                    key.add_first(key_symbol)
                else:
                    key.add_first(key_symbol)
                    # (   the following two lines of code move the symbol
                    #     from the end of the deque to the start of it     )
                    key_symbol = key.remove_last()
                    key.add_first(key_symbol)
                    decoded_text.add_last(key.get_last())
                    break

        res_string = ""
        for i in range(decoded_text.size()):
            res_string += decoded_text.remove_first()

        print(res_string)