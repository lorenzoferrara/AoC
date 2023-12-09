

time_list = [60, 80, 86, 76]
dist_list = [601,   1163,   1559,   1300]

product=1
for time, dist in zip(time_list, dist_list):
    somma=0
    for T_p in range(time):
        if (time-T_p)*T_p>dist:
            somma += 1
    product *= somma

print(product)

####################################

time = 60808676
dist = 601116315591300

somma=0
for T_p in range(time):
    if (time-T_p)*T_p>dist:
        somma += 1

print(somma)
