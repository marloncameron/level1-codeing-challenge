longest = ["the", "quick", "brown", "fox", "ate", "my", "chickens", ]


def longest_word():
    max_len = -1
    for word in longest:
        if len(word) > max_len:
            max_len = len(word)
            res = word


    print("Maximum length string is : " + res)


longest_word()
