import datetime


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


class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.timestamp = datetime.datetime.now()

    def signed_up_on(self):
        delta = datetime.datetime.now() - self.timestamp
        secs_since = int(delta.total_seconds())
        return f"{self.username} signed up {secs_since} seconds ago."


class Nakama(User):
    def __init__(self, username, email, division="Sales"):
        super().__init__(username, email)
        self.division = division

    def signed_up_on(self):
        res = super().signed_up_on()
        additional = f"{self.username} is a {self.division} employee."
        return res, additional


import time

adam = User(username="kadiB", email="kadi_b@hollywood.com")
andi = Nakama(username="lauluv2sing", email="andi@tokopedia.com")
time.sleep(3)
print(adam.signed_up_on())
time.sleep(1)
print(andi.signed_up_on())
# print(help(Nakama))
print(isinstance(adam, Nakama))
print(isinstance(andi, Nakama))
print(issubclass(Nakama, User))
