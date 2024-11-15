class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        liste = []
        for ele in nums:
            if ele in liste:
                liste.pop(liste.index(ele))
            else:
                liste.append(ele)
        return liste