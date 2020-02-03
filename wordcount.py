# put your code here.

def read_file(file):

    file_to_read = open(file)

    all_words = []
    for line in file_to_read:
        lines = line.strip()
        words = lines.split(' ')
        all_words.extend(words)

    print(all_words)
    for words in all_words:
        for letter in words:
            if letter in [',', '.', '!', '?', ':', ';']:
                print(words)
                words = words[0:-1]
                print(words)

    print(all_words)


    word_count = {}
    for word in all_words:
        word_count[word] = word_count.get(word, 0) + 1

    for word, count in word_count.items():
        print(f"{word} {count}") 

