def string_compare(P, T, i, j):
    if i == 0:
        return j
    if j == 0:
        return i
    switches = string_compare(P, T, i - 1, j - 1) + (P[i] != T[j])
    inserts = string_compare(P, T, i, j - 1) + 1
    deletes = string_compare(P, T, i - 1, j) + 1

    lowest_cost = min(switches, inserts, deletes)

    return lowest_cost


def string_compare_dp(P, T):
    D = [[0 for _ in range(len(T))] for __ in range(len(P))]
    for i in range(len(T)):
        D[0][i] = i
    for i in range(1, len(P)):
        D[i][0] = i

    parents = [['X' for _ in range(len(T))] for __ in range(len(P))]
    for i in range(1, len(T)):
        parents[0][i] = 'I'
    for i in range(1, len(P)):
        parents[i][0] = 'D'

    for i in range(1, len(P)):
        for j in range(1, len(T)):
            switches = D[i - 1][j - 1] + (P[i] != T[j])
            inserts = D[i][j - 1] + 1
            deletes = D[i - 1][j] + 1

            lowest_cost = min(switches, inserts, deletes)
            D[i][j] = lowest_cost

            if lowest_cost == switches:
                if P[i] == T[j]:
                    parents[i][j] = 'M'
                else:
                    parents[i][j] = 'S'
            elif lowest_cost == inserts:
                parents[i][j] = 'I'
            elif lowest_cost == deletes:
                parents[i][j] = 'D'
    parents[0][0] = 'X'

    return D[-1][-1]


def string_compare_dp_with_path(P, T):
    D = [[0 for _ in range(len(T))] for __ in range(len(P))]
    for i in range(len(T)):
        D[0][i] = i
    for i in range(1, len(P)):
        D[i][0] = i

    parents = [['X' for _ in range(len(T))] for __ in range(len(P))]
    for i in range(1, len(T)):
        parents[0][i] = 'I'
    for i in range(1, len(P)):
        parents[i][0] = 'D'

    for i in range(1, len(P)):
        for j in range(1, len(T)):
            switches = D[i - 1][j - 1] + (P[i] != T[j])
            inserts = D[i][j - 1] + 1
            deletes = D[i - 1][j] + 1

            lowest_cost = min(switches, inserts, deletes)
            D[i][j] = lowest_cost

            if lowest_cost == switches:
                if P[i] == T[j]:
                    parents[i][j] = 'M'
                else:
                    parents[i][j] = 'S'
            elif lowest_cost == inserts:
                parents[i][j] = 'I'
            elif lowest_cost == deletes:
                parents[i][j] = 'D'
    parents[0][0] = 'X'

    i = len(parents) - 1
    j = len(parents[0]) - 1
    path = []
    while parents[i][j] != 'X':
        path.append(parents[i][j])
        if parents[i][j] == 'M' or parents[i][j] == 'S':
            i -= 1
            j -= 1
        elif parents[i][j] == 'I':
            j -= 1
        elif parents[i][j] == 'D':
            i -= 1

    path.reverse()
    path = ''.join(path)
    return path


def string_compare_dp_fit(P, T):
    D = [[0 for _ in range(len(T))] for __ in range(len(P))]
    for i in range(1, len(P)):
        D[i][0] = i

    parents = [['X' for _ in range(len(T))] for __ in range(len(P))]
    for i in range(1, len(T)):
        parents[0][i] = 'I'
    for i in range(1, len(P)):
        parents[i][0] = 'D'

    for i in range(1, len(P)):
        for j in range(1, len(T)):
            switches = D[i - 1][j - 1] + (P[i] != T[j])
            inserts = D[i][j - 1] + 1
            deletes = D[i - 1][j] + 1

            lowest_cost = min(switches, inserts, deletes)
            D[i][j] = lowest_cost

            if lowest_cost == switches:
                if P[i] == T[j]:
                    parents[i][j] = 'M'
                else:
                    parents[i][j] = 'S'
            elif lowest_cost == inserts:
                parents[i][j] = 'I'
            elif lowest_cost == deletes:
                parents[i][j] = 'D'
    parents[0][0] = 'X'
    end = D[-1].index(min(D[-1]))
    start = end - len(P) + 2

    return start


def string_compare_dp_sequence(P, T):
    D = [[0 for _ in range(len(T))] for __ in range(len(P))]
    for i in range(len(T)):
        D[0][i] = i
    for i in range(1, len(P)):
        D[i][0] = i

    parents = [['X' for _ in range(len(T))] for __ in range(len(P))]
    for i in range(1, len(T)):
        parents[0][i] = 'I'
    for i in range(1, len(P)):
        parents[i][0] = 'D'

    for i in range(1, len(P)):
        for j in range(1, len(T)):
            if P[i] != T[j]:
                switches = D[i - 1][j - 1] + float('inf')
            else:
                switches = D[i - 1][j - 1]
            inserts = D[i][j - 1] + 1
            deletes = D[i - 1][j] + 1

            lowest_cost = min(switches, inserts, deletes)
            D[i][j] = lowest_cost

            if lowest_cost == switches:
                if P[i] == T[j]:
                    parents[i][j] = 'M'
                else:
                    parents[i][j] = 'S'
            elif lowest_cost == inserts:
                parents[i][j] = 'I'
            elif lowest_cost == deletes:
                parents[i][j] = 'D'
    parents[0][0] = 'X'

    i = len(parents) - 1
    j = len(parents[0]) - 1
    path = []
    while parents[i][j] != 'X':
        if parents[i][j] == 'M' or parents[i][j] == 'S':
            path.append(P[i])
            i -= 1
            j -= 1
        elif parents[i][j] == 'I':
            j -= 1
        elif parents[i][j] == 'D':
            i -= 1

    path.reverse()
    path = ''.join(path)

    return path


if __name__ == '__main__':
    P = ' kot'
    T = ' pies'
    print(string_compare(P, T, len(P) - 1, len(T) - 1))

    P = ' biały autobus'
    T = ' czarny autokar'
    print(string_compare_dp(P, T))

    P = ' thou shalt not'
    T = ' you should not'
    print(string_compare_dp_with_path(P, T))

    P = ' ban'
    T = ' mokeyssbanana'
    print(string_compare_dp_fit(P, T))

    P = ' democrat'
    T = ' republican'
    print(string_compare_dp_sequence(P, T))

    P = ' 123456789'
    T = ' 243517698'
    print(string_compare_dp_sequence(P, T))
