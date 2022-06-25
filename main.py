from tkinter import *
from tkinter import messagebox
import time
import random

#  Инициализация переменных
GameRunning = True  # Флаг запуска игры
WindowGame = Tk()
size_canvas_x = 600
size_canvas_y = 600
s_x = s_y = 3  # размер игрового поля
step_x = size_canvas_x // s_x  # размер шагов между ячейками
step_y = size_canvas_y // s_y
field = [[""] * 3 for i in range(3)]
NextGamer = True
countPlay = 0
player_win = ai_win = False


# --------------------------------------  Функция закрытия окна  -------------------------------------------------------
def closeWindow():
    global GameRunning
    if messagebox.askokcancel("Выход из игры", "Хотите выйти из игры?"):
        GameRunning = False
        WindowGame.destroy()
# ---------------------------------------------------------------------------------------------


WindowGame.protocol("WM_DELETE_WINDOW", closeWindow)
WindowGame.title('Игра "Крестики - нолики" ')
WindowGame.resizable(False, False)  # по x и y менять размер не можем
WindowGame.wm_attributes("-topmost", 1)  # поверх всех окон
canvas = Canvas(WindowGame, width=size_canvas_x, height=size_canvas_y, bd=0, highlightthickness=0)
canvas.create_rectangle(0, 0, size_canvas_x, size_canvas_y, fill="white")
canvas.pack()
WindowGame.update()


# ----------------------------  Функция отрисовки сетки игрового поля  -----------------------------
def drawField():
    for i in range(0, s_x + 1):
        canvas.create_line(step_x * i, 0, step_x * i, size_canvas_y)
        canvas.create_line(0, step_y * i, size_canvas_x, step_y * i)
# --------------------------------------------------------------------------------------------------


# ------------------------------  Функция определения выигрыша  ------------------------------------
def get_win_check(fd, symbol):
    flag_win = False
    for line in fd:
        if line.count(symbol) == 3:
            flag_win = True
    for i in range(3):
        if fd[0][i] == fd[1][i] == fd[2][i] == symbol:
            flag_win = True
    if fd[0][0] == fd[1][1] == fd[2][2] == symbol:
        flag_win = True
    if fd[0][2] == fd[1][1] == fd[2][0] == symbol:
        flag_win = True
    return flag_win
# --------------------------------------------------------------------------------------------------


# -----------------------------  Функция отрисовки нолика Player  ----------------------------------
def draw_O(x, y):
    size = 25
    global field, countPlay
    canvas.create_oval(x * step_x + 5, y * step_y + 5, x * step_x + step_x - 5, y * step_y + step_y - 5, fill="red")
    canvas.create_oval(x * step_x + size, y * step_y + size, x * step_x + step_x - size, y * step_y + step_y - size, fill="white")
    field[y][x] = "0"
    countPlay += 1
# --------------------------------------------------------------------------------------------------


# -----------------------------  Функция отрисовки крестика AI--------------------------------------
def draw_x(x, y):
    global field, countPlay
    canvas.create_line(x * step_x + 5, y * step_y + 5, x * step_x + step_x - 5, y * step_y + step_y - 5, width=10.0, fill="blue")
    canvas.create_line(x * step_x + 5, y * step_y + step_y - 5, x * step_x + step_x - 5, y * step_y + 5, width=10.0, fill="blue")
    field[y][x] = "x"
    countPlay += 1
# --------------------------------------------------------------------------------------------------


# ----------------------------  Функция определения координат клика мышки на поле-------------------
def add_to_points(event):
    mouse_x = canvas.winfo_pointerx() - canvas.winfo_rootx()
    mouse_y = canvas.winfo_pointery() - canvas.winfo_rooty()
    ip_x = mouse_x // step_x
    ip_y = mouse_y // step_y
    if field[ip_y][ip_x] == "" and countPlay < 9:
        draw_O(ip_x, ip_y)
# --------------------------------------------------------------------------------------------------


drawField()
canvas.bind_all("<Button-1>", add_to_points)

while GameRunning:
    if GameRunning:
        WindowGame.update_idletasks()
        WindowGame.update()
    ai_win = get_win_check(field, "x")
    player_win = get_win_check(field, "0")
    if player_win or ai_win:
        if player_win:
            messagebox.showinfo("Победа", "Поздравляем! Вы победили!")
            GameRunning = False
            WindowGame.destroy()
        else:
            messagebox.showerror("Поражение...", "К сожалению вы проиграли...")
            GameRunning = False
            WindowGame.destroy()
    if countPlay == 9 and player_win == ai_win == False:
        messagebox.showinfo("Ничья", "Ничья")
        GameRunning = False
        WindowGame.destroy()
    x, y = random.randint(0, 2), random.randint(0, 2)
    if countPlay % 2 == 1 and field[x][y] == "" and countPlay < 8 and not (player_win or ai_win):
        draw_x(y, x)
    else:
        x, y = random.randint(0, 2), random.randint(0, 2)







