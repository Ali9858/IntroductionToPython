# Задание 1: Определение класса Tile
class Tile:
    pass

# Задание 2: Создание экземпляров класса Tile
tile1 = Tile()
tile2 = Tile()

# Задание 3: Инициализатор класса Tile
class Tile:
    def __init__(self, num):
        self.number = num
my_tile = Tile(3)
your_tile = Tile(4)

# Задание 4: Реализация метода get_number
class Tile:
    def __init__(self, num):
        self.number = num

    def get_number(self):
        return self.number
tile_number = my_tile.get_number()

# Задание 5: Добавление поля exposed и методов для его управления
class Tile:
    def __init__(self, num):
        self.number = num
        self.exposed = False

    def get_number(self):
        return self.number

    def is_exposed(self):
        return self.exposed

    def expose_tile(self):
        self.exposed = True

    def hide_tile(self):
        self.exposed = False

# Задание 6: Реализация метода __str__
class Tile:
    def __init__(self, num, exp=False):
        self.number = num
        self.exposed = exp

    def get_number(self):
        return self.number

    def is_exposed(self):
        return self.exposed

    def expose_tile(self):
        self.exposed = True

    def hide_tile(self):
        self.exposed = False

    def __str__(self):
        return f"Number is {self.number}, exposed is {self.exposed}"
print(my_tile)  # Output: Number is 3, exposed is False

# Задание 7: Добавление расположения плитки и метода draw_tile
class Tile:
    TILE_WIDTH = 100
    TILE_HEIGHT = 100

    def __init__(self, num, x, y, exp=False):
        self.number = num
        self.exposed = exp
        self.x = x
        self.y = y

    def get_number(self):
        return self.number

    def is_exposed(self):
        return self.exposed

    def expose_tile(self):
        self.exposed = True

    def hide_tile(self):
        self.exposed = False

    def __str__(self):
        return f"Number is {self.number}, exposed is {self.exposed}"

    def draw_tile(self, canvas):
        if self.exposed:
            canvas.draw_text(str(self.number), self.x, self.y)
        else:
            canvas.draw_polygon([(self.x, self.y), 
                                 (self.x + self.TILE_WIDTH, self.y), 
                                 (self.x + self.TILE_WIDTH, self.y + self.TILE_HEIGHT), 
                                 (self.x, self.y + self.TILE_HEIGHT)], 
                                1, 'green', 'green')

# Задание 8: Определение метода is_selected
class Tile:
    TILE_WIDTH = 100
    TILE_HEIGHT = 100

    def __init__(self, num, x, y, exp=False):
        self.number = num
        self.exposed = exp
        self.x = x
        self.y = y

    def get_number(self):
        return self.number

    def is_exposed(self):
        return self.exposed

    def expose_tile(self):
        self.exposed = True

    def hide_tile(self):
        self.exposed = False

    def __str__(self):
        return f"Number is {self.number}, exposed is {self.exposed}"

    def draw_tile(self, canvas):
        if self.exposed:
            canvas.draw_text(str(self.number), self.x, self.y)
        else:
            canvas.draw_polygon([(self.x, self.y), 
                                 (self.x + self.TILE_WIDTH, self.y), 
                                 (self.x + self.TILE_WIDTH, self.y + self.TILE_HEIGHT), 
                                 (self.x, self.y + self.TILE_HEIGHT)], 
                                1, 'green', 'green')

    def is_selected(self, pos):
        x1, y1 = pos
        return self.x <= x1 <= self.x + self.TILE_WIDTH and self.y <= y1 <= self.y + self.TILE_HEIGHT

#Avatar
class Avatar:
    def __init__(self, name, hair, initial_gold):
        # Initialize attributes for Avatar
        self.name = name
        self.hair_color = hair
        self.gold_in_bag = initial_gold  # Gold carried in the bag
        self.gold_buried = 0.0  # Gold buried, starts with 0.0

    def find_gold(self, amount):
        # Add the found gold to the Avatar's bag
        self.gold_in_bag += amount

    def bury_gold(self, amount):
        # If there's enough gold in the bag, bury it
        if self.gold_in_bag >= amount:
            self.gold_in_bag -= amount
            self.gold_buried += amount
        else:
            print(f"Not enough gold in the bag to bury {amount}!")

    def sprinkled_with_fairy_dust(self):
        # Increase the gold in the bag by 10%
        self.gold_in_bag *= 1.10

    def __str__(self):
        # Return a string representation of the Avatar's current state
        return f"{self.name}, Hair Color: {self.hair_color}, " \
               f"Gold in Bag: {self.gold_in_bag:.2f}, Gold Buried: {self.gold_buried:.2f}"


# TEST SECTION

wildgirl = Avatar("Wild Girl", "purple", 5.5)
print(wildgirl)
wildgirl.find_gold(2.0)
print(wildgirl)
wildgirl.sprinkled_with_fairy_dust()
print(wildgirl)
wildgirl.bury_gold(2.5)
print("=================================")
print("Check totals here:")
print(wildgirl)
print("=================================")

madmax = Avatar("Mad Max", "black", 6.5)
print(madmax)
madmax.find_gold(25.0)
print(madmax)
madmax.bury_gold(2.0)
madmax.sprinkled_with_fairy_dust()
madmax.bury_gold(4.5)
madmax.sprinkled_with_fairy_dust()
madmax.find_gold(10.0)
madmax.bury_gold(15.0)
madmax.sprinkled_with_fairy_dust()
print("=================================")
print("Check totals here:")
print(madmax)
print("=================================")
