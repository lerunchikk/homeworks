def longest_word(text):
    new_text = text.split()
    print(new_text)
    max_lenght = new_text[0]
    print(max_lenght)
    for word in new_text[1:]:
     if len(max_lenght )< len(word):
        max_lenght = word
    return max_lenght
print(longest_word("Были у бабуси два веселых гуся"))
