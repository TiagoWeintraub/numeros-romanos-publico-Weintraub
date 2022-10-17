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