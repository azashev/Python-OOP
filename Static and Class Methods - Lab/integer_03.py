class Integer:
    def __init__(self, value: int):
        self.value = value

    @classmethod
    def from_float(cls, float_value):
        if not isinstance(float_value, float):
            return "value is not a float"
        return cls(int(float_value))

    @classmethod
    def from_roman(cls, value):
        roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        for i, c in enumerate(value):
            if (i + 1) == len(value) or roman_numerals[c] >= roman_numerals[value[i + 1]]:
                result += roman_numerals[c]
            else:
                result -= roman_numerals[c]
        return cls(result)

    @classmethod
    def from_string(cls, value):
        try:
            if not isinstance(value, str):
                raise ValueError
            return cls(int(value))
        except ValueError:
            return "wrong type"


# Create a class called Integer. Upon initialization, it should receive a single parameter value (int).
# It should have 3 additional methods:
# • from_float(float_value) - creates a new instance by flooring the provided floating number. If the value is not a
#   float, return a message "value is not a float"
# • from_roman(value) - creates a new instance by converting the roman number (as string) to an integer
# • from_string(value) - creates a new instance by converting the string to an integer (if the value cannot be
#   converted, return a message "wrong type")
#
#
# Test code:
first_num = Integer(10)
print(first_num.value)

second_num = Integer.from_roman("IV")
print(second_num.value)

print(Integer.from_float("2.6"))
print(Integer.from_string(2.6))

#
# Expected output:
# 10
# 4
# value is not a float
# wrong type
