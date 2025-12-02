def next_secret_number(num):
    temp = num*64
    num = num ^ temp
    num = num % 16777216 #2^24

    temp = int(num/32)
    num = num ^ temp
    num = num % 16777216

    temp = num*2048
    num = num ^ temp
    num = num % 16777216

    return num

sequences = set()
total=0

start = 123
num=start

sequence=[]
for i in range(2000):
    new_num=next_secret_number(num)

    new_price = new_num%10 
    diff = new_price - (num%10)
    num=new_num
    sequence.append(diff)
    if i>3:
    	sequence.pop(0)
    	sequences.add(tuple(sequence))

print(len(sequences))

max_result=0


# L=len(sequences)
# for ind,chosen_sequence in enumerate(sequences):

#     print(f'{ind}/{L}')
#     result=0

#         start = 123
#         num=start

#         sequence=[]
#         for i in range(10):
#             new_num=next_secret_number(num)

#             new_price = new_num%10 
#             diff = new_price - (num%10)
#             num=new_num

#             sequence.append(diff)
#             if i>3:
#                 sequence.pop()
#                 if sequence==chosen_sequence:
#                     result+=new_price

#     max_result = max(max_result, result)

#     # print(start, num)

# print(f'Final secret number: {max_result}')