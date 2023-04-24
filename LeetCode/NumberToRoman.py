# define the problem: convert an integer given as input into a roman numeral
# what are the rules? 
# 1. I can be placed before V (5) and X (10) to make 4 and 9. 
# 2. X can be placed before L (50) and C (100) to make 40 and 90. 
# 3. C can be placed before D (500) and M (1000) to make 400 and 900.



class Solution:
    def intToRoman(self, num: int) -> str:
        Ints = {
        1 : "I",
        4 : "IV",
        5: "V",
        9: "IX",
        10: "X",
        40: "XL",
        50: "L",
        90: "XC",
        100: "C",
        400: "CD",
        500: "D",
        900: "CM",
        1000: "M"
        }
        num_str = str(num)
        num_digits = len(num_str)
        position_strings = []
        

        for i, digit in enumerate(num_str):
            position = num_digits - i - 1
            if position == 0:
                if int(digit) == 4:
                    fourstr = "IV"
                    position_strings.append(fourstr)
                if int(digit) == 9:
                    ninestr = "IX"
                    position_strings.append(ninestr)
                if int(digit) < 4:
                    threestr = int(digit)*"I"
                    position_strings.append(threestr)
                if int(digit) > 5 and int(digit) != 9:
                    sixstr = "V" + (int(digit)-5)*"I"
                    position_strings.append(sixstr)
                if int(digit) == 5:
                    fivestr = "V"
                    position_strings.append(fivestr)
            elif position == 1:
                if int(digit) == 4:
                    fourstr = "XL"
                    position_strings.append(fourstr)
                if int(digit) == 9:
                    ninestr = "XC"
                    position_strings.append(ninestr)
                if int(digit) < 4:
                    threestr = int(digit)*"X"
                    position_strings.append(threestr)
                if int(digit) > 5 and int(digit) != 9:
                    sixstr = "L" + (int(digit)-5)*"X"
                    position_strings.append(sixstr)
                if int(digit) == 5:
                    fivestr = "L"
                    position_strings.append(fivestr)
            elif position == 2:
                if int(digit) == 4:
                    fourstr = "CD"
                    position_strings.append(fourstr)
                if int(digit) == 9:
                    ninestr = "CM"
                    position_strings.append(ninestr)
                if int(digit) < 4:
                    threestr = int(digit)*"C"
                    position_strings.append(threestr)
                if int(digit) > 5 and int(digit) != 9:
                    sixstr = "D" + (int(digit)-5)*"C"
                    position_strings.append(sixstr)
                if int(digit) == 5:
                    fivestr = "D"
                    position_strings.append(fivestr)
            elif position == 3:
                if int(digit) == 3:
                    fourstr = "MMM"
                    position_strings.append(fourstr)
                if int(digit) == 2:
                    ninestr = "MM"
                    position_strings.append(ninestr)
                if int(digit) == 1:
                    threestr = "M"
                    position_strings.append(threestr)
                if int(digit) > 5 and int(digit) != 9:
                    sixstr = "D" + (int(digit)-5)*"C"
                    position_strings.append(sixstr)
                

        return "".join(position_strings)