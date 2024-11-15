from typing import List

class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        for i in range(len(details)):
            if details[i][11:13] > '60':
                count += 1

        return count

if __name__ == '__main__':
    details = ["7868190130M7522", "5303914400F9211", "9273338290F4010"]
    print(Solution().countSeniors(details))
