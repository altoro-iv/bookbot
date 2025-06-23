# Import function from stats.py into main.py
from stats import count_words
from stats import count_char
from stats import sort_char

# Take a file path and return as string
def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    book = get_book_text("books/frankenstein.txt")
    words = count_words(book)
    print("=========== BOOKBOT ===========")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count -----------")
    print("Found " + str(words) + " total words")

    # Create an empty list to store dictionary in
    char_list = []
    characters = count_char(book)

    # Loop through dicts to add into list skipping non alphabetic characters
    for key, value in characters.items():
        char_dict = {"char": key, "num": value}
        if key.isalpha() == True:
            char_list.append(char_dict)

    # Sorts the list from greatest to least
    char_list.sort(reverse=True, key=sort_char)

    print("--------- Character Count ---------")
    for char in char_list:
        print(f"{char['char']}: {char['num']}")

main()