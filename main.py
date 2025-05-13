from stats import split_book, char_count, sort_dict
import sys

def get_book_test(path_to_file):
    try:
        with open(path_to_file, "r") as f:
            file_contents = f.read()
        return file_contents
    except FileNotFoundError:
        print(f"Error: File not found at {path_to_file}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_file_path = sys.argv[1]
    book_content = get_book_test(book_file_path)
    wc = split_book(book_content)
    char_dict = char_count(book_content)
    sorted_dict = sort_dict(char_dict)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {wc} total words")
    print("--------- Character Count -------")
    print(f"{sorted_dict}")

main()