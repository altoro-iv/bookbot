# Take a file path and return as string
def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

# Takes the contents from the book to find how many words are in it
def count_words(book):
    text = book
    words = text.split()
    num_words = len(words)
    return num_words

def main():
    book = get_book_text("books/frankenstein.txt")
    words = count_words(book)
    print(str(words) + " words found in the document")

main()