import tkinter as tk
import tkinter.font as tkFont


def factorial(n):
    if n < 0:
        return "Not Possible"

    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)




def on_change(e):
    a = e.widget.get()
    fact = factorial(int(a))
    return tk.Label(root, text="The factorial of " + str(a) + " is: \n " + str(fact), font=fontStyle).pack()


root = tk.Tk()
root.title("Factorial")
fontStyle = tkFont.Font(family="Times New Roman", size="14")
tk.Label(root, text="Enter the number(Integer) and press Enter: ", font=fontStyle).pack()
e = tk.Entry(root, width=30)
e.pack()

e.bind("<Return>", on_change)  # <Return> is the 'Enter' in keyboard.

root.mainloop()
