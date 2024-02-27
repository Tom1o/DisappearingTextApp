import tkinter as tk

FONT = 'TimesNewRoman 20 bold'


def countdown_five():
    global countdown
    timer_canvas.delete('all')
    timer_canvas.create_text(25, 25, anchor='center', text='5', font='Impact 40 bold', fill='red')

    countdown = window.after(1000, countdown_four)


def countdown_four():
    global countdown
    timer_canvas.delete('all')
    timer_canvas.create_text(25, 25, anchor='center', text='4', font='Impact 40 bold', fill='red')

    countdown = window.after(1000, countdown_three)


def countdown_three():
    global countdown
    timer_canvas.delete('all')
    timer_canvas.create_text(25, 25, anchor='center', text='3', font='Impact 40 bold', fill='red')

    countdown = window.after(1000, countdown_two)


def countdown_two():
    global countdown
    timer_canvas.delete('all')
    timer_canvas.create_text(25, 25, anchor='center', text='2', font='Impact 40 bold', fill='red')
    countdown = window.after(1000, countdown_one)


def countdown_one():
    global countdown
    timer_canvas.delete('all')
    timer_canvas.create_text(25, 25, anchor='center', text='1', font='Impact 40 bold', fill='red')
    countdown = window.after(1000, countdown_end)


def countdown_end():
    global countdown, typed_chars
    timer_canvas.delete('all')
    text_canvas.delete('all')
    typed_chars = []
    countdown_five()


def print_typed_chars():
    global typed_chars, text
    text_canvas.delete('all')
    full_text = ''.join(typed_chars)
    text = text_canvas.create_text(10, 25, anchor='nw', text=full_text, font=FONT)


def add_letter(key):
    global typed_chars
    number_of_lines = len(typed_chars) // 60
    if number_of_lines > typed_chars.count('\n'):
        try:
            last_space = typed_chars[::-1].index(' ')
        except ValueError:
            typed_chars += "\n"
        else:
            typed_chars[(last_space * -1) - 1] = '\n'
    typed_chars += key.char
    print_typed_chars()


def backspace():
    global typed_chars
    if typed_chars is None:
        pass
    else:
        text_canvas.delete('all')
        typed_chars = typed_chars[0:(len(typed_chars) - 1)]
        print_typed_chars()


def key_press(key):
    global typed_chars
    if countdown is None:
        pass
    else:
        window.after_cancel(countdown)
    if key.keysym == 'BackSpace':
        backspace()
    elif key.keysym == 'Tab':
        pass
    elif key.keysym == 'Return':
        left_in_line = 60 - (len(typed_chars) % 60)
        for n in range(left_in_line):
            typed_chars += ' '
    else:
        add_letter(key)
    countdown_five()
    if len(typed_chars) > 1200:
        save_work(typed_chars)


def save_work(text_list):
    global countdown
    window.after_cancel(countdown)
    window.bind('<KeyPress>', '')
    with open("text.txt", mode="w") as file:
        text_str = ''.join(text_list)
        file.write(text_str)


typed_chars = []

window = tk.Tk()
window.minsize(800, 600)
window.title('Disappearing Text App')

window.bind('<KeyPress>', key_press)

timer_canvas = tk.Canvas(window, width=50, height=50)
timer_canvas.place(x=375, y=0)
timer_text = timer_canvas.create_text(25, 25, anchor='center', text='5', font='Impact 40 bold', fill='red')

text_canvas = tk.Canvas(window, width=750, height=500)
text_canvas.place(x=50, y=50)
text = text_canvas.create_text(10, 25, anchor='nw',
                               text="If you leave it more than 5 seconds between key presses\n"
                                    " your text will be deleted!\n\nIf you fill the page before the "
                                    "timer runs out,\nyour work will be saved!\n\nStart typing to begin the timer!\n\n"
                                    "Good Luck!",
                               font=FONT)


countdown = None

window.mainloop()
