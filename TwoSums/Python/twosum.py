"""
Given an array of integers nums and an integer target, return indices of the two
numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not
use the same element twice.

You can return the answer in any order.
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_set = set()
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_set:
                return [nums.index(complement), i]
            num_set.add(num)

"""
    J'initialise un set vide qui va contenir les nombres de la liste
    Je parcours la liste avec la fonction enumerate qui me permet de récupérer
    l'index et la valeur de chaque élément de la liste
    Je calcule le complément de la valeur de l'élément en cours de traitement
    par rapport à la valeur target
    Je vérifie si le complément est présent dans le set
    Si oui, je retourne l'index du complément et l'index de l'élément en cours
    de traitement
    Si non, j'ajoute l'élément en cours de traitement dans le set
"""
