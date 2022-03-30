class InventoryControl:
    INGREDIENTS = {
        'hamburguer': ['pao', 'carne', 'queijo'],
        'pizza': ['massa', 'queijo', 'molho'],
        'misto-quente': ['pao', 'queijo', 'presunto'],
        'coxinha': ['massa', 'frango'],
    }
    MINIMUM_INVENTORY = {
        'pao': 50,
        'carne': 50,
        'queijo': 100,
        'molho': 50,
        'presunto': 50,
        'massa': 50,
        'frango': 50,
    }

    def __init__(self):
        self.minimum = {
            'pao': 50,
            'carne': 50,
            'queijo': 100,
            'molho': 50,
            'presunto': 50,
            'massa': 50,
            'frango': 50,
        }
        self.stock = {
            'pao': 50,
            'carne': 50,
            'queijo': 100,
            'molho': 50,
            'presunto': 50,
            'massa': 50,
            'frango': 50,
        }
        self.ingredients = {
            'hamburguer': ['pao', 'carne', 'queijo'],
            'pizza': ['massa', 'queijo', 'molho'],
            'misto-quente': ['pao', 'queijo', 'presunto'],
            'coxinha': ['massa', 'frango'],
        }
        self.cart = set(['hamburguer', 'pizza', 'misto-quente', 'coxinha'])

    def add_new_order(self, customer, order, day):
        for ingredient in self.ingredients[order]:
            if self.stock[ingredient] == 0:
                return False
            self.stock[ingredient] -= 1

    def get_quantities_to_buy(self):
        ingredients_to_buy = {
            'pao': 0,
            'carne': 0,
            'queijo': 0,
            'molho': 0,
            'presunto': 0,
            'massa': 0,
            'frango': 0,
        }
        for ingredient in ingredients_to_buy:
            minimum_ammount = self.minimum[ingredient]
            in_stock = self.stock[ingredient]
            ingredients_to_buy[ingredient] = minimum_ammount - in_stock
        return ingredients_to_buy

    def get_available_dishes(self):
        available_dishes = self.cart
        sold_off_ingredients = set()
        for ingredient in self.stock:
            if self.stock[ingredient] == 0:
                sold_off_ingredients.add(ingredient)
        for dish in self.ingredients:
            ingredients = set(self.ingredients[dish])
            disjointed = ingredients.isdisjoint(sold_off_ingredients)
            if disjointed is False:
                available_dishes.discard(dish)
        return available_dishes
