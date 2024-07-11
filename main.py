def main():
    book = "books/frankenstein.txt"
    with open(book) as f:
        file_contents = f.read()
    word_count = count_words(file_contents)
    char_count = count_char(file_contents)
    dict_list = convert_dict(char_count)
    dict_list.sort(reverse=True, key=sort_on)
    print(f"--- Begin report of {book} ---")
    print(f"{word_count} words found in the document\n")
    for dict in dict_list:
        letter, count = dict['letter'], dict['count']
        print(f"The '{letter}' character was found '{count}' times")
    print(f"--- End report ---")


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

def convert_dict(char_count):
    dict_list = []
    for key, value in char_count.items():
        if key.isalpha():
            dict_list.append({'letter': key, 'count': value})
    return dict_list

def sort_on(dict_list):
    return dict_list["count"]

main()