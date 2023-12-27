def nth_term(a, d, n):

    if n < 1:
        raise ValueError("Номер члена повинен бути не менше 1")
    if d == 0:
        raise ValueError("Постійний для послідовності не повинен дорівнювати 0")

    return a + (n - 1) * d


def main():

    a = 5
    d = 3
    n = 5

    try:
        print(nth_term(a, d, n))
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
