from stats import count_words, sorted_dictionary

#Read contents within file 
def get_book_text(filepath):
    #book = input("Book title: ")
    #pwd = filepath + book
    with open(filepath) as f:
        book_contents = f.read()
    return book_contents

def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path) 
    num_words = count_words(book_text)
    # print(f"{num_words} words found in the document")
    character_count = sorted_dictionary(book_text)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    
    for char, count in character_count:
        print(f"{char}: {count}")

    print("============= END ===============")


main()
