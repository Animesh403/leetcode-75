class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashMap = {}
        for index,element in enumerate(nums):
            to_check = target - element
            if to_check in hashMap:
                return [index,hashMap[to_check]]
            hashMap[element]= index
#Time -O(n)
