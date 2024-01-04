class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numsset = set(nums)

        l1 = len(nums)
        l2 = len(numsset)

        if(l1 != l2):
            return True
        
        return False

        