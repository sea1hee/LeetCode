class Solution(object): 
        
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        
        def sub(cur, index):
            result.append(cur)
            for i in range(index, len(nums)):
                sub(cur+[nums[i]], i+1)
        
        sub([], 0)
        return result
        