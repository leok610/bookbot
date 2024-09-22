
def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    print(words_in_string(book_text))

def get_book_text(path):
    with open(path, "r") as book:
        file_contents = book.read()
        return file_contents

def words_in_string(text):
    words = text.split()
    return len(words)

main()
