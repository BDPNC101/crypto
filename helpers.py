def alphabet_position(letter):
    # receives a letter and returns the 0-based numerical 
    # position of that letter within the alphabet.
    ordinal_of_letter = ord(letter)
    if 90 >= ordinal_of_letter >= 65:
        return ordinal_of_letter - 65 
    return ordinal_of_letter - 97

def rotate_character(char, rot):
    if char.isalpha():
        char_value = alphabet_position(char)
        new_char_value = (char_value + int(rot)) % 26
        if 90 >= ord(char) >= 65:
            return chr(new_char_value + 65)
        return chr(new_char_value + 97)
    return char
