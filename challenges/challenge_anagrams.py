def sort_it(string):
    listed = list(string)

    for i in range(len(listed)):
        for j in range(i + 1, len(listed)):
            if listed[i] > listed[j]:
                listed[i], listed[j] = listed[j], listed[i]

    return "".join(listed)


def is_anagram(first_string, second_string):
    status = False
    if not first_string or len(first_string) < 1:
        return ["", second_string, status]

    lowered_1st = first_string.lower()

    if not second_string or len(second_string) < 1:
        return [lowered_1st, "", status]

    lowered_2nd = second_string.lower()

    sorted_1st = sort_it(lowered_1st)
    sorted_2nd = sort_it(lowered_2nd)

    status = sorted_1st == sorted_2nd

    return (sorted_1st, sorted_2nd, status)
