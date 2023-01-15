from project.meals.meal import Meal
from project.client import Client


class FoodOrdersApp:
    receipt_id = 0

    def __init__(self):
        self.menu = []      # contains all the meals as objects
        self.clients_list = []      # contains all the clients as objects

    def __find_client_by_phone_number_and_return_it(self, phone_number: str):
        for client in self.clients_list:
            if client.phone_number == phone_number:
                return client

    def __check_if_menu_is_ready(self):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

    def __check_if_meals_exist(self, **meals):
        for meal in meals.keys():
            if meal not in [m.name for m in self.menu]:
                raise Exception(f"{meal} is not on the menu!")

    def __check_if_enough_meal_quantities(self, **meals):
        for m, quantity in meals.items():
            for meal in self.menu:
                if m == meal.name:
                    if quantity > meal.quantity:
                        raise Exception(f"Not enough quantity of {meal.__class__.__name__}: {m}!")

    def __make_client_order(self, client: Client, **meals):
        current_order = []
        for client_meal, client_meal_quantity in meals.items():
            for meal in self.menu:
                if client_meal == meal.name:
                    meal.quantity -= client_meal_quantity
                    client.shopping_cart.append(meal)
                    current_order.append(client_meal)
                    client.ordered_meals[client_meal] = client_meal_quantity
                    client.bill += meal.price * client_meal_quantity
                    break
        return f"Client {client.phone_number} successfully ordered {', '.join(client.ordered_meals.keys())} for " \
               f"{client.bill:.2f}lv."

    @staticmethod
    def __reset_client_orders_shopping_cart_and_bill(client: Client):
        client.ordered_meals = {}
        client.shopping_cart = []
        client.bill = 0.0

    @staticmethod
    def __check_client_shopping_cart(client: Client):
        if not client.shopping_cart:
            raise Exception("There are no ordered meals!")

    def register_client(self, client_phone_number: str):
        client = self.__find_client_by_phone_number_and_return_it(client_phone_number)

        if client:
            raise Exception("The client has already been registered!")

        self.clients_list.append(Client(client_phone_number))

        return f"Client {client_phone_number} registered successfully."

    def add_meals_to_menu(self, *meals: Meal):
        for meal in meals:
            if meal.__class__.__name__ in ["Starter", "MainDish", "Dessert"]:
                self.menu.append(meal)

    def show_menu(self):
        self.__check_if_menu_is_ready()

        result = []
        for meal in self.menu:
            result.append(meal.details())

        return '\n'.join(result)

    def add_meals_to_shopping_cart(self, client_phone_number: str, **meal_names_and_quantities):
        self.__check_if_menu_is_ready()
        client = self.__find_client_by_phone_number_and_return_it(client_phone_number)

        if not client:
            self.register_client(client_phone_number)

        client = self.__find_client_by_phone_number_and_return_it(client_phone_number)
        self.__check_if_meals_exist(**meal_names_and_quantities)
        self.__check_if_enough_meal_quantities(**meal_names_and_quantities)

        return self.__make_client_order(client, **meal_names_and_quantities)

    def cancel_order(self, client_phone_number: str):
        client = self.__find_client_by_phone_number_and_return_it(client_phone_number)

        self.__check_client_shopping_cart(client)

        for client_meal, client_meal_quantity in client.ordered_meals.items():
            for meal in self.menu:
                if client_meal == meal.name:
                    meal.quantity += client_meal_quantity
                    break

        self.__reset_client_orders_shopping_cart_and_bill(client)

        return f"Client {client_phone_number} successfully canceled his order."

    def finish_order(self, client_phone_number: str):
        client = self.__find_client_by_phone_number_and_return_it(client_phone_number)

        self.__check_client_shopping_cart(client)
        FoodOrdersApp.receipt_id += 1
        message = f"Receipt #{FoodOrdersApp.receipt_id} with total amount of {client.bill:.2f} was successfully " \
                  f"paid for {client_phone_number}."

        self.__reset_client_orders_shopping_cart_and_bill(client)

        return message

    def __str__(self):
        return f"Food Orders App has {len(self.menu)} meals on the menu and {len(self.clients_list)} clients."
