class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        n = self.size
        list = []
        while n > 0:
            list.append("🍪")
            n = n - 1
        emoji = "".join(list)
        return emoji

    def deposit(self, n):
        self.size = self.size + n

    def withdraw(self, n):
       self.size = self.size - n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0:
            raise ValueError
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if size > self.capacity:
            raise ValueError
        if size < 0:
            raise ValueError
        self._size = size


jar = Jar(10)
"""print(jar.capacity)
print(jar.size)"""

while True:
    x = input("What do? ")
    if x == "d":
        n = int(input("How many? "))
        jar.deposit(n)
    elif x == "w":
        n = int(input("How many? "))
        jar.withdraw(n)
    print(jar)

