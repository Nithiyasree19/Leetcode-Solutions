class Solution(object):
    def isValid(self, s):
        stack = []
        for c in s:
            if c in '([{': 
                stack.append(c)
            elif not stack or c + stack.pop() not in (')(', '][', '}{'): 
                return False
        return not stack
