def square_root_field(a: int, p: int, interim=False):
    is_square = pow(a, int((p - 1) / 2), p)
    if is_square != 1:
        if interim: print(
            f"a ^ (p - 1) / 2 = {a} ^ {int((p - 1) / 2)} = {is_square} != 1;\n => a = {a} ist kein Quadrat in F{p}")
        return
    if interim: print(f"a ^ (p - 1) / 2 = {a} ^ {int((p - 1) / 2)} = {is_square}\n    {a} ist ein Quadrat in F{p}")

    if (p + 1) % 4 == 0:
        if interim: print(
            f"4 | (p - 1) <=> 4 | {p + 1}: w = a ^ (p + 1) / 4 = {a} ^ {int((p + 1) / 4)} = {pow(a, int((p + 1) / 4), p)}\n => w = {pow(a, int((p + 1) / 4), p)} ist Wurzel von {a} in F{p}")
        return pow(a, int((p + 1) / 4), p)

    l = 0
    t = -1
    while (p - 1) / 2 != pow(2, l, p) * t:
        t += 2
        while (p - 1) / 2 != pow(2, l, p) * t:
            l += 1
            if l > p:
                break;
        if t > p:
            if interim: print("Kein (p-1)/2 =", (p - 1) / 2, "= 2^l * t")
            return

    if interim: print(f"Suche (p - 1) / 2 = 2 ^ l * t  mit t ungerade:\n    {int((p - 1) / 2)} = 2 ^ {l} * {t}")

    b = 1
    while pow(b, int((p - 1) / 2), p) != p - 1:
        b += 1
    if interim: print(f"Wähle b mit b ^ (p - 1) / 2 = -1:\n    {b} ^ {int((p - 1) / 2)} = -1 => b = {b}")

    n = [None] * (l + 2)
    c = [None] * (l + 2)
    n[0] = 0

    if interim: print(" n0 = 0")
    for i in range(l + 1):
        if n[i] is not None:
            c[i] = (pow(a, int(2 ** (l - (i + 1)) * t), p) * pow(b, int(n[i]), p)) % p
            if interim: print(
                f" c{i} = a ^ (2 ^ (l - (i + 1)) * t) * b ^ ni = {a} ^ (2 ^ ({l} - {(i + 1)}) * {t}) * {b} ^ {n[i]} = {c[i]}")
        if c[i] == 1:
            n[i + 1] = int(n[i] / 2)
            if interim: print(f" n{i + 1} = n{i} / 2 = {n[i]} / 2 = {n[i + 1]}")
        else:
            n[i + 1] = int(n[i] / 2 + (p - 1) / 4)
            if interim: print(f" n{i + 1} = n{i} / 2 + (p - 1) / 4 = {n[i]} / 2 + {int((p - 1) / 4)} = {n[i + 1]}")
    if interim: print(
        f"w = a ^ (t + 1) / 2 * b ^ nl = {a} ^ {int((t + 1) / 2)} * {b} ^ {n[l]} = {(pow(a, int((t + 1) / 2), p) * pow(b, int(n[l]), p)) % p}\n => w = {(pow(a, int((t + 1) / 2), p) * pow(b, int(n[l]), p)) % p} ist Wurzel von {a} in F{p}")
    return (pow(a, int((t + 1) / 2), p) * pow(b, int(n[l]), p)) % p



if __name__ == "__main__":
    square_root_field(2, 11, True)
    print("\n----------------------\n")
    square_root_field(5, 11, True)
    print("\n----------------------\n")
    square_root_field(2, 17, True)
