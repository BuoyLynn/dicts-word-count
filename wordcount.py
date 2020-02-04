# put your code here.

def read_file(file):

    file_to_read = open(file)

# read strip and split text file into a set of words.
    
    all_words = []
    for line in file_to_read:
        lines = line.strip()
        words = lines.split(' ')
        all_words.extend(words)


# Remove all punctuations to the words
    punctuations = [',', '.', '!', '?', ':', ';']
    for words in all_words:
        for letter in words:
            if letter in punctuations:
                words = words[0:-1]
                all_words.append(words)
    

    print(all_words)

# Parse through list of words and add counter
    word_count = {}
    for word in all_words:
        word_count[word] = word_count.get(word, 0) + 1

    for word, count in word_count.items():
        print(f"{word} {count}") 

