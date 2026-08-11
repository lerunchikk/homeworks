def analyze_text(text):
    words = text.split()
    num_words = len(words)
    letters = len(text.replace(" ", ""))

    longest_word = words[0]
    shortest_word = words[0]
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
        if len(word) < len(shortest_word):
            shortest_word = word

    unique_words_set = set()
    for word in words:
        unique_words_set.add(word.lower())
    unique_words = len(unique_words_set)

    return {
        "words": num_words,
        "letters": letters,
        "longest_word": longest_word,
        "shortest_word": shortest_word,
        "unique_words": unique_words
    }

text = input("Введите предложение: ")
result = analyze_text(text)
print(result)