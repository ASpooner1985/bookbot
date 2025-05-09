import sys

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)


def get_num_words():
    num_words = 0

    with open(sys.argv[1]) as f:
        file_contents = f.read()
        list_of_words = file_contents.split()
        num_words = num_words + len(list_of_words)

    print(f"Found {num_words} total words")


def count_letters():
    letter_dict = {}

    with open(sys.argv[1]) as f:
        file_contents = f.read()   
        for i in range (len(file_contents)):
            checkLetter = file_contents[i].lower()
            if checkLetter in letter_dict:
                letter_dict[checkLetter] += 1
            else:
                letter_dict[checkLetter] = 1
    
    return letter_dict

def sort_on(dict):
    return dict["num"]

def sort_chars(char_dict):
    chars_list = []
    for char, count in char_dict.items():
        if char.isalpha() and char != " ":
            char_data = {"char": char, "num": count}
            chars_list.append(char_data)

    return chars_list

def sort_on(dict):
    return dict["num"]

def statprint():

    get_num_words()
    letterDict = sort_chars(count_letters())
    letterDict.sort(key=sort_on, reverse=True)
    for entry in letterDict:
        print(f"{entry['char']}: {entry['num']}")
