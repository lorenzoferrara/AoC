import numpy as np
import pandas as pd
import re

with open("input.txt", "r") as file:
    # with open("example.txt", "r") as file:
    lines = file.readlines()

matr = []
for line in lines:
    matr.append(list(line))

row_num = len(matr)
col_num = len(matr[0]) - 1  # c'è il \n a fine riga

parola = "XMAS"
totale = 0
for i in range(row_num):
    for j in range(col_num):
        # print(f"{i} su {row_num}, {j} su {col_num}")

        if matr[i][j] == "X":
            for step_row in [-1, 0, 1]:
                for step_col in [-1, 0, 1]:  # qui scelgo la direzione
                    cont = 1
                    while (
                        row_num > i + step_row * cont >= 0
                        and col_num > j + step_col * cont >= 0
                        and cont < 4
                        and matr[i + step_row * cont][j + step_col * cont]
                        == parola[cont]
                    ):
                        cont += 1
                        # print(i+step_row*cont, j+step_col*cont)#matr[i+step_row*cont])
                    if cont == 4:
                        totale += 1


print(totale)

########### part 2

totale = 0
for i in range(row_num):
    for j in range(col_num):

        if matr[i][j] == "A" and row_num - 1 > i >= 1 and col_num - 1 > j >= 1:

            ul_dr = set([matr[i - 1][j - 1], matr[i + 1][j + 1]])
            ur_dl = set([matr[i - 1][j + 1], matr[i + 1][j - 1]])
            if ul_dr == {"M", "S"} and ur_dl == {"M", "S"}:
                totale += 1

print(totale)
