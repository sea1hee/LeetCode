class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        result = [0]*len(temperatures)
        
        st = []
        for i, cur in enumerate(temperatures):
            while st and cur > temperatures[st[-1]]:
                lower = st.pop()
                result[lower] = i - lower
            st.append(i)
        
        
        
        return result
        