import tkinter as tk
from tkinter import ttk
from ctypes import windll
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

import equation
import built_in_integration
import my_integration
import plotting

windll.shcore.SetProcessDpiAwareness(1)

root = tk.Tk()
root.title("")
root.geometry("1600x900")
root.resizable(False, False)

# Задание темы
root.tk.call("source", "common/azure.tcl")
root.tk.call("set_theme", "dark")

root.columnconfigure(index=0, weight=2)
root.columnconfigure(index=1, weight=1)
for index in [0, 2]:
    root.rowconfigure(index=index, weight=1)

graph_frame = ttk.Frame(root)
graph_frame.grid(
    row=0, column=0, sticky="nsew", rowspan=3
)

conditions_frame = ttk.LabelFrame(root, text="Начальные условия", padding=(20, 10))
conditions_frame.grid(
    row=0, column=1, padx=10, pady=(20, 10), sticky="nsew"
)
for index in range(5):
    conditions_frame.rowconfigure(index=index, weight=1)

solve_frame = ttk.Frame(root, padding=(0, 10))
solve_frame.grid(
    row=1, column=1, padx=0, pady=(20, 0), sticky="nsew"
)

answer_frame = ttk.LabelFrame(root, text="Ответ", padding=(20, 10))
answer_frame.grid(
    row=2, column=1, padx=10, pady=(20, 10), sticky="nsew"
)
for index in range(2):
    answer_frame.rowconfigure(index=index, weight=1)

def y(x):
    return 0 * x
fig = plotting.plotting(y, 0, 0)
graph_canvas = FigureCanvasTkAgg(fig, master = graph_frame)
graph_canvas.draw()
graph_canvas.get_tk_widget().grid(row = 0, column = 0)

equation_frame = ttk.Frame(conditions_frame)
equation_frame.grid(
    row=0, column=0, padx=10, pady=(20, 10), sticky="nsew"
)
equation_image = tk.PhotoImage(file='gfx/equation.png')
equation_label = ttk.Label(equation_frame, image=equation_image)
equation_label.grid(
    row=0, column=0, sticky='nsew'
)

U_m_frame = ttk.Frame(conditions_frame)
U_m_frame.grid(
    row=1, column=0, padx=10, pady=(20, 10), sticky='nsew'
)
U_m_label = ttk.Label(U_m_frame, text="U_m = ")
U_m_label.grid(
    row=0, column=0, sticky='nsew'
)
U_m_var = tk.DoubleVar(value=220)
U_m_entry = ttk.Entry(U_m_frame, textvariable=U_m_var)
U_m_entry.grid(
    row=0, column=1, sticky='nsew'
)
U_m_unit_label = ttk.Label(U_m_frame, text="В")
U_m_unit_label.grid(
    row=0, column=2, sticky='nsew'
)

W_frame = ttk.Frame(conditions_frame)
W_frame.grid(
    row=2, column=0, padx=10, pady=(20, 10), sticky='nsew'
)
W_label = ttk.Label(W_frame, text="W = ")
W_label.grid(
    row=0, column=0, sticky='nsew'
)
W_var = tk.DoubleVar(value=1)
W_entry = ttk.Entry(W_frame, textvariable=W_var)
W_entry.grid(
    row=0, column=1, sticky='nsew'
)
W_unit_label = ttk.Label(W_frame, text="Дж")
W_unit_label.grid(
    row=0, column=2, sticky='nsew'
)

T_frame = ttk.Frame(conditions_frame)
T_frame.grid(
    row=3, column=0, padx=10, pady=(20, 10), sticky='nsew'
)
T_label = ttk.Label(T_frame, text="T = ")
T_label.grid(
    row=0, column=0, sticky='nsew'
)
T_var = tk.DoubleVar(value=1)
T_entry = ttk.Entry(T_frame, textvariable=T_var)
T_entry.grid(
    row=0, column=1, sticky='nsew'
)
T_unit_label = ttk.Label(T_frame, text="с")
T_unit_label.grid(
    row=0, column=2, sticky='nsew'
)

optionmenu_frame = ttk.Frame(conditions_frame)
optionmenu_frame.grid(
    row=4, column=0, padx=10, pady=(20, 10), sticky='nsew'
)
optionmenu_list = ["", "Решение встроенной функцией", "Решение реализованной функцией"]
optionmenu_var = tk.StringVar(value=optionmenu_list[1])
optionmenu = ttk.OptionMenu(
    optionmenu_frame, optionmenu_var, *optionmenu_list
)
optionmenu.config(width = 33)
optionmenu.grid(
    row=0, column=0, sticky='nsew'
)

def solve_command():
    U_m = float(U_m_entry.get())
    W = float(W_entry.get())
    T = float(T_entry.get())
    print(type(T))

    if optionmenu_var.get() == "Решение встроенной функцией":
        alpha = built_in_integration.alpha(T)

    if optionmenu_var.get() == "Решение реализованной функцией":
        alpha = my_integration.alpha(T)

    R = equation.R(alpha, U_m, W)

    y = lambda x: equation.u(x, U_m)
    fig = plotting.plotting(y, 0, T)
    graph_canvas = FigureCanvasTkAgg(fig, master = graph_frame)
    graph_canvas.draw()
    graph_canvas.get_tk_widget().grid(row = 0, column = 0)

    R = round(R, 3)
    R_var.set(R)


solve_button = ttk.Button(
    solve_frame, text="Решить", style="Accent.TButton", command=solve_command
)
solve_button.config(width=30)
solve_button.grid(row=0, column=0, padx=(250, 0), sticky="nsew")

R_frame = ttk.Frame(answer_frame)
R_frame.grid(
    row=0, column=0, padx=10, pady=(20, 10), sticky='nsew'
)
R_label = ttk.Label(R_frame, text="R = ")
R_label.grid(
    row=0, column=0, sticky='nsew'
)
R_var = tk.DoubleVar(value=0)
R_entry = ttk.Entry(R_frame, state="readonly", textvariable=R_var)
R_entry.grid(
    row=0, column=1, sticky='nsew'
)
R_unit_label = ttk.Label(R_frame, text="Ом")
R_unit_label.grid(
    row=0, column=2, sticky='nsew'
)

root.update()
x_cordinate = int((root.winfo_screenwidth() / 2) - (root.winfo_width() / 2))
y_cordinate = int((root.winfo_screenheight() / 2) - (root.winfo_height() / 2))
root.geometry("+{}+{}".format(x_cordinate, y_cordinate-20))

root.mainloop()