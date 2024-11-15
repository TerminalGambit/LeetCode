from typing import List

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seq = sorted([s[i:i+10] for i in range(0, len(s)-10)])
        res = set()
        for i in range(len(seq)-1):
            if seq[i] == seq[i+1]:
                res.add(seq[i])
        return list(res)
