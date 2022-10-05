s = [
    [1, 3, 4, 10],
    [2, 5, 9, 11],
    [6, 8, 12, 15],
    [7, 13, 14, 16]
]
# b = 1 , l = 4
# d_l = 1
s2 = [
    [1, 2, 3, 4]
]
# b = 2, l = 4
# d_l = 2
s3 = [
    [1, 3, 4, 7],
    [2, 5, 6, 8]
]

# b = 5 , l = 4
# d_l = 4
s4 = [
    [1, 3, 4, 10],
    [2, 5, 9, 11],
    [6, 8, 12, 17],
    [7, 13, 16, 18],
    [14, 15, 19, 20]
]


# s = {}
# for i,j = 0 to l-1, 0 to b-1: s[i+j+1] = [], append i,j pairs
# loop through evert zigzag step, 1 to  l+b-1
# default order is down slope, every odd pos should be opposite direction


def zig_zag_traverse(m=s4):
    l = len(m[0])
    b = len(m)
    zzs = {}
    for j in range(b):
        for i in range(l):
            if (i + j + 1) in zzs:
                zzs[i + j + 1].append(m[j][i])
            else:
                zzs[i + j + 1] = [m[j][i]]
    solution = []
    for z in range(1, l + b):
        if z % 2 == 0:
            for i in range(len(zzs[z]) - 1, -1, -1):
                solution.append(zzs[z][i])
        else:
            solution.extend(zzs[z])
    return solution


if __name__ == '__main__':
    sol = zig_zag_traverse()
    print(sol)
    # FIXME need to optimize the code
