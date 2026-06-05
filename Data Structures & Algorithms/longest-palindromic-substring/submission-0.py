class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1 :
            return s
        
        start = 0
        max_len = 1

        def expand(left , right ) :
            nonlocal start, max_len

            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            curr_len = right - left - 1
        
            if curr_len > max_len:
                max_len = curr_len
                start = left + 1

        
        for i in range(len(s)) :
            expand(i , i)
            expand(i , i + 1)

        return s[start:start + max_len]

            
        
