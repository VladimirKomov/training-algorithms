def is_isogram(string) -> bool:
    seen = set()
    for char in string.lower():
        if char.isalpha():
            if char in seen:
                return False
            seen.add(char)
    return True

def prtint_isogram():
    word_list = ["lumberjacks", "background", "downstream", "six-year-old"]
    for word in word_list:
         print(is_isogram(word))

prtint_isogram()