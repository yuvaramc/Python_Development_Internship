def count_words():
    file_name = "sample.txt"

    with open(file_name, "r") as file:
        text = file.read()

    words = text.lower().split()

    word_count = {}

    for word in words:
        word_count[word] = word_count.get(word, 0) + 1

    print("Word Frequency:")

    for word in sorted(word_count):
        print(word, ":", word_count[word])


count_words()