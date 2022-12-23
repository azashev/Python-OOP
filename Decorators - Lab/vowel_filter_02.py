# Having the following code:
#
# def vowel_filter(function):
#
#     def wrapper():
#
#         # TODO: Implement
#
#     return wrapper
#
#
# Complete the code, so it works as expected:
#
# Test code:
# @vowel_filter
# def get_letters():
#     return ["a", "b", "c", "d", "e"]
#
# print(get_letters())

# Expected output:
# ["a", "e"]


def vowel_filter(func_ref):
    vowels = "eyuioa"

    def wrapper():
        result = func_ref()
        filtered = [x for x in result if x.lower() in vowels]

        return filtered

    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


print(get_letters())
