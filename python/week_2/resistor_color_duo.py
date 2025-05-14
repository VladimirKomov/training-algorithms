code = {
    "black": "0",
    "brown": "1",
    "red": "2",
    "orange": "3",
    "yellow": "4",
    "green": "5",
    "blue": "6",
    "violet": "7",
    "grey": "8",
    "white": "9"
}

def value(colors):
    return int(code[colors[0]] + code[colors[1]])

if __name__ == '__main__':
    colors = ["brown", "green", "black"]
    print(value(colors))