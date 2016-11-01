m = [
    [1, 0, 3, 4, 2],
    [3, 1, 0, 2, 4],
    [1, 4, 2, 3, 0],
    [0, 3, 2, 1, 4],
    [1, 3, 0, 4, 2]
]
w = [
    [4, 0, 1, 3, 2],
    [2, 1, 3, 0, 4],
    [1, 2, 3, 4, 0],
    [0, 4, 3, 2, 1],
    [2, 1, 3, 0, 4]
]

SINGLE_DOG = -1


def gale_shapley(man, woman):
    global SINGLE_DOG
    n = len(man)

    man_marry = []  # match[current_man] is man[current_man] match woman
    women_marry = []
    current_woman_match = []
    man_index = []

    # initialize
    for i in range(0, n):
        temp = {}
        man_marry.append(SINGLE_DOG)
        current_woman_match.append(SINGLE_DOG)
        man_index.append(0)

        for j in range(0, n):
            temp[woman[i][j]] = j
        women_marry.append(temp)

    is_no_one_single = False

    while not is_no_one_single:
        is_no_one_single = True
        for current_man in range(0, n):
            # if no one still single, is_no_one_single = True
            if man_marry[current_man] != SINGLE_DOG:
                continue
            # if still has someone single
            is_no_one_single = False

            women_index = man_index[current_man] + 1
            man_index[current_man] += 1
            current_woman = man[current_man][women_index]

            fiance = current_woman_match[current_woman]
            # Success kick the old one
            if fiance == SINGLE_DOG or women_marry[current_woman][current_man] < women_marry[current_woman][fiance]:
                man_marry[current_man] = current_woman
                current_woman_match[current_woman] = current_man
                # The old one go back to single dog
                if fiance != SINGLE_DOG:
                    man_marry[fiance] = SINGLE_DOG
    return man_marry


def main():
    man = m
    woman = w
    match = gale_shapley(man, woman)
    for man, woman in enumerate(match):
        print(man, "<=>", woman)


if __name__ == "__main__":
    main()
