#Counting number of words within file
def count(book_text):
    words = book_text.split()
    number = len(words)
    return number