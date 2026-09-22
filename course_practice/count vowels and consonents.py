s='hel lo 123$world'
vowels = 0
consonents = 0
for ch in s:
    if ch.isalpha():
        if ch in("aeiou"):
            vowels +=1
        else:
            consonents+=1

print(f'there are {vowels} vowels and {consonents} consonents')