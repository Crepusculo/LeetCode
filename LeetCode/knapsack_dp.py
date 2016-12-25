limit = 25
items = [(3, 2), (1, 7), (15, 20)]


def best_value(i, cur_weight):
    if i == 0:
        return 0
    value, weight = items[i - 1]
    if weight > cur_weight:
        return best_value(i - 1, cur_weight)
    else:
        return max(best_value(i - 1, cur_weight), best_value(i - 1, cur_weight - weight) + value)


result = []
i = limit
for each in range(len(items), 0, -1):
    if best_value(each, i) != best_value(each - 1, i):
        result.append(items[each - 1])
        i -= items[each - 1][1]
print(best_value(len(items), limit), result)
