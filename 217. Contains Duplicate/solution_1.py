class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numsdict = {}
        for num in nums:
            if num in numsdict:
                return True
            else:
                numsdict[num] = 1
        
        return False