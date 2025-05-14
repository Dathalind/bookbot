# Function to count the number of words in the book
def split_book(book):
    words = book.split()  # Split the book string into words using whitespace
    return len(words)     # Return the number of words

# Function to count the frequency of each character in the book
def char_count(book):
    new_dict = {}         
    book = book.lower()   # Convert the entire book string to lowercase
    for char in book:     
        # Update the character count using get() to handle new characters
        new_dict[char] = new_dict.get(char, 0) + 1
    return new_dict        # Return the dictionary of character counts

# Function to sort the character frequency dictionary and return a formatted string
def sort_dict(dict):
    return_list = []
    # Sort dictionary items by frequency in descending order
    sorted_dict = sorted(dict.items(), key=lambda item: item[1], reverse=True)
    # Convert each key-value pair into a dictionary with keys "char" and "num"
    converted_list = [{"char": k, "num": v} for k, v in sorted_dict]
    for item in converted_list:
        char = item["char"]
        # Only include alphabetic characters in the result
        if char.isalpha():
            return_list.append(f"{char}: {item['num']}")
    # Join the formatted strings into one string with line breaks
    return "\n".join(return_list)
