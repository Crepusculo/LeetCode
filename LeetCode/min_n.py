arrays = [1, 5, 10, 9, 5, 4, 23, 32, 6, 31, 2, ]
n = 3


def min_n(k):
    if n < len(arrays):
        ret = [["Index: " + str(i), arrays[i]] for i in range(k)]
        for idx, val in enumerate(arrays[n:]):
            maxs = max(ret, key=lambda x: x[1])
            if val < maxs[1]:
                ret.pop(ret.index(maxs))
                ret.append(["Index: " + str(idx), val])
        return ret

if __name__ == '__main__':
    print(max(min_n(n), key=lambda x: x[1]))
