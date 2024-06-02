from typing import List

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occ = {}
        liste = []
        for ele in arr:
            if str(ele) in occ:
                occ[str(ele)] = occ[str(ele)] + 1
            else:
                occ[str(ele)] = 1
        print(occ)
    
def main():
    sol = Solution()
    sol.uniqueOccurrences([1,2,2,1,1,3])

if __name__ == "__main__":
    main()