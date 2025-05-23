def count_words(sentence):
    gap = """.:!?\t\n /"/"""
    words = {}
    prev = 0
    for i in range(len(sentence) - 1):
        if sentence[i] in gap:
            if (prev + 1) == i:
                prev += 1
            else:
                word = sentence[prev:i]
                prev = i + 1
                print(word)




if __name__ == '__main__':
    print(count_words("""That's the password: 'PASSWORD 123'!", cried the Special Agent.\nSo I fled."""))