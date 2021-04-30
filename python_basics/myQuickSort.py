def sort(lst):
    if len(lst) == 0:
        return lst
    else:
        pivot = lst[0]
        smallers = []
        biggers = []
        equals = []
        for item in lst:
            if item < pivot:
                smallers.append(item)
            elif item > pivot:
                biggers.append(item)
            else:
                equals.append(item)
        return sort(smallers) + equals + sort(biggers)


if __name__ == "__main__":
    lst = [2, 3, 6, 1, 9, 5, 7, 8, 10, 4]
    print(sort(lst))