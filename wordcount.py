# put your code here.
file_to_read = open("test.txt")

all_words = []
for line in file_to_read:
    lines = line.strip()
    words = lines.split(' ')
    all_words.extend(words)


word_count = {}
for word in all_words:
    word_count[word] = word_count.get(word, 0) + 1

for word, count in word_count.items():
    print(f"{word} {count}") 