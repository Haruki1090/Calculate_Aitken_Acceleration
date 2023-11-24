def calculate_an(n):
    result = 0
    for k in range(n + 1):
        numerator = (-1) ** k
        denominator = 2 * k + 1
        result += numerator / denominator
    return result

# n=1から30までの数列a_nを求める。さらに求めた数列それぞれを配列a_nに格納する。
a_n = []
for n in range(1, 31):
    result = calculate_an(n)
    a_n.append(result)
    print(f"a_{n} = {result}")

# b_nを計算し、b_nという配列に格納（1回加速）して出力。
b_n = []
for n in range(len(a_n) - 2):
    result = a_n[n] - (a_n[n + 1] - a_n[n]) ** 2 / (a_n[n + 2] - 2 * a_n[n + 1] + a_n[n])
    b_n.append(result)
    print(f"b_{n+1} = {result}")

# c_nを計算し、c_nという配列に格納（2回加速）して出力。
c_n = []
for n in range(len(b_n) - 2):
    result = b_n[n] - (b_n[n + 1] - b_n[n]) ** 2 / (b_n[n + 2] - 2 * b_n[n + 1] + b_n[n])
    c_n.append(result)
    print(f"c_{n+1} = {result}")

# d_nを計算し、d_nという配列に格納（3回加速）して出力。
d_n = []
for n in range(len(c_n) - 2):
    result = c_n[n] - (c_n[n + 1] - c_n[n]) ** 2 / (c_n[n + 2] - 2 * c_n[n + 1] + c_n[n])
    d_n.append(result)
    print(f"d_{n+1} = {result}")

# e_nを計算し、d_nという配列に格納（4回加速）して出力。
e_n = []
for n in range(len(d_n) - 2):
    result = d_n[n] - (d_n[n + 1] - d_n[n]) ** 2 / (d_n[n + 2] - 2 * d_n[n + 1] + d_n[n])
    e_n.append(result)
    print(f"e_{n+1} = {result}")