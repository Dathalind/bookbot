def split_book(book):
    words = book.split()
    return len(words)

def char_count(book):
    new_dict = {}
    book = book.lower()
    for char in book:
        new_dict[char] = new_dict.get(char, 0) + 1
    return new_dict

def sort_dict(dict):
    return_list = []
    sorted_dict = sorted(dict.items(), key=lambda item: item[1], reverse=True)
    converted_list = [{"char": k, "num": v} for k, v in sorted_dict]
    for item in converted_list:
        char = item["char"]
        if char.isalpha():
            return_list.append(f"{char}: {item['num']}")
    return "\n".join(return_list)