def check(sides):
    if len(sides) != 3:
        return False

    a = sides[0]
    b = sides[1]
    c = sides[2]

    if (a + b > c) and (b + c > a) and (a + c > b):
        return True
    else:
        return False


def equilateral(sides):
    if not check(sides):
        return False
    if len(set(sides)) == 1:
        return True
    else:
        return False


def isosceles(sides):
    if not check(sides):
        return False
    if len(set(sides)) <= 2:
        return True
    else:
        return False


def scalene(sides):
    if not check(sides):
        return False
    if len(set(sides)) == 3:
        return True
    else:
        return False



if __name__ == '__main__':
    print(isosceles([1, 1, 3]))