def two_fer(name='you'):
    return f'One for {name}, one for me.'


if __name__ == '__main__':
    print(two_fer())
    print(two_fer('<NAME>'))