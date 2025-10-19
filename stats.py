from helper import get_books_text

def count_words(filepath):
    text = get_books_text(filepath) 
    print(f"Found {len(text.split())} total words")

def count_letters(filepath):
    text = get_books_text(filepath).lower()
    letter_dict = {}
    for i in range(len(text)):
        if text[i] not in letter_dict:
            letter_dict[text[i]] = 1
        else:
            letter_dict[text[i]]+=1

    return letter_dict


def sorted_dict(import_dict):
    new_List = []
    for entry in import_dict:
        new_dict = {}
        new_dict["letter"] = entry
        new_dict["count"] = import_dict[entry]
        new_List.append(new_dict)

    new_List.sort(reverse = True, key = sort_helper)

    return new_List

def sort_helper(import_dict):
    return import_dict["count"]


    