s = input()

# string import method
import string


def count_words_string(word):
    count = 1
    for letter in word:
        if letter in string.ascii_uppercase:
            count += 1
    return count


# ord method
def count_words_ord(word):
    count = 1
    for letter in word:
        if ord(letter) >= 65 and ord(letter) <= 90:
            count += 1
    return count


print(count_words_ord(s))
# print(count_words_string(s))