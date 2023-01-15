class Client:
    def __init__(self, phone_number: str):
        self.phone_number = phone_number
        self.shopping_cart = []     # contains all meals added by the client as objects
        self.bill = 0.0     # the total amount of money for all meals that the client has added to his shopping cart
        self.ordered_meals = {}

    @property
    def phone_number(self):
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, value):
        if not value[0] == '0' or len(value) < 10 or not value.isnumeric():
            raise ValueError("Invalid phone number!")
        self.__phone_number = value
