s = 'banana'
counts = dict()
for ch in s:
    counts[ch] = counts.get(ch,0)+1
counts