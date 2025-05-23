def convert(number):
    result = []
    if number % 3 == 0:
        result.append('Pling')
    if number % 5 == 0:
        result.append('Plang')
    if number % 7 == 0:
        result.append('Plong')

    if len(result) == 0:
        return str(number)
    else:
        return ''.join(result)

if __name__ == '__main__':
    print(convert(34))