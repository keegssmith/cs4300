def count_words(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        file_text = file.read() # read all file_text in file
    word_count = file_text.split() # splits the file_text into seperate words and counts them
    return len(word_count)

print(count_words("task6_read_me.txt"))