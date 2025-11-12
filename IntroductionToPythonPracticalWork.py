import math
import random

def miles_to_feet(miles):
    """Преобразует мили в футы."""
    feet_in_mile = 5280  # 1 миля = 5280 футов
    return miles * feet_in_mile
print(miles_to_feet(1))   # 5280
print(miles_to_feet(3.5)) # 18480.0

def total_seconds(hours, minutes, seconds):
    """Возвращает общее количество секунд для заданных часов, минут и секунд."""
    return hours * 3600 + minutes * 60 + seconds
print(total_seconds(1, 0, 0))     # 3600
print(total_seconds(0, 1, 30))    # 90
print(total_seconds(2, 30, 15))   # 9015

def rectangle_perimeter(width, height):
    """Возвращает периметр прямоугольника в дюймах."""
    return 2 * (width + height)
print(rectangle_perimeter(5, 3))   # 16
print(rectangle_perimeter(10, 2.5)) # 25.0

def rectangle_area(width, height):
    """Возвращает площадь прямоугольника в квадратных дюймах."""
    return width * height
print(rectangle_area(5, 3))    # 15
print(rectangle_area(10, 2.5)) # 25.0

def circle_circumference(radius):
    """Возвращает окружность круга с заданным радиусом в дюймах."""
    return 2 * math.pi * radius
print(circle_circumference(1))   # 6.283185307179586
print(circle_circumference(5))   # 31.41592653589793

def circle_area(radius):
    """Возвращает площадь круга с заданным радиусом в квадратных дюймах."""
    return math.pi * radius ** 2
print(circle_area(1))   # 3.141592653589793
print(circle_area(5))   # 78.53981633974483

def future_value(present_value, annual_rate, years):
    """
    Возвращает будущую стоимость инвестиций.

    :param present_value: начальная сумма в долларах
    :param annual_rate: годовая процентная ставка (например, 0.05 для 5%)
    :param years: количество лет инвестирования
    :return: будущая стоимость через заданное количество лет
    """
    # Вычисляем будущую стоимость с учетом ежегодного сложного процента
    return present_value * (1 + annual_rate) ** years
# ----------------------------
# Примеры использования функции
# ----------------------------

# Пример 1: Инвестируем $1000 под 5% на 10 лет
fv1 = future_value(1000, 0.05, 10)
print(f"Будущая стоимость $1000 через 10 лет при 5% годовых: ${fv1:.2f}")

# Пример 2: Инвестируем $500 под 7% на 5 лет
fv2 = future_value(500, 0.07, 5)
print(f"Будущая стоимость $500 через 5 лет при 7% годовых: ${fv2:.2f}")

# Пример 3: Инвестируем $2000 под 3% на 15 лет
fv3 = future_value(2000, 0.03, 15)
print(f"Будущая стоимость $2000 через 15 лет при 3% годовых: ${fv3:.2f}")

def name_tag(first_name, last_name):
    """
    Возвращает строку вида "My name is <first_name> <last_name>."
    
    :param first_name: имя (строка)
    :param last_name: фамилия (строка)
    :return: строка с тегом имени
    """
    return f"My name is {first_name} {last_name}."
print(name_tag("John", "Doe"))    # My name is John Doe.
print(name_tag("Alice", "Smith")) # My name is Alice Smith.
print(name_tag("Иван", "Иванов")) # My name is Иван Иванов.

def name_and_age(name, age):
    """
    Возвращает строку вида "<name> is <age> years old."
    
    :param name: имя (строка)
    :param age: возраст (число)
    :return: строка с именем и возрастом
    """
    return f"{name} is {age} years old."
print(name_and_age("John", 25))   # John is 25 years old.
print(name_and_age("Alice", 30))  # Alice is 30 years old.
print(name_and_age("Иван", 40))   # Иван is 40 years old.


def point_distance(x0, y0, x1, y1):
    """
    Возвращает расстояние между точками (x0, y0) и (x1, y1).
    
    :param x0: координата x первой точки
    :param y0: координата y первой точки
    :param x1: координата x второй точки
    :param y1: координата y второй точки
    :return: расстояние между точками
    """
    return math.sqrt((x1 - x0) ** 2 + (y1 - y0) ** 2)
print(point_distance(0, 0, 3, 4))  # 5.0
print(point_distance(1, 2, 4, 6))  # 5.0
print(point_distance(-1, -1, 2, 3)) # 5.0

def triangle_area(x0, y0, x1, y1, x2, y2):
    """
    Возвращает площадь треугольника с вершинами (x0, y0), (x1, y1), (x2, y2).
    
    :param x0, y0: координаты первой вершины
    :param x1, y1: координаты второй вершины
    :param x2, y2: координаты третьей вершины
    :return: площадь треугольника
    """
    return abs((x0*(y1 - y2) + x1*(y2 - y0) + x2*(y0 - y1)) / 2)
print(triangle_area(0, 0, 4, 0, 0, 3))  # 6.0
print(triangle_area(1, 1, 4, 1, 1, 5))  # 6.0
print(triangle_area(-1, -1, 2, -1, -1, 3)) # 6.0

def print_digits(number):
    """
    Печатает сообщение о цифрах десятков и единиц числа от 0 до 99.
    
    :param number: целое число в диапазоне [0, 100)
    """
    if not (0 <= number < 100):
        print("Error: number must be in the range [0, 100).")
        return

    tens = number // 10   # цифра десятков
    ones = number % 10    # цифра единиц

    print(f"The tens digit is {tens}, and the ones digit is {ones}.")
print_digits(0)   # The tens digit is 0, and the ones digit is 0.
print_digits(7)   # The tens digit is 0, and the ones digit is 7.
print_digits(42)  # The tens digit is 4, and the ones digit is 2.
print_digits(99)  # The tens digit is 9, and the ones digit is 9.



def powerball():
    """
    Печатает случайные числа Powerball.
    Первые пять чисел: от 1 до 59 (включительно)
    Номер Powerball: от 1 до 35 (включительно)
    """
    # Генерируем пять чисел для "обычных" номеров
    numbers = [random.randrange(1, 60) for _ in range(5)]

    # Генерируем номер Powerball
    powerball_number = random.randrange(1, 36)

    # Печатаем сообщение в нужном формате
    print(f"Today's numbers are {numbers[0]}, {numbers[1]}, {numbers[2]}, {numbers[3]}, and {numbers[4]}. The Powerball number is {powerball_number}.")
powerball()
# Пример вывода:
# Today's numbers are 12, 45, 7, 33, and 19. The Powerball number is 8.

