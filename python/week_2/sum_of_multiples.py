def sum_of_multiples(limit, multiples):
    multiples_set = set()
    for multiple in multiples:
        if multiple <= 0:
            continue
        for i in range(multiple, limit, multiple):
            if i % multiple == 0:
                multiples_set.add(i)


    return sum(multiples_set)

if __name__ == '__main__':
    print(sum_of_multiples(1, [0]))