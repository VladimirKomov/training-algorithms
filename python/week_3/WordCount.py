import re


def count_words(sentence):
    words = {}
    templet = r"[a-z0-9]+"

    for word in re.findall(templet, sentence.lower()):
        words[word] = words.get(word, 0) + 1

    return words


if __name__ == '__main__':
    print(count_words("'First: don't laugh. Then: don't cry. You're getting it.'"))