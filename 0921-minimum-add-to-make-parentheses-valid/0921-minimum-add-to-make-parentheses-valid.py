class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        for val in s:
            if not stack:
                stack.append(val)
            elif stack[-1] == '(' and val == ')':
                stack.pop()
            else:
                stack.append(val)

        return len(stack)