class MoneyBox:
    def __init__(self, capacity):
        self.capacity = capacity

    def can_add(self, v):
        if v <= self.capacity:
            return True
        if v > self.capacity:
            return False

    def add(self, v):
        self.capacity -= v
        return self.capacity

x = MoneyBox(10)
x.add(9)
print(x.can_add(2))