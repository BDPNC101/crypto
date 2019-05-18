from helper import alphabet_position, rotate_character

def encrypt(text, key):
    #(1) break key in series of rot commands
    key_list = []
    if 0 == len(text) % len(key):
        key = key * int(len(text)/len(key) + 1)
    else:
        key = key * ((len(text)//len(key)) + 1)
        for j in range(len(text) % len(key)):
            key += key[j]

    char_counter = 0
    crypt_mess = ""
    for char in text:
        if char.isalpha():
            a = rotate_character(char, alphabet_position(key[char_counter]))
            crypt_mess += a
            char_counter += 1
        else:
            crypt_mess += char
    return crypt_mess

def main():
    from sys import argv
    text_input = input("Type a message: ")
    print(encrypt(text_input, argv[1]))
    return encrypt(text_input, argv[1])

if __name__ == '__main__':
    main()
