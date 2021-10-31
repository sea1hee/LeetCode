import operator

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        ans = []
        dic_num = {}
        for num in nums:
            if num in dic_num:
                dic_num[num] += 1
            else:
                dic_num[num] = 1
         
        sorted_dic= sorted(dic_num.items(), key=operator.itemgetter(1), reverse = True)
        
        for i in range(k):
            ans.append(sorted_dic[i][0])
            
        return ans
            
        