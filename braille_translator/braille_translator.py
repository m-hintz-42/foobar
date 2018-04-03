def braille_translate(plaintext):
    """
    Translation of characters to 6 digit Braille representation. Read left to right as position 1 - 6
    with a 1 representing a raised dot.

    """
    out_string = ''
    braille_alphabet = {'a': '1', 'b': '12', 'c': '14', 'd': '145', 'e': '15', 'f': '124', 'g': '1245',
                        'h': '125', 'i': '24', 'j': '245', 'k': '13', 'l': '123', 'm': '134', 'n': '1345',
                        'o': '135', 'p': '1234', 'q': '12345', 'r': '1235', 's': '234', 't': '2345', 'u': '136',
                        'v': '1236', 'w': '2456', 'x': '1346', 'y': '13456', 'z': '1356'}
    for char in plaintext:
        return_string = ''
        base_string = '000000'
        base_list = list(base_string)
        upper_string = '000001'

        if char == ' ':
            out_string += base_string
            continue
        if char == char.upper():
            out_string += upper_string

        for each in range(0, len(braille_alphabet[char.lower()])):
            base_list[int(braille_alphabet[char.lower()][each]) - 1] = '1'
            return_string = ''.join(base_list)
        out_string += return_string

    return(out_string)


print(braille_translate('Braille'))
