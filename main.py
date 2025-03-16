def get_book_text(filepath):
    #book = input("Book title: ")
    #pwd = filepath + book
    with open(filepath) as f:
        book_contents = f.read()
    return book_contents

def main():
    book_texts = get_book_text("books/frankenstein.txt")
    print(book_texts)

main() 
