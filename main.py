from tkinter import *
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def evaluate_function(equation, up_x, lo_x):

    # Clear the plot frame
    for widget in plot_frame.winfo_children():
        widget.destroy()

    try:
        segments = (up_x - lo_x) + 1
        x = np.linspace(lo_x, up_x, segments*100)
        y = eval(equation, {"x":x, "np":np})

        print(f"x values : {x}")
        print(f"y values : {y}")

        fig = Figure(figsize=(7, 4), dpi=100)
        ax = fig.add_subplot(111)
        ax.plot(x, y)
        ax.set_title("Graph of y = " + equation)
        ax.set_xlabel("x")
        ax.set_ylabel("y")

        canvas = FigureCanvasTkAgg(fig, master=plot_frame)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.pack(fill=BOTH, expand=True)
        canvas.draw()


    except Exception as e:
        print(f"Error evaluating function: {e}")

    


def process_input(usr_input, up_x, lo_x):

    if usr_input.startswith("y ="):
        usr_input = usr_input[3:].strip()
    elif usr_input.startswith("y="):
        usr_input = usr_input[2:].strip()

    #checking if x is there
    if "x" not in usr_input:
        print("Error: The function must include 'x' variable")
        return
    
    if not up_x: up_x = 10
    if not lo_x: lo_x = -10
    
    evaluate_function(usr_input, int(up_x), int(lo_x))

def take_user_input():
    user_input = func_entry.get()  # Get the function string

    up_x = upper_x.get()
    lo_x = lower_x.get()


    process_input(user_input, up_x, lo_x)



root = ttk.Window(themename="darkly")
root.title("Graph Plotter")
root.geometry("1000x700")

plot_frame = ttk.Frame(root)
plot_frame.place(x=130, y=200, width=700, height=450)

style = ttk.Style()

style.configure("success.Outline.TButton", font=("Helvetica", 16))


Label(root, text="Graph Plotter", font=("Helvetica", 20, "bold")).place(x=400, y=40)

func_entry = ttk.Entry(root, bootstyle="success", font=("Helvetica", 16))
func_entry.place(x=75, y=100)

func_add = ttk.Button(root, text="Plot", style="success.Outline.TButton", command=lambda: take_user_input())
func_add.place(x=350, y=100)

#range of x
Label(root, text="Range of x: ", font=("Helvetica", 14)).place(x=500, y=100)

lower_x = ttk.Entry(root, bootstyle="success", font=("Helvetica", 16), width=5)
lower_x.place(x=620, y=100)

Label(root, text="<= x <=", font=("Helvetica", 15, "bold")).place(x=700, y=100)

upper_x = ttk.Entry(root, bootstyle="success", font=("Helvetica", 16), width=5)
upper_x.place(x=780, y=100)

root.mainloop()