# Import functions from stats module
from stats import split_book, char_count, sort_dict
import sys  # Import sys to access command-line arguments

# Function to read the contents of a book file
def get_book_test(path_to_file):
    try:
        # Attempt to open and read the file
        with open(path_to_file, "r") as f:
            file_contents = f.read()
        return file_contents  # Return file content as a string
    except FileNotFoundError:
        # Handle case where the file path is invalid or missing
        print(f"Error: File not found at {path_to_file}")
        return None
    except Exception as e:
        # Catch and print any other unexpected errors
        print(f"An error occurred: {e}")
        return None

# Main function to coordinate the analysis
def main():
    # Check if the user provided a file path as a command-line argument
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)  # Exit the program if no file path was given

    book_file_path = sys.argv[1]  # Get the file path from command-line arguments
    book_content = get_book_test(book_file_path)  # Read the book content

    # Analyze the book content using imported functions
    wc = split_book(book_content)              # Count total words
    char_dict = char_count(book_content)       # Count character frequencies
    sorted_dict = sort_dict(char_dict)         # Sort and format character count

    # Display the analysis results
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {wc} total words")
    print("--------- Character Count -------")
    print(f"{sorted_dict}")

# Run the main function
main()
