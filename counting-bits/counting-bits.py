class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ans = []
        
        for i in range(n+1):
            binary = str(bin(i))
            count = binary.count("1")
            ans.append(count)
        
        return ans