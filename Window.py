import tkinter as tk
import random, time

root = tk.Tk()
root.title('SimpleChance')
current_frame = None

status = {
    'wins':0,
    'loses':0
}


def lose():
    status['loses'] += 1
    load_text_frame('YOU LOSE!')


def win():

    status['wins'] += 1
    load_text_frame('YOU WIN!')


def load_text_frame(text):

    global root
    global current_frame

    current_frame.destroy()

    current_frame = tk.Frame(root)
    current_frame.grid()

    tk.Label(current_frame, text=' ', width=30, height=5).grid(columnspan=3, row=0)
    tk.Label(current_frame, text=text, width=30, height=5).grid(columnspan=3, row=1)
    tk.Label(current_frame, text='Wins: {0} - Loses: {1}'.format(status['wins'], status['loses']), width=30, height=5).grid(columnspan=3, row=2)

    root.after(2000, load_frame)


def reset():
    
    load_text_frame('Reseting score')
    status['wins'] = 0
    status['loses'] = 0


def load_frame():
    global root
    global current_frame

    if current_frame is not None:
        current_frame.destroy()
    
    current_frame = tk.Frame(root)

    current_frame.grid()

    trap_num = random.randint(1, 3)

    if trap_num == 1:
        deur_1 = tk.Button(current_frame, text='1', width=10, height=10, command=lose)
        deur_2 = tk.Button(current_frame, text='2', width=10, height=10, command=win)
        deur_3 = tk.Button(current_frame, text='3', width=10, height=10, command=win)
    elif trap_num == 2:
        deur_1 = tk.Button(current_frame, text='1', width=10, height=10, command=win)
        deur_2 = tk.Button(current_frame, text='2', width=10, height=10, command=lose)
        deur_3 = tk.Button(current_frame, text='3', width=10, height=10, command=win)
    else:
        deur_1 = tk.Button(current_frame, text='1', width=10, height=10, command=win)
        deur_2 = tk.Button(current_frame, text='2', width=10, height=10, command=win)
        deur_3 = tk.Button(current_frame, text='3', width=10, height=10, command=lose)

    tk.Button(current_frame, text='Reset', width=31, height=2, command=reset).grid(columnspan=4, row=1)

    deur_1.grid(column=1, row=2)
    deur_2.grid(column=2, row=2)
    deur_3.grid(column=3, row=2)


load_frame()
root.mainloop()
