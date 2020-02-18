def array_manipulation(n, queries):
    helper_array = [0] * (n + 1)

    for query in queries:
        start_column = query[0] - 1
        end_column = query[1]
        value = query[2]

        helper_array[start_column] += value
        helper_array[end_column] -= value

    return calculate_max(helper_array)


def calculate_max(array):
    total = 0
    maximum = 0
    for x in array:
        total += x
        if total > maximum:
            maximum = total

    return maximum
