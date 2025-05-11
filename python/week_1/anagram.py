def find_anagrams(word, candidates):
    word_lower = word.lower()
    sorted_word = sorted(word_lower)
    anagrams = []

    for candidate in candidates:
        normalized = candidate.lower()
        if word_lower == normalized:
            continue
        if sorted(normalized) == sorted_word:
            anagrams.append(candidate)

    return anagrams


def print_result():
    word = 'stone'
    candidates = ['stone', 'tones', 'banana', 'tons', 'notes', 'Seton']
    print(find_anagrams(word, candidates))

if __name__ == '__main__':
    print_result()