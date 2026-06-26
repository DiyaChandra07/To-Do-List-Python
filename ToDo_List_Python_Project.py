
import tkinter as tk
from datetime import datetime

# COLOURS
High_green="#364025"
Low_green="#cfbb9a"
Mid_green="#899064"
Beige_bg="#E5D7C4"
Header_brown="#4b3d1a"
High_green_text="#b7c77e"
Low_green_text="#4b3d1a"
Mid_green_text="#d3d488"


#ROOT
root = tk.Tk()
root.title("✦ Get It Done ✦")
root.state("zoomed")  #keep the screen filled
root.config(bg=Beige_bg) #setting bg colour



# HEADER FRAME
header = tk.Frame(root, bg=Header_brown, height=80)
header.pack(side="top", fill="x")
header.pack_propagate(False)

left = tk.Frame(header, bg=Header_brown)
left.pack(side="left", padx=20)

center = tk.Frame(header, bg=Header_brown)
center.pack(side="left", expand=True)

right = tk.Frame(header, bg=Header_brown)
right.pack(side="right", padx=20)

# date in header frame
def get_date():
    return datetime.now().strftime("%B %d • %A").lower()  # to get the present day date

tk.Label(left, text=get_date(), bg=Header_brown, fg=Low_green, font=("Times New Roman", 16)).pack()

tk.Label(center, text="✦ Get It Done ✦", bg=Header_brown, fg=Low_green, font=("Times New Roman", 26, "bold")).pack()



# MAIN FRAME
main = tk.Frame(root, bg=Beige_bg)
main.pack(fill="both", expand=True)  #creating frame for whole main screen

canvas = tk.Canvas(main, bg=Beige_bg, highlightthickness=0)
canvas.pack(side="left", fill="both", expand=True)

# Scrollbar
scrollbar = tk.Scrollbar(main, command=canvas.yview)
scrollbar.pack(side="right", fill="y")    #for ease of accessibility (scrollable screen)
canvas.configure(yscrollcommand=scrollbar.set)

frame = tk.Frame(canvas, bg=Beige_bg)
canvas.create_window((0, 0), window=frame, anchor="nw", width=canvas.winfo_width())
def resize_frame(event):
    canvas.itemconfig("all", width=event.width)

canvas.bind("<Configure>", resize_frame)
frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))  # to make sure the content  stretches and fills the frame

for i in range(4):
    frame.columnconfigure(i, weight=0)

# FILE-HANDLING 
FILE = "tasks.txt"
tasks = []   # store title - notes - priority

#priority management
def get_color(priority):
    if priority == "high":
        return High_green
    elif priority == "medium":
        return Mid_green
    else:
        return Low_green

def get_text_color(priority):
    if priority == "high":
        return High_green_text
    elif priority == "medium":
        return Mid_green_text
    else:
        return Low_green_text


def save():
    with open(FILE, "w") as f:
        for t in tasks:
            f.write(f"{t[0]}|{t[1]}|{t[2]}\n")

def load():
    try:
        with open(FILE) as f:
            for line in f:
                parts = line.strip().split("|")  # remove space and save separate parts
                if len(parts) == 3:
                    tasks.append(parts)
    except:
        pass

# CARDS
def show_tasks():
    for w in frame.winfo_children():
        w.destroy()      # to destroy cards after every time window opens

    for i, t in enumerate(tasks):
        r = i // 4
        c = i % 4
        bg = get_color(t[2])
        fg = get_text_color(t[2])

        # outer frame for each card in the grid
        outer = tk.Frame(frame, bg=Beige_bg, width=340, height=260)
        outer.grid(row=r, column=c, padx=35, pady=20)
        outer.grid_propagate(False)

        # card placed inside the outer frame
        card = tk.Frame(outer, bg=bg, width=290, height=200)
        card.pack(padx=8, pady=8)
        card.pack_propagate(False)

        tk.Label(card, text=t[0], bg=bg, fg=fg, font=("Times New Roman", 18, "bold",)).pack(pady=(10, 5))

        tk.Label(card, text=t[1], bg=bg, fg=fg, font=("Times New Roman", 15), wraplength=230, justify="left").pack(pady=5)
        # each delete button for each card i for each card
        tk.Button(card, text="Delete", bg=Beige_bg, fg=Header_brown, activebackground="#7a2a2a", command=lambda i=i: delete(i)).pack(side="bottom", pady=8)
        

def delete(i):
    tasks.pop(i)
    save()
    show_tasks()

# ADD TASK
def open_popup():
    pop = tk.Toplevel(root)
    pop.title("New Task")
    pop.geometry("320x320+600+200")  #aligning the new window
    pop.config(bg=Beige_bg)

    tk.Label(pop, text="✦ New Task ✦", bg=Beige_bg, font=("Times New Roman", 20, "bold"),fg=Header_brown).pack(pady=10)

    tk.Label(pop, text="Title", bg=Beige_bg,fg=Header_brown).pack()
    title = tk.Entry(pop, font=("Times New Roman", 13))
    title.pack(pady=5)
    

    tk.Label(pop, text="Notes", bg=Beige_bg, fg=Header_brown).pack()
    notes = tk.Entry(pop, font=("Times New Roman", 13))
    notes.pack(pady=5)

    pr = tk.StringVar(value="low") 

    tk.Label(pop, text="Priority", bg=Beige_bg, fg=Header_brown).pack(pady=5)
    
    # choice for priority
    tk.Radiobutton(pop, text="High", variable=pr, value="high", bg=Beige_bg,fg=Header_brown).pack()
    tk.Radiobutton(pop, text="Medium", variable=pr, value="medium", bg=Beige_bg,fg=Header_brown).pack()
    tk.Radiobutton(pop, text="Low", variable=pr, value="low", bg=Beige_bg,fg=Header_brown).pack()

    def add():
        if title.get() != "":
            tasks.append([title.get(), notes.get(), pr.get()])
            save()
            show_tasks()
            pop.destroy()

    tk.Button(pop, text="Add", bg=Header_brown, fg=Low_green, activebackground="#80714c", font=("Times New Roman", 11), command=add).pack(pady=10)

# SORT OPTION
def sort_tasks():
    order = {"high": 0, "medium": 1, "low": 2}
    tasks.sort(key=lambda x: order[x[2]])
    save()
    show_tasks()

#CLEAT OPTION
def clear():
    tasks.clear()
    save()
    show_tasks()

# MENU
menu_btn = tk.Menubutton(right, text="☰", bg=Header_brown, fg=Low_green, font=("Times New Roman", 18))
menu = tk.Menu(menu_btn, tearoff=0)

menu.add_command(label="Sort by Priority", command=sort_tasks)
menu.add_command(label="Clear All", command=clear)

menu_btn.config(menu=menu)
menu_btn.pack()

# ADD BUTTON
tk.Button(root, text="+", font=("Times New Roman", 26, "bold"), bg=Low_green, fg=Header_brown,
          activebackground="#80714c", width=3, height=1,
          command=open_popup).place(relx=0.95, rely=0.9, anchor="center")



# MAIN CALLING OF FUNCTION
load()
show_tasks()

root.mainloop()

