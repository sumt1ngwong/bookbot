#Read contents within file 
def get_book_text(filepath):
    #book = input("Book title: ")
    #pwd = filepath + book
    with open(filepath) as f:
        book_contents = f.read()
    return book_contents

def count(book_text):
    words = book_text.split()
    number = len(words)
    return number

def main():
    book_text = get_book_text("books/frankenstein.txt") 
    num_words = count(book_text)
    print(f"{num_words} words found in the document")

main()
