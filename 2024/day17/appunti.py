2 4 reg_B= reg_A % 8

# b fra 0 e 7

1 3 reg_B = reg_B ^ 3

# 0^3=3
# 1^3=2
# 2^3=1
# 3^3=0
# 4^3=7
# 5^3=6
# 6^3=5
# 7^3=4

7 5 reg_C = int(reg_A / (2**reg_B) )

4 2 reg_B = reg_B ^ reg_C

0 3 reg_A = int(reg_A / 8 )

1 5 reg_B = reg_B ^ 5

5 5 print( reg_B % 8)

3 0 if reg_A!=0, torna da capo

A deve essere al massimo 2e14, al minimo 3.5e13