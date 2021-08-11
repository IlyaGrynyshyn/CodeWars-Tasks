def bubble(l):
    g = []
    for i in range(len(l)):
        for j in range(len(l) - i - 1):
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]
                g.append(l[:])

    return g


ke = [2, 1, 4, 3]

print(bubble(ke))
