class FancyShoppingListDL:
    def __init__(self, food, amount):
        self.food = food
        self.amount = amount
        self._standard_prices = self._price_listDL()
        self._standard_price_per_pound = self._get_standard_priceDL()
        self._calculated_price = self.calculate_costDL()

    def _price_listDL(self):
        prices = {
            'Dry Cured Iberian Ham': 177.80,
            'Wagyu Steaks': 450.00,
            'Matsutake Mushrooms': 272.00,
            'Kopi Luwak Coffee': 306.50,
            'Moose Cheese': 487.20,
            'White Truffles': 3600.00,
            'Blue Fin Tuna': 3603.00,
            'Le Bonnotte Potatoes': 270.81
        }
        return prices

    def _get_standard_priceDL(self):
        if self.food in self._standard_prices:
            return self._standard_prices[self.food]
        else:
            return 0.00

    def calculate_costDL(self):
        return self.amount * self._standard_price_per_pound

    def __str__(self):
        return f"Item: {self.food}\nAmount ordered: {self.amount:.1f} pounds\n" \
               f"Price per pound: ${self._standard_price_per_pound:.2f}\n" \
               f"Price of order: ${self._calculated_price:.2f}"
 