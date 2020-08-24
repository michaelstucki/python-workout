def sum(*args):
    result = 0
    for arg in args:
        result += arg

    return result


if __name__ == '__main__':
    print(sum(1, 2, 3, 4))

