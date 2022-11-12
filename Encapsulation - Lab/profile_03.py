class Profile:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if not (5 <= len(value) <= 15):
            raise ValueError("The username must be between 5 and 15 characters.")
        self.__username = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        is_length_valid = len(value) >= 8
        has_upper_case = [char for char in value if char.isupper()]
        has_digit = [char for char in value if char.isdigit()]

        if not is_length_valid or not has_upper_case or not has_digit:
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")
        self.__password = value

    def __str__(self):
        return f'You have a profile with username: "{self.username}" and password: {"*" * len(self.__password)}'


# Create a class called Profile. Upon initialization, it should receive:
# • username: str - the username should be between 5 and 15 characters (inclusive).
#   If it is not, raise a ValueError with the message "The username must be between 5 and 15 characters."
# • password: str - the password must be at least 8 characters long; it must contain at least one upper case letter and
#   at least one digit. If it does not, raise a ValueError with the message:
#   "The password must be 8 or more characters with at least 1 digit and 1 uppercase letter."
# Use Getters and Setters to name-mangle them.
#
# Override the __str__() method of the base class, so it returns:
# "You have a profile with username: "{username}" and password: {"*" with the length of password}".
#
#
# Test code:
# profile_with_invalid_password = Profile('My_username', 'My-password')
#
# Expected output:
# ValueError: The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.
#
#
#
# Test code:
profile_with_invalid_username = Profile('Too_long_username', 'Any')
#
#
# Expected output:
# ValueError: The username must be between 5 and 15 characters.
#
#
#
# Test code:
# correct_profile = Profile("Username", "Passw0rd")
# print(correct_profile)
#
#
# Expected output:
# You have a profile with username: "Username" and password: ********
