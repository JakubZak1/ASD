import time

with open("lotr.txt", encoding='utf-8') as f:
    text = f.readlines()

S = ' '.join(text).lower()
W = 'time.'


def naive(S, W):
    m = 0
    execution_counter = 0
    correct_text_counter = 0
    while len(S) - m >= len(W):
        i = 0
        execution_counter += 1
        while i < len(W) and S[m + i] == W[i]:
            i += 1
        if i == len(W):
            correct_text_counter += 1
        m += 1
    return correct_text_counter, execution_counter


d = 256
q = 101  # liczba pierwsza


def hash(word):
    hw = 0
    for i in range(len(word)):  # N - to długość wzorca
        hw = (hw * d + ord(word[i])) % q  # dla d będącego potęgą 2 można mnożenie zastąpić shiftem uzyskując pewne przyspieszenie obliczeń

    return hw


def RabinKarp(S, W):
    hW = hash(W)
    found = 0
    execution_counter = 0
    collision_counter = 0
    idx = []
    h = 1
    for i in range(len(W) - 1):
        h = (h * d) % q
    for m in range(len(S) - len(W) + 1):
        if m == 0:
            hS = hash(S[m:m + len(W)])
        else:
            hS = (d * (hS - ord(S[m - 1]) * h) + ord(S[m - 1 + len(W)])) % q
        execution_counter += 1
        if hS == hW:
            if S[m:m + len(W)] == W:
                found += 1
                idx.append(m)
            else:
                collision_counter += 1
    return found, execution_counter, collision_counter


def kmp_table(W):
    T = [0 for _ in range(len(W) + 1)]
    T[0] = -1
    pos = 1
    cnd = 0
    while pos < len(W):
        if W[pos] == W[cnd]:
            T[pos] = T[cnd]
        else:
            T[pos] = cnd
            while cnd >= 0 and W[pos] != W[cnd]:
                cnd = T[cnd]
        pos += 1
        cnd += 1
    T[pos] = cnd
    return T


def kmp_search(S, W):
    m = 0
    i = 0
    T = kmp_table(W)
    nP = 0
    P = []
    execution_counter = 0
    while m < len(S):
        execution_counter += 1
        if W[i] == S[m]:
            m += 1
            i += 1
            if i == len(W):
                P.append(m - i)
                nP += 1
                i = T[i]
        else:
            i = T[i]
            if i < 0:
                m += 1
                i += 1
    return len(P), execution_counter, T


# t_start = time.perf_counter()
result = naive(S, W)
# t_stop = time.perf_counter()
result1 = str(result[0]) + '; ' + str(result[1])
print(result1)
# print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))

# t_start = time.perf_counter()
result = RabinKarp(S, W)
# t_stop = time.perf_counter()
result1 = str(result[0]) + '; ' + str(result[1]) + '; ' + str(result[2])
print(result1)
# print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))

# t_start = time.perf_counter()
result = kmp_search(S, W)
# t_stop = time.perf_counter()
result1 = str(result[0]) + '; ' + str(result[1]) + '; ' + str(result[2])
print(result1)
# print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))
