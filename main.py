# Import function from stats.py into main.py
from stats import count_words
from stats import count_char
# Take a file path and return as string
def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    book = get_book_text("books/frankenstein.txt")
    words = count_words(book)
    print(str(words) + " words found in the document")
    char = count_char(book)
    print(str(char))

main()