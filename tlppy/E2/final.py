class Character:
    def __init__(self):
        self.health = 100
        self.coins = 0
        self.diamonds = 0

    def get_health(self):
        return self.health

    def get_coins(self):
        return self.coins

    def add_coins(self, amount):
        self.coins += amount
        self.health += amount // 10  # 1 health for every 10 coins

        while self.coins >= 200:
            self.coins -= 200
            self.diamonds += 1

    def lose_health(self, amount):
        self.health -= amount
        if self.health < 0:
            self.health = 0

    def is_alive(self):
        return self.health > 0

    def has_diamond(self):
        return self.diamonds > 0

    def get_status(self):
        return f"Health: {self.health}, Coins: {self.coins}, Diamonds: {self.diamonds}"
