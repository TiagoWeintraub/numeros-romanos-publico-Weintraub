import unittest


def convert_decimal_to_roman(decimal_number):
    roman = ''
    
    rest = decimal_number % 10
    mult_10 = decimal_number // 10
    var_1 = ''
    var_2 = ''
    result_1_2_3 = ''
    result_4 = ''
    result_5 = ''
    result_6_7_8 = '' 
    result_9 = ''
    result_10 = ''
    result_50 = ''
    result_100 = ''

    if 0 < mult_10 < 4:
        for digit in range(mult_10):
            result_10 += 'X'

    if rest < 4:
        for digit in range(rest):
            result_1_2_3 += 'I'
    
    if rest == 5:
        result_5 = 'V' 

    if rest == 4:
        result_4 = 'IV' 

    if rest == 9:
        result_9 = 'IX' 

    if 5 < rest < 9:
        for digit in range(rest-5):
            var_2 = 'V'
            var_1 += 'I'
            result_6_7_8 = var_2 + var_1
    
    if mult_10 == 5:
        result_50 = 'L' 

    if 9 < mult_10 < 20:
        result_100 = 'C'

    result = result_100 + result_50 + result_10 + result_9 + result_4+ result_5 + result_6_7_8 + result_1_2_3
    return result


class TestDecimalToRoman(unittest.TestCase):
    def test_1(self):
        roman_number = convert_decimal_to_roman(1)
        self.assertEqual(roman_number, 'I')

    def test_2(self):
        roman_number = convert_decimal_to_roman(2)
        self.assertEqual(roman_number, 'II')

    def test_3(self):
        roman_number = convert_decimal_to_roman(3)
        self.assertEqual(roman_number, 'III')

    def test_4(self):
        roman_number = convert_decimal_to_roman(4)
        self.assertEqual(roman_number, 'IV')

    def test_5(self):
        roman_number = convert_decimal_to_roman(5)
        self.assertEqual(roman_number, 'V')

    def test_6(self):
        roman_number = convert_decimal_to_roman(6)
        self.assertEqual(roman_number, 'VI')

    def test_7(self):
        roman_number = convert_decimal_to_roman(7)
        self.assertEqual(roman_number, 'VII')

    def test_8(self):
        roman_number = convert_decimal_to_roman(8)
        self.assertEqual(roman_number, 'VIII')

    def test_9(self):
        roman_number = convert_decimal_to_roman(9)
        self.assertEqual(roman_number, 'IX')    

    def test_10(self):
        roman_number = convert_decimal_to_roman(10)
        self.assertEqual(roman_number, 'X')

    def test_11(self):
        roman_number = convert_decimal_to_roman(11)
        self.assertEqual(roman_number, 'XI')

    def test_12(self):
        roman_number = convert_decimal_to_roman(12)
        self.assertEqual(roman_number, 'XII')

    def test_13(self):
        roman_number = convert_decimal_to_roman(13)
        self.assertEqual(roman_number, 'XIII')

    def test_14(self):
        roman_number = convert_decimal_to_roman(14)
        self.assertEqual(roman_number, 'XIV')


    def test_15(self):
        roman_number = convert_decimal_to_roman(15)
        self.assertEqual(roman_number, 'XV')

    def test_19(self):
        roman_number = convert_decimal_to_roman(19)
        self.assertEqual(roman_number, 'XIX')

    def test_20(self):
        roman_number = convert_decimal_to_roman(20)
        self.assertEqual(roman_number, 'XX')

    def test_21(self):
        roman_number = convert_decimal_to_roman(21)
        self.assertEqual(roman_number, 'XXI')
    
    def test_22(self):
        roman_number = convert_decimal_to_roman(22)
        self.assertEqual(roman_number, 'XXII')
    
    def test_23(self):
        roman_number = convert_decimal_to_roman(23)
        self.assertEqual(roman_number, 'XXIII')

    def test_24(self):
        roman_number = convert_decimal_to_roman(24)
        self.assertEqual(roman_number, 'XXIV')

    def test_25(self):
        roman_number = convert_decimal_to_roman(25)
        self.assertEqual(roman_number, 'XXV')
    
    def test_29(self):
        roman_number = convert_decimal_to_roman(29)
        self.assertEqual(roman_number, 'XXIX')
    
    def test_30(self):
        roman_number = convert_decimal_to_roman(30)
        self.assertEqual(roman_number, 'XXX')

    def test_50(self):
        roman_number = convert_decimal_to_roman(50)
        self.assertEqual(roman_number, 'L')

    def test_100(self):
        roman_number = convert_decimal_to_roman(100)
        self.assertEqual(roman_number, 'C')

if __name__ == '__main__':
    unittest.main()