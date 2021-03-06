class Solution:
    def singleNumber(self, nums):
        """
        returns the number that is only used once in the given array
        :param nums: array of ints
        :return: int
        """
        # This is the faster solution
        return 2*sum(set(nums)) - sum(nums)
        # However this solution will use slightly less memory
        # answer = 0
        # for value in nums:
        #     answer ^= value
        # return answer

    def testSingleNumber(self):
        assert self.singleNumber([1, 1, 2, 2, 3, 3, 4]) == 4
        assert self.singleNumber([1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 4, 5, 6]) == 7
        assert self.singleNumber([8, 7, 6, 5, 4, 3, 2, 1, 8, 7, 6, 5, 4, 3, 2, 9, 9, 10, 10, 11, 12, 11, 12]) == 1
        assert self.singleNumber([1, 1, 2]) == 2
        assert self.singleNumber([10, 10, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6]) == 6
        assert self.singleNumber([1]) == 1


if __name__ == '__main__':
    S = Solution()
    S.testSingleNumber()
    print("All Tests Passed")