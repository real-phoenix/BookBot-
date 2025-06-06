import sys
from stats import get_num_words, count_chars

def main(): 
    # file_path = "/Users/shreyasingh/BookBot-/books/frankenstein.txt"
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_path = sys.argv[1]
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(file_path)} total words")
    print("--------- Character Count -------")
    count_chars(file_path)
    print("============= END ===============")

if __name__ =="__main__": 
    main()