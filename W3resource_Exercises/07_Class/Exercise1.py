class ConvertToRomanNumeral:
    # Method convert
    def convert(self, n):
        val = [ 
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
            ]
        syb = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
            ]
        roman = ''
        i = 0
        while n > 0:
            for x in range(n // val[i]):
                roman += syb[i]
                n -= val[i]
            i += 1
        return roman

                 
# main
roman = ConvertToRomanNumeral().convert(3986)
print(roman)
       

    