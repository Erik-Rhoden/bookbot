def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    word_count = count_words(file_contents)
    char_count = count_char(file_contents)
    print(char_count)

def count_words(file_contents):
    count = 0
    words = file_contents.split()
    for word in words:
        count += 1
    return count

def count_char(file_contents):
    char_dict = {}
    lowercase_chars = file_contents.lower()
    for char in lowercase_chars:
        if char not in char_dict:
            char_dict[char] = 0
        char_dict[char] += 1
    return char_dict

main()