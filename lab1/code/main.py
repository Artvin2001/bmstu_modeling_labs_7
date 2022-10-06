import matplotlib.pyplot as plt
from matplotlib import style
import tkinter as tk
from math import exp
import tkinter.font as font

def uni_func_pl(x, a, b):
    if x < a or x > b:
        return 0
    else:
        return 1 / (b - a)
    
def uni_func(x, a, b):
    if x <= a:
        return 0
    elif x > b:
        return 1
    else:
        return (x - a) / (b - a)

def begin_uni(entry_a, entry_b):
    try:
       a = float(entry_a.get())
       b = float(entry_b.get())
    except:
        tk.messagebox.showerror(title='Ошибка ввода', message='Введите корректные данные')
        return
    
    if (a > b):
        tk.messagebox.showerror(title='Ошибка ввода', message='Левая граница должна быть меньше правой')
        return
    xu1, xu2, xu3 = [], [], []
    xu = []
    yu = []
    yup1, yup2, yup3 = [], [], []
    gr1 = a - (b - a) / 2
    gr2 = b + (b - a) / 2
    i = gr1
    
    while i < gr2:
        if i < a:
            xu1.append(i)
        elif i > b:
            xu3.append(i)
        else:
            xu2.append(i)
        xu.append(i)
        i += (gr2 - gr1) / 100
    for i in range(len(xu)):
        yu.append(uni_func(xu[i], a, b))

    for i in range(len(xu1)):
        yup1.append(uni_func_pl(xu1[i], a, b))

    for i in range(len(xu2)):
        yup2.append(uni_func_pl(xu2[i], a, b))

    for i in range(len(xu3)):
        yup3.append(uni_func_pl(xu3[i], a, b))
        
    fig, ax = plt.subplots(figsize=(5, 3))
    ax.grid()
    plt.plot(xu1, yup1, color='m')
    plt.plot(xu2, yup2, color='m')
    plt.plot(xu3, yup3, color='m')
    plt.title('Функция плотности распределения')

    fig2, ax2 = plt.subplots(figsize=(5, 3))
    ax2.grid()
    plt.plot(xu, yu)
    plt.title('Функция распределения')
    
    plt.show()

def exp_func(x, gamma):
    gamma = -gamma
    if x <= 0:
        return 0
    else:
        return 1 - exp(x * gamma)

def exp_func_pl(x, gamma):
    if x < 0:
        return 0
    else:
        return gamma * exp(x * (-gamma))

def begin_exp(entry_al):
    try:
        gamma = float(entry_al.get())
    except:
        tk.messagebox.showerror(title='Ошибка ввода', message='Введите корректные данные')
        return

    if gamma <= 0:
        tk.messagebox.showerror(title='Ошибка ввода', message='Параметр должен быть больше 0')
        return
    xe = []
    ye = []
    yep = []
    i = 0
    gr2 = 10 / gamma
    
    while i < gr2:
        xe.append(i)
        i += (gr2 + 1) / 100
    for i in range(len(xe)):
        ye.append(exp_func(xe[i], gamma))
        yep.append(exp_func_pl(xe[i], gamma))

    fig, ax = plt.subplots(figsize=(5, 3))
    ax.grid()
    plt.plot(xe, yep, color='m')
    plt.title('Функция плотности распределения')

    fig2, ax2 = plt.subplots(figsize=(5, 3))
    ax2.grid()
    plt.plot(xe, ye)
    plt.title('Функция распределения')
    
    plt.show()

    

def click_start_uni():
    window2 = tk.Tk()
    window2.title('Параметры равномерного распределения')
    window2.geometry('500x200')
    frame1 = tk.Frame(window2, padx=10, pady=10)
    frame1.pack(expand=True)
    label_a = tk.Label(frame1, text= 'a:', bg='lavender')
    label_a.config(font=("Courier", 16))
    label_a.pack()

    window2.configure(background='lavender')
    frame1.configure(background='lavender')

    entry_a = tk.Entry(frame1)
    entry_a.pack()

    label_b = tk.Label(frame1, text= 'b:', bg='lavender')
    label_b.config(font=("Courier", 16))
    label_b.pack()

    entry_b = tk.Entry(frame1)
    entry_b.pack()

    graph_but = tk.Button(frame1, text='Построить',
                          command=lambda :begin_uni(entry_a, entry_b), bg='SeaGreen3')
    graph_but.config(font=("Courier", 16))
    graph_but.pack()
    window2.mainloop()

def click_start_exp():
    window3 = tk.Tk()
    window3.title('Параметры экспоненциального распределения')
    window3.geometry('500x200')
    frame2 = tk.Frame(window3, padx=10, pady=10)
    frame2.pack(expand=True)
    label_al = tk.Label(frame2, text= 'Гамма:', bg='lavender')
    label_al.config(font=("Courier", 16))
    label_al.pack()

    window3.configure(background='lavender')
    frame2.configure(background='lavender')
    
    entry_al = tk.Entry(frame2)
    entry_al.pack()
    graph_but = tk.Button(frame2, text='Построить',
                          command=lambda :begin_exp(entry_al), bg='pink')
    graph_but.config(font=("Courier", 16))
    graph_but.pack()
    window3.mainloop()

window = tk.Tk()
window.title('Приложение')
window.geometry('600x300')

frame = tk.Frame(window, padx=10, pady=10)
frame.pack(expand=True)
window.configure(background='lavender')
frame.configure(background='lavender')

label1 = tk.Label(frame, text='Выберите вид распределения', bg='lavender')
label1.config(font=("Courier", 16))
label1.pack()
uni_but = tk.Button(frame, text='Равномерное распределение',
                         command=click_start_uni, width = 30, height = 3, padx=10, pady=10, bg='SeaGreen3')
uni_but.config(font=("Courier", 16))
uni_but.pack()
exp_but = tk.Button(frame, text='Экспоненциальное распределение',
                         command=click_start_exp, width = 30, height = 3, padx=10, pady=10, bg = 'pink')
exp_but.config(font=("Courier", 16))
exp_but.pack()


window.mainloop()
