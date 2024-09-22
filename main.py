def main():
    with open("books/frankenstein.txt", "r") as book:
        file_contents = book.read()
        print(file_contents)
main()
