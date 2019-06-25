class Inventory:
    listed = False

    def __init__(self, name, price, discount):
        self.name = name
        self.price = int(price)
        self.discount = int(discount)
        self.headline = f"{name} at {self.net_price()} IDR today!"

    def net_price(self):
        return self.price - self.discount

    @classmethod
    def toggle_list(cls):
        cls.listed = not cls.listed

    @classmethod
    def from_string(cls, string):
        """
        Alternative constructor method
        """
        name, price, discount = string.split("_")
        return cls(name, price, discount)

    @staticmethod
    def inventory_updated(num_of_days):
        import datetime

        return datetime.datetime.now() - datetime.timedelta(days=num_of_days)


# pilotpen = Inventory(name="pilot pen", price=15000, discount="5000")
# print(pilotpen.headline)

journal = Inventory.from_string("mujijournal_50000_5000")
print(journal.headline)
print(journal.listed)
Inventory.toggle_list()
print(journal.listed)

print(Inventory.inventory_updated(2))
print(Inventory.inventory_updated(3))

