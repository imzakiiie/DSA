s = "rat"
t = "car"
class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False

        mapping = [0]*26
        for ch in s:
            index = ord(ch)-97
            mapping[index] += 1

        for ch in t:
            index = ord(ch)-97
            mapping[index] -= 1

        if all (m==0 for m in mapping):
            return True
        else:
            return False
