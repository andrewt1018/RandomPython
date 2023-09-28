def calculate_pigeonhole_multiple(n: int) -> int:
    possibilities = []
    mods = []
    index1 = None
    index2 = None
    for i in range(0, n + 1):
        print("Mods: ", mods)
        if i == 0:
            possibilities.append(1)
        else:
            possibilities.append(possibilities[i-1] * 10 + 1)
        new_mod = possibilities[i] % n
        for k in mods:
            if new_mod == k:
                print("New Mod: ", new_mod)
                index1 = mods.index(k)
                index2 = i
                return possibilities[index2] - possibilities[index1]
        mods.append(new_mod)


print(calculate_pigeonhole_multiple(7))

