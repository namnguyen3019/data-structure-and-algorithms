

class Solution:
    def minMovesToMakePalindrome(self, s: str) -> int:
        s = list(s)
        moves = 0
        left, right = 0, len(s) - 1

        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
                continue
            # FIND s[k] == s[left] from right to the left

            k = right - 1
            while s[k] != s[left]:
                k -= 1
            
            # if could not find s[k] == s[left]
            if k == left:
                mid = len(s)//2
                for i in range(left, mid):
                    moves += 1
            else:
                for i in range(k, right):
                    s[i], s[i+1] = s[i+1], s[i]
                    moves += 1
                left += 1
                right -= 1
        return moves
