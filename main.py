from stats import count_characters

#Read contents within file 
def get_book_text(filepath):
    #book = input("Book title: ")
    #pwd = filepath + book
    with open(filepath) as f:
        book_contents = f.read()
    return book_contents

def main():
    book_text = get_book_text("books/frankenstein.txt") 
    # num_words = count_words(book_text)
    # print(f"{num_words} words found in the document")
    x = count_characters(book_text)
    print(x)

main()
