# Takes the contents from the book to find how many words are in it
def count_words(book):
    text = book
    words = text.split()
    num_words = len(words)
    return num_words

# Takes the text from the book as a string and returns the number of times each character appears
def count_char(text): 
    char_count = {}
    for char in text:
        lowercase_char = char.lower()
        if lowercase_char in char_count:
            char_count[lowercase_char] += 1
        else:
            char_count[lowercase_char] = 1
    return char_count
    