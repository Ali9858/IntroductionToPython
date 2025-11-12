import tkinter as tk
import math

"""Решение "Mouse Echo" (Щелчки мышью)"""
def on_click(event):
    print(f"Mouse clicked at ({event.x}, {event.y})")
root = tk.Tk()
# Отображаем окно
root.geometry("400x400")
root.bind("<Button-1>", on_click)  # Слушаем левый щелчок мыши
root.mainloop()


"""Решение "Щелчок по окружности"""
# Функция для вычисления расстояния между точкой и центром окружности
def dist(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
# Функция, которая обрабатывает щелчки мышью
def on_click(event):
    for i, circle in enumerate(circles):
        x, y, r, color = circle
        if dist(event.x, event.y, x, y) <= r:
            print(f"Clicked inside {color} circle")
            break
root = tk.Tk()
root.geometry("400x400")
# Определяем три окружности с разными центрами и радиусами
circles = [
    (100, 100, 50, "red"),
    (300, 100, 50, "green"),
    (200, 300, 50, "blue")
]
# Рисуем окружности
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()
for x, y, r, color in circles:
    canvas.create_oval(x - r, y - r, x + r, y + r, fill=color)
# Обработчик щелчков
canvas.bind("<Button-1>", on_click)
root.mainloop()

"""Решение для функции day_to_number"""
day_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
def day_to_number(day):
    try:
        return day_list.index(day)
    except ValueError:
        return -1  # Если дня нет в списке
# Пример использования
print(day_to_number("Wednesday"))  # Выведет: 2
print(day_to_number("Holiday"))    # Выведет: -1

"""Решение для функции string_list_join"""
def string_list_join(string_list):
    result = ""
    for s in string_list:
        result += s
    return result
# Пример использования
string_list = ["Hello", " ", "World", "!"]
print(string_list_join(string_list))  # Выведет: "Hello World!"


"""Решение для создания сетки из шаров"""
def draw_balls(canvas, ball_radius):
    for i in range(10):  # Внешний цикл
        for j in range(10):  # Внутренний цикл
            x = ball_radius + i * (2 * ball_radius + 10)  # X координата
            y = ball_radius + j * (2 * ball_radius + 10)  # Y координата
            canvas.create_oval(x - ball_radius, y - ball_radius,
                               x + ball_radius, y + ball_radius,
                               fill="blue")
root = tk.Tk()
root.geometry("600x600")
canvas = tk.Canvas(root, width=600, height=600)
canvas.pack()
# Рисуем сетку из шаров
draw_balls(canvas, ball_radius=20)
root.mainloop()


""""Решение для рисования полилинии с кнопкой "Очистить"""
# Список для хранения точек
points = []
def on_click(event):
    points.append((event.x, event.y))
    if len(points) > 1:
        canvas.create_line(points[-2], points[-1], fill="black")
def clear_drawing():
    global points
    points = []  # Очищаем список точек
    canvas.delete("all")  # Удаляем все объекты на холсте
root = tk.Tk()
root.geometry("400x400")
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()
# Обработчик щелчков
canvas.bind("<Button-1>", on_click)
# Кнопка для очистки
clear_button = tk.Button(root, text="Clear", command=clear_drawing)
clear_button.pack()
root.mainloop()

