def value_range(values):
    return min(values), max(values)


def mean(values):
    return sum(values) / len(values)


x = (10, 50, 1, 4, 30)
print(value_range(x))
print(mean(x))
