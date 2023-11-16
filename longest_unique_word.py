import json

with open('dictionary_compact.json', 'r') as json_file:
    data = json.load(json_file)
    unique_words = []
    for word in data.keys():
        is_unique = 0
        for i in range(len(word)):
            for i2 in range(len(word)):
                if i != i2:
                    if word[i] == word[i2]:
                        is_unique = 1
        if is_unique == 0:
            unique_words.append(word)

    longest_unique_word = ""
    for word in unique_words:
        if len(word) > len(longest_unique_word):
            longest_unique_word = word
    
    print(longest_unique_word)

