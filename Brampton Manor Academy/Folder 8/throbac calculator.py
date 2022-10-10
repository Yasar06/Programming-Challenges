def throbac():
    roman_numerals = {"I":1,"V":2,"X":10,"L":50,"C":100}
    first_numeral = input("enter a roman numeral: ")
    second_numeral = input("enter another roman numeral: ")
    first_int = numeral_to_int(first_numeral,roman_numerals)
    second_int = numeral_to_int(second_numeral,roman_numerals)
    intsum = first_int + second_int
    int_to_numeral(intsum,roman_numerals)
    
def numeral_to_int(numeral,roman_numerals):
    integer = 0
    for i in range(len(numeral)):    
        if numeral[i] in roman_numerals:
            integer += (roman_numerals[numeral[i]])
    return integer   

def int_to_numeral(intsum,roman_numerals):
    numeral = ""
    while intsum != 0:        
        while intsum >= 100:
            numeral += list(roman_numerals.keys()[4])

    print(numeral)    
throbac()
