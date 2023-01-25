def sort_it(string):
    listed = list(string)

    for i in range(len(listed)):
        for j in range(i + 1, len(listed)):
            if listed[i] > listed[j]:
                listed[i], listed[j] = listed[j], listed[i]

    return "".join(listed)


def is_anagram(first_string, second_string):
    status = False

    lowered_1st = first_string.lower()
    lowered_2nd = second_string.lower()

    sorted_1st = sort_it(lowered_1st)
    sorted_2nd = sort_it(lowered_2nd)

    status = sorted_1st == sorted_2nd

    return (sorted_1st, sorted_2nd, status)
