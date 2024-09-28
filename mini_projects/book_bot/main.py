def get_book_text(path):
    with open(path) as file:
        return file.read()
    
def count_words(text):
    words = text.split()
    return len(words)

def count_chars(text):
    chars = {}
    for c in text:
        c_lower = c.lower() # Convert to lowercase
        if c_lower in chars:
            chars[c_lower] += 1
        else:
            chars[c_lower] = 1
    return chars

def sort_chars(chars_dict):
    sorted_chars = [] 
    for key in chars_dict: # Key is the char itself: Sample dictionary: {"a": 10, "b": 5}
        sorted_chars.append({"char": key, "count": chars_dict[key]})
    sorted_chars.sort(key=lambda x: x["count"], reverse=True)
    return sorted_chars # List of dictionaries: [{"char": "a", "count": 10}, {"char": "b", "count": 5}]
    
    

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = count_words(text)
    chars_dict = count_chars(text)
    sorted_chars = sort_chars(chars_dict)

    print(f"Report of {book_path}")
    print(f"Word count: {word_count}")
    
    for item in sorted_chars:
        if not item["char"].isalpha(): # Skip non-alphabetic characters
            continue
        print(f"The '{item['char']}' character was found {item['count']} times")

main()