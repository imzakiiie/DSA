data = [4,5,6,7,8,9,0]
# n = len(data)
# reversed_data = []
# for i in range(n-1,-1,-1):
#     reversed_data.append(data[i])
# print(f"the reversed data is:", reversed_data)


n = len(data) - 1
reversed_data2 = []
while n >= 0:
    reversed_data2.append(data[n])
    n -= 1
print(f"The reversed data is: {reversed_data2}")
