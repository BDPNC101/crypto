from helper import alphabet_position, rotate_character

def encrypt(text, rot):
    new_string = ""
    for char in text:
        new_string += rotate_character(char, rot)
    return new_string

def main():
    from sys import argv
    text_ = input("What would you like to Encrypt? > ")
    print(encrypt(text_, argv[1]))

if __name__ == "__main__":
    main()
