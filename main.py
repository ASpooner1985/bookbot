from stats import count_words
from stats import count_letters
from stats import sorted_dict
import sys



def main():

    print(sys.argv)
    # get_books_text("books/frankenstein.txt")
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]
    sorted_dictionary = sorted_dict(count_letters(filepath))
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(count_words(filepath))
    print("--------- Character Count -------")
    for entry in sorted_dictionary:
        if entry["letter"].isalpha():
            print(f"{entry["letter"]}: {entry["count"]}")
    print("============= END ===============")




main()