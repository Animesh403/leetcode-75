class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        hash = set()
        for i in range(0,len(nums)):
            if nums[i] in hash:
                return True
            else:
                hash.add(nums[i])
        return False
