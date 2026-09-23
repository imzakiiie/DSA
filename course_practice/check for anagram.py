# # time: nlogn
s1 = 'listen'
s2 = 'silent'

# s1_sorted = sorted(s1)
# s2_sorted = sorted(s2)

# if s1_sorted == s2_sorted:
#     print("Anagram")

# else:
#     print("Not Anagram")



# time: n
mapping = [0] * 26
for ch in s1:
    index = ord(ch) - 97
    mapping[index] += 1

for ch in s2:
    index = ord(ch) - 97
    mapping[index] -= 1

if all(m == 0 for m in mapping):
    print('Anagram')
else:
    print('Not anagram')
