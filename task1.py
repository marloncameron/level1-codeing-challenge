# total_sum = 3
# for i in range(10):
#     if (i%3 == 0 or i%5 == 0):
#         total_sum = total_sum+i
# print(total_sum)

nums = [3, 5]

result = 0
for i in range(0,1000):
    if i%3 == 0 or i%5 == 0:
        result += i

print(result)
