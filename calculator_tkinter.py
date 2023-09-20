import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Calculator")
o_string = ""


# Functions

# This function will clear the screen
def clear_sc():
    global o_string
    o_string = ""
    refresh_screen()
    resultField.insert("1.0", "0")


# This function will clear the screen and update the values of the screen
def refresh_screen():
    global o_string
    resultField.delete("1.0", tk.END)
    # print(o_string)
    resultField.insert("1.0", o_string)


def evaluate():
    global o_string
    res = eval(o_string)
    print(res)
    o_string = res
    # print("This function will print the results of the expression")
    refresh_screen()


def refresh(val):
    global o_string
    o_string += val
    refresh_screen()


# Input Screen

resultField = tk.Text(root, bg="#FFFFFF", fg="#000000", height=2, width=37)
resultField.insert("1.0", "0")
resultField.grid(row=0, column=0, columnspan=4)

# 1st column

tk.Button(root, text="1", height=2, width=5, command=lambda: refresh("1")).grid(row=1, column=0)
tk.Button(root, text="4", height=2, width=5, command=lambda: refresh("4")).grid(row=2, column=0)
tk.Button(root, text="7", height=2, width=5, command=lambda: refresh("7")).grid(row=3, column=0)
tk.Button(root, text="0", height=2, width=5, command=lambda: refresh("0")).grid(row=4, column=0)

# 2nd column
tk.Button(root, text="2", height=2, width=5, command=lambda: refresh("2")).grid(row=1, column=1)
tk.Button(root, text="5", height=2, width=5, command=lambda: refresh("5")).grid(row=2, column=1)
tk.Button(root, text="8", height=2, width=5, command=lambda: refresh("8")).grid(row=3, column=1)
tk.Button(root, text="(", height=2, width=5, command=lambda: refresh("(")).grid(row=4, column=1)

# 3rd column
tk.Button(root, text="3", height=2, width=5, command=lambda: refresh("3")).grid(row=1, column=2)
tk.Button(root, text="6", height=2, width=5, command=lambda: refresh("6")).grid(row=2, column=2)
tk.Button(root, text="9", height=2, width=5, command=lambda: refresh("9")).grid(row=3, column=2)
tk.Button(root, text=")", height=2, width=5, command=lambda: refresh(")")).grid(row=4, column=2)

# 4th column
tk.Button(root, text="+", height=2, width=5, command=lambda: refresh("+")).grid(row=1, column=3)
tk.Button(root, text="-", height=2, width=5, command=lambda: refresh("-")).grid(row=2, column=3)
tk.Button(root, text="*", height=2, width=5, command=lambda: refresh("*")).grid(row=3, column=3)
tk.Button(root, text="/", height=2, width=5, command=lambda: refresh("/")).grid(row=4, column=3)

# Last Row
tk.Button(root, text="=", height=2, width=5, command=evaluate).grid(row=5, column=0, columnspan=2)
tk.Button(root, text="Clear", height=2, width=7, command=clear_sc).grid(row=5, column=2, columnspan=2)

# Start the Tkinter event loop
root.mainloop()
