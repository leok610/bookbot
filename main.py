import string

test_list = [(0,1),(1,2)]
def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    characters_dict = char_occurrences(book_text)
    occurrences = reverse_sort_occurrences(characters_dict)
    print(f"--- Begin report of {book_path} ---")
    print(f"{words_in_string(book_text)} words found in the document\n\n")
    character_report(occurrences)
    print("--- End report ---")

def get_book_text(path):
    with open(path, "r") as book:
        file_contents = book.read()
        return file_contents

def words_in_string(text):
    words = text.split()
    return len(words)

def char_occurrences(input):
    """Stores in a dictionary how many times each letter in a string appears"""
    input = input.lower()
    chars = {}
    for char in input:
        if char in set(string.ascii_lowercase):
            if char in set(chars.keys()):
                chars[char] += 1
            else:
                chars[char] = 1
    return chars

def reverse_sort_occurrences(paired_data):
    data = list(paired_data.items())
    # Use a lambda to look at the second item in each pair
    data.sort(reverse=True, key=lambda x: x[1])
    return data

def character_report(input):
    for pair in input:
        print(f"The '{pair[0]}' character was found {pair[1]} times")

main()
