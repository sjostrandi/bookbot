
def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def word_count(content):
    split_content = content.split()
    return len(split_content)

def character_count(content):
    char_count = {}
    for char in content.lower():
        if char not in char_count:
            char_count[char] = 1
        elif char in char_count:
            char_count[char] = char_count[char] + 1
    return char_count


def sort_clean_dictionary(sample):
    legal_dictionary = {}
    for key,value in sample.items():
        if key.isalpha() == True:
            legal_dictionary[key] = value

    sorted_dictionary = dict(sorted(legal_dictionary.items(), key=lambda item: item[1], reverse=True))
    return sorted_dictionary