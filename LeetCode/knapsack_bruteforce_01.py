w = [1, 2, 3, 4, 5, 6, 10]
v = [2, 4, 6, 8, 10, 3, 10]
l = 10


def brute_force(w_array, v_array, w_limit):
    n = len(w_array)
    max_value = 0
    max_weight = 0
    ret = []
    for i in range(0, pow(2, n)):
        bin_int = '%0*d' % (n, int(bin(i)[2:]))
        bin_list = list(map(int, str(bin_int)))
        w_cur = 0
        v_cur = 0
        for j, val in enumerate(bin_list):
            if val == 1:
                w_cur += w_array[j]
                v_cur += v_array[j]
        # print('Now Value is ', w_cur, '\t the weight is ', v_cur, "\t And the solution is", list(bin_list),
        #      '' if w_cur < 20 else 'invalid')
        if w_cur <= w_limit and max_value <= v_cur:
            max_value = v_cur
            max_weight = w_cur
            ret = bin_list
    print('Max Value is ', max_value, '\t the weight is ', max_weight, "\t And the solution is", list(ret))
    return ret


def main():
    weight_array = w
    value_array = v
    limit = l
    ret = brute_force(weight_array, value_array, limit)


if __name__ == '__main__':
    main()
