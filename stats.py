#Counting number of words within file
def count_words(book_text):
    words = book_text.split()
    number = len(words)
    return number

def count_characters(book_text):
    #list_of_words = count_words(book_text)
    joined = ""
    for character in book_text:
        joined += character.lower()
    if len(joined) != 0:
        joined = joined[:-1]
        
        every_character = list(joined)

        counter = {}

        for char in every_character:
            if char in counter:
                counter[char] += 1 
            else:
                counter[char] = 1 
        return counter

def sorted_dictionary(book_text):
    unsorted_dict = count_characters(book_text)

    sorted_list = sorted(unsorted_dict.items(), key=lambda item: item[1], reverse=True)
    return sorted_list
        
    



