class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        ret = []
        
        reverse = s[::-1]
        maxIndex = 0
        count = 0
        for index in range(len(s)):
            count += 1
            
            curMaxIndex = len(s) - reverse.find(s[index]) - 1
            maxIndex = curMaxIndex if maxIndex < curMaxIndex else maxIndex
        
            if maxIndex == index:
                ret.append(count)
                count = 0
                maxIndex = 0
        
        return ret
            
            
        
        
        