class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        given string, returns if the string is a palindrome (if reversed if it's the same as original string)
        :param s: str
        :return: bool
        """
        j = len(s) - 1
        i = 0
        while i < j:
            if not s[i].isalnum():
                i += 1
            elif not s[j].isalnum():
                j -= 1
            elif s[i].lower() != s[j].lower():
                return False
            else:
                i += 1
                j -= 1
        return True


    def testIsPalindrome(self):
        assert self.isPalindrome("A man, a plan, a canal: Panama") == True
        assert self.isPalindrome("race a car") == False
        assert self.isPalindrome("how about that") == False
        assert self.isPalindrome("a") == True
        assert self.isPalindrome("") == True
        assert self.isPalindrome("Aa") == True
        assert self.isPalindrome("ab") == False
        assert self.isPalindrome('0P') == False
        assert self.isPalindrome('00') == True


if __name__ == "__main__":
    S = Solution()
    S.testIsPalindrome()
    print("All Tests Passed")