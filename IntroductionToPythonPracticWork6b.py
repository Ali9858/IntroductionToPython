# 1. Реализация класса Person
class Person:
    def __init__(self, first_name, last_name, birth_year):
        """Инициализация объекта Person с именем, фамилией и годом рождения."""
        self.first_name = first_name
        self.last_name = last_name
        self.birth_year = birth_year

    def full_name(self):
        """Возвращает полное имя (имя + фамилия)."""
        return f"{self.first_name} {self.last_name}"

    def age(self, current_year):
        """Возвращает возраст человека на основе текущего года."""
        return current_year - self.birth_year

    def __str__(self):
        """Возвращает строковое представление объекта Person."""
        return f"{self.first_name} {self.last_name}, born in {self.birth_year}"

# Пример использования:
person1 = Person("John", "Doe", 1990)
print(person1.full_name())  # John Doe
print(person1.age(2025))  # 35
print(person1)  # John Doe, born in 1990

# 2. Функция average_age
def average_age(person_list, current_year):
    """Возвращает средний возраст людей в списке."""
    total_age = 0
    for person in person_list:
        total_age += person.age(current_year)
    
    return total_age / len(person_list) if person_list else 0

# Пример использования:
person1 = Person("John", "Doe", 1990)
person2 = Person("Jane", "Doe", 1985)
person_list = [person1, person2]
print(average_age(person_list, 2025))  # 40.0

# 3. Реализация класса Student
class Student:
    def __init__(self, person, password):
        """Инициализация студента с объектом Person и паролем."""
        self.person = person
        self.password = password
        self.projects = []

    def get_name(self):
        """Возвращает полное имя студента."""
        return self.person.full_name()

    def check_password(self, password):
        """Проверяет, совпадает ли введенный пароль с паролем студента."""
        return self.password == password

    def get_projects(self):
        """Возвращает список проектов студента."""
        return self.projects

    def add_project(self, project_name):
        """Добавляет проект в список проектов студента."""
        self.projects.append(project_name)

# Пример использования:
student1 = Student(person1, "securePassword123")
student1.add_project("Project 1")
student1.add_project("Project 2")
print(student1.get_name())  # John Doe
print(student1.get_projects())  # ['Project 1', 'Project 2']
print(student1.check_password("securePassword123"))  # True

# 4. Функция assign
def assign(student_list, full_name, password, project_name):
    """Находит студента по имени и паролю и добавляет проект, если он не существует."""
    for student in student_list:
        if student.get_name() == full_name and student.check_password(password):
            if project_name not in student.get_projects():
                student.add_project(project_name)

# Пример использования:
student1 = Student(person1, "securePassword123")
student2 = Student(person2, "anotherPassword")
students = [student1, student2]
assign(students, "John Doe", "securePassword123", "Project 3")
print(student1.get_projects())  # ['Project 1', 'Project 2', 'Project 3']

# 5. Реализация игры Memory (класс Tile и функции)
import random

class Tile:
    def __init__(self, number):
        """Инициализация плитки с числом."""
        self.number = number
        self.revealed = False

    def reveal(self):
        """Открывает плитку, показывая число."""
        self.revealed = True

    def hide(self):
        """Скрывает плитку."""
        self.revealed = False

    def draw(self):
        """Рисует плитку (если открыта - отображается число)."""
        if self.revealed:
            print(self.number, end=" ")
        else:
            print("X", end=" ")

def new_game():
    """Инициализирует игру Memory с плитками."""
    DISTINCT_TILES = 8  # 8 уникальных чисел
    tiles = [Tile(i) for i in range(DISTINCT_TILES)] * 2
    random.shuffle(tiles)
    return tiles

def draw_board(tiles):
    """Рисует доску с плитками."""
    for i, tile in enumerate(tiles):
        tile.draw()
        if (i + 1) % 4 == 0:
            print()  # Перенос на новую строку после 4 плиток

# Пример использования:
tiles = new_game()
draw_board(tiles)

# Пример клика по плитке
tiles[0].reveal()  # Открывает первую плитку
draw_board(tiles)
