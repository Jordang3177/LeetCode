from unittest import TestCase

from Leetcode.Python.Finished.Easy.countAndSay import Solution as CountSolution
from Leetcode.Python.Finished.Easy.AddBinary import Solution as BinarySolution
from Leetcode.Python.Finished.Easy.atoi import Solution as AtoiSolution
from Leetcode.Python.Finished.Easy.CheckIfExist import Solution as CIESolution
from Leetcode.Python.Finished.Easy.ClimbingStairs import Solution as ClimbingSolution
from Leetcode.Python.Finished.Easy.DefangIP import Solution as DefangSolution
from Leetcode.Python.Finished.Easy.Fib import Solution as FibSolution
from Leetcode.Python.Finished.Easy.IntegerToRoman import Solution as ITRSolution
from Leetcode.Python.Finished.Easy.IsAnagram import Solution as AnagramSolution

class TestSolution(TestCase):
    def test_count_and_say(self):
        S = CountSolution()
        self.assertEqual(S.countAndSay(1), '1')
        self.assertEqual(S.countAndSay(2), '11')
        self.assertEqual(S.countAndSay(3), '21')
        self.assertEqual(S.countAndSay(4), '1211')
        self.assertEqual(S.countAndSay(5), '111221')
        self.assertEqual(S.countAndSay(6), '312211')
        self.assertEqual(S.countAndSay(7), '13112221')

    def test_add_binary(self):
        S = BinarySolution()
        self.assertEqual(S.addBinary('0', '0'), '0')
        self.assertEqual(S.addBinary('11', '1'), '100')
        self.assertEqual(S.addBinary('1010', '1011'), '10101')
        self.assertEqual(S.addBinary("10100000100100110110010000010101111011011001101110111111111101000000101111001110001111100001101","110101001011101110001111100110001010100001101011101010000011011011001011101111001100000011011110011"), "110111101100010011000101110110100000011101000101011001000011011000001100011110011010010011000000000")
        self.assertEqual(S.convertToBinary(1), '1')
        self.assertEqual(S.convertToBinary(0), '0')
        self.assertEqual(S.convertToBinary(10), '1010')

    def test_atoi(self):
        S = AtoiSolution()
        self.assertEqual(S.myAtoi('42'), 42)
        self.assertEqual(S.myAtoi('3439'), 3439)
        self.assertEqual(S.myAtoi('-13'), -13)
        self.assertEqual(S.myAtoi("     -42"), -42)
        self.assertEqual(S.myAtoi("         wow a 123"), 0)
        self.assertEqual(S.myAtoi("-234334853434325262343262362362362363"), -2**31)
        self.assertEqual(S.myAtoi("3248308420394637426384762347628346823"), 2**31 -1)
        self.assertEqual(S.myAtoi('-1+'), -1)
        self.assertEqual(S.myAtoi('+-2'), 0)
        self.assertEqual(S.myAtoi('-+2'), 0)
        self.assertEqual(S.myAtoi('000000'), 0)
        self.assertEqual(S.myAtoi('          0000            '), 0)
        self.assertEqual(S.myAtoi('0-1'), 0)
        self.assertEqual(S.myAtoi('           0-1'), 0)
        self.assertEqual(S.myAtoi('0+1'), 0)
        self.assertEqual(S.myAtoi('              0+1'), 0)


    def test_check_if_exist(self):
        S = CIESolution()
        self.assertEqual(S.checkIfExist([10,2,5,3]), True)
        self.assertEqual(S.checkIfExist([1]), False)
        self.assertEqual(S.checkIfExist([]), False)
        self.assertEqual(S.checkIfExist([1,1]), False)
        self.assertEqual(S.checkIfExist([1,3,5]), False)

    def test_climbing_stairs(self):
        S = ClimbingSolution()
        self.assertEqual(S.climbStairs(0), 1)
        self.assertEqual(S.climbStairs(1), 1)
        self.assertEqual(S.climbStairs(2), 2)
        self.assertEqual(S.climbStairs(3), 3)
        self.assertEqual(S.climbStairs(4), 5)
        self.assertEqual(S.climbStairs(5), 8)
        self.assertEqual(S.climbStairs(6), 13)
        self.assertEqual(S.climbStairs(7), 21)
        self.assertEqual(S.climbStairs(8), 34)
        self.assertEqual(S.climbStairs(9), 55)
        self.assertEqual(S.climbStairs(10), 89)

    def test_defang_ip(self):
        S = DefangSolution()
        self.assertEqual(S.defang_ip('1.1.1.1'), '1[.]1[.]1[.]1')
        self.assertEqual(S.defang_ip('250.0.168.1'), '250[.]0[.]168[.]1')
        self.assertEqual(S.defang_ip('168.1.1.0'), '168[.]1[.]1[.]0')

    def test_fib(self):
        S = FibSolution()
        self.assertEqual(S.fib(0), 0)
        self.assertEqual(S.fib(1), 1)
        self.assertEqual(S.fib(2), 1)
        self.assertEqual(S.fib(3), 2)
        self.assertEqual(S.fib(4), 3)
        self.assertEqual(S.fib(5), 5)
        self.assertEqual(S.fib(6), 8)
        self.assertEqual(S.fib(7), 13)
        self.assertEqual(S.fib(8), 21)
        self.assertEqual(S.fib(9), 34)
        self.assertEqual(S.fib(10), 55)
        self.assertEqual(S.fib(11), 89)
        self.assertEqual(S.fib(300), 222232244629420445529739893461909967206666939096499764990979600)

    def test_int_to_rom(self):
        S = ITRSolution()
        self.assertEqual(S.intToRoman(1), 'I')
        self.assertEqual(S.intToRoman(4), 'IV')
        self.assertEqual(S.intToRoman(1990), 'MCMXC')
        self.assertEqual(S.intToRoman(3999), 'MMMCMXCIX')
        self.assertEqual(S.intToRoman(90), 'XC')
        self.assertEqual(S.intToRoman(500), 'D')
        self.assertEqual(S.intToRoman(400), 'CD')
        self.assertEqual(S.intToRoman(100), 'C')
        self.assertEqual(S.intToRoman(50), 'L')
        self.assertEqual(S.intToRoman(40), 'XL')
        self.assertEqual(S.intToRoman(10), 'X')
        self.assertEqual(S.intToRoman(5), 'V')

    def test_is_anagram(self):
        S = AnagramSolution()
        self.assertEqual(S.isAnagram('anagram', 'nagaram'), True)