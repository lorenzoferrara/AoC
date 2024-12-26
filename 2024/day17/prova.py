for i in range(8):
    print(f"{i}^3={i^3}")

for reg_A in range(10, 200):
    p1 = reg_B = reg_A % 8

    p2 = reg_B = reg_B ^ 3

    p3 = reg_C = int(reg_A / (2**reg_B))

    p4 = reg_B = reg_B ^ reg_C

    p5 = reg_B = reg_B ^ 5

    out = reg_B % 8

    print(f"{reg_A},\t{p1},\t{p2},\t{p3},\t{p4},\t{p5},\t{out}")
