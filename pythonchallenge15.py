def same_in_reverse():
    word = input("input word: ")
    reverse_word = "".join(reversed(word))
    if word == reverse_word:
        return True
    else:
        return False

print(same_in_reverse())
