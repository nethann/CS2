class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        """
        :type string: str
        :rtype: bool
        """
        track_openings = []
        closing_to_opening = {')': '(', ']': '[', '}': '{'}
        
        for character in s:
            if character in closing_to_opening:
                if not track_openings:
                    return False
                last_opening = track_openings.pop()
                if last_opening != closing_to_opening[character]:
                    return False
            else:
                track_openings.append(character)
        return len(track_openings) == 0

solution = Solution()

print(solution.isValid("()"))  
print(solution.isValid("()[]{}"))  
print(solution.isValid("(]"))  
print(solution.isValid("([])"))  
