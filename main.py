from stats import word_count, character_count, get_book_text,sort_clean_dictionary
import sys




def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python3 main.py <path_to_book>")
    
    file_path = sys.argv[1]
    content = get_book_text(file_path)

    lines = ["============ BOOKBOT ============",
         f"Analyzing book found at {file_path}...",
         "----------- Word Count ----------",
         f"Found {word_count(content)} total words",
         "--------- Character Count -------"]
    
    for line in lines:
        print(line)
    printable_dictionary = sort_clean_dictionary(character_count(content))
    for key,value in printable_dictionary.items():
        print(f"{key}: {value}")
    print("============= END ===============")

main()