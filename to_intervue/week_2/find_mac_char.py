def max_count(string: str):
    if  not string:
        return ''

    max_char = string[0]
    count = 1
    max_count = 1

    for i in range(1, len(string)):
        if string[i] == string[i-1]:
            count += 1
        else:
            count = 1

        if count >= max_count:
            max_count = count
            max_char = string[i]

    return max_char

# if __name__ == "__main__":
#     print(max_count("bbcccbbdd"))


def symmetry(points):
    if not points:
        return None

    point_set = set(points)

    max_x = max(x for x, y in points)
    min_x = min(x for x, y in points)
    axis = (max_x + min_x) / 2

    for x, y in points:
        reflected = (2 * axis - x, y)
        if reflected not in point_set:
            return None

    return axis




if __name__ == "__main__":
    points_1 = [(-4, 2), (4, 2), (3, 3), (-3, 3)]
    points_2 = [(-4, 2), (4, 3), (3, 3), (-3, 3)]
    print(symmetry(points_1))