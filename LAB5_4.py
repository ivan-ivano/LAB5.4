# < Іваньо Іван >
# Лабораторна робота № 5.4
# Обчислення сум та добутків за допомогою рекурсії.
# Варіант 0.6

N = int(input('N = '))


def P0(N):
    P = 1
    k = N
    while k <= 19:
        P *= (k - N) / (k + N) + 1
        k += 1
    return P


def P1(N, k):
    if k > 19:
        return 1
    else:
        return ((k - N) / (k + N) + 1) * P1(N, k + 1)


def P2(N, k):
    if k < N:
        return 1
    else:
        return ((k - N) / (k + N) + 1) * P2(N, k - 1)


def P3(N, k, t):
    t = t * ((k - N) / (k + N) + 1)
    if k >= 19:
        return t
    else:
        return P3(N, k + 1, t)


def P4(N, k, t):
    t = t * ((k - N) / (k + N) + 1)
    if k <= N:
        return t
    else:
        return P4(N, k - 1, t)


print(round(P0(N), 4))
print(round(P1(N, N), 4))
print(round(P2(N, 19), 4))
print(round(P3(N, N, 1), 4))
print(round(P4(N, 19, 1), 4))
