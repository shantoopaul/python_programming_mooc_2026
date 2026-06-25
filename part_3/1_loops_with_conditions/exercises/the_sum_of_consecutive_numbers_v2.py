limit = int(input("Limit: "))
num = 1
sum = 1
sum_word = "1"

while sum < limit:
    num += 1
    sum += num
    sum_word += f" + {num}"
print(f"The consecutive sum: {sum_word} = {sum}")