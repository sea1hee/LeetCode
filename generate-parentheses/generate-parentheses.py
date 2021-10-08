class Solution(object):
    def generate(self, left, right, s, result):
        
        if right == 0:
            result.append(s)
        elif left == 0:
            result.append(s+")"*right)
            right = 0
        elif left == right:
            self.generate(left-1, right, s+"(", result)
        else:
            self.generate(left-1, right, s+"(", result)
            self.generate(left, right-1, s+")", result)
        
        return result
    
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        return self.generate(n, n, "", [])
        
    
        