class Solution:
    def isPalindrome(self, s: str) -> bool:
        pal=''
        for i in s.upper():
            if i.isalnum():
                pal+=i
            else:
                continue
        if pal[::-1]==pal:
            return True
        else:
            return False