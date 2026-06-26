import tkinter as tk

root=tk.Tk()
root.title("✦ Get It Done ✦")
root.state("zoomed")    #used "zoomed" to open in full screen
root.config()


# HEADER FRAME
header = tk.Frame(root, bg="#4b3d1a", height=80)
header.pack(side="top", fill="x")
# Prevent shrinking
header.pack_propagate(False)

#Creating frames in header frame
left=tk.Frame(header, bg="#4b3d1a")
left.pack(side="left",padx=20)

center=tk.Frame(header, bg="#4b3d1a")
center.pack(side="left",expand=True)    #Tkinter does not take "center" so create a left widget that expands into the avail space

right=tk.Frame(header, bg="#4b3d1a")
right.pack(side="right",padx=20)

#date for left frame
def left_text():
    
    from datetime import datetime
    
    now = datetime.now()
    formatted = now.strftime("%B %d • %A").lower()
    return formatted
    
left_label=tk.Label(left,text=left_text(), font = ("Times New Roman",15),bg="#4b3d1a",fg="#cfbb9a")
left_label.pack(side="left")

#center frame title
center_label=tk.Label(center,text="✦ Get it Done ✦",font=("Times New Roman",25),bg="#4b3d1a",fg="#cfbb9a") #label under center frame
center_label.pack()

#right motivational text + menu option
right_label=tk.Label(right,text="☘︎ one step at a time       ☰",font=("Times New Roman",15),bg="#4b3d1a",fg="#cfbb9a") #
right_label.pack()



#MAIN FRAME
main = tk.Frame(root, bg="#e6d7c4")
main.pack(fill="both",expand=True)  #creating main frame under root filling x and y axis

# Make grid cells expand
canvas = tk.Canvas(main, bg="#E5D7C4", highlightthickness=0)
scrollbar = tk.Scrollbar(main, orient="vertical", command=canvas.yview)

scrollable_frame = tk.Frame(canvas, bg="#E5D7C4")

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)

canvas.create_window((20, 20), window=scrollable_frame, anchor="nw", width=canvas.winfo_screenwidth())

canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")


# -------- GRID CONFIG (IMPORTANT) --------
for j in range(4):
    scrollable_frame.columnconfigure(j, weight=1)


# -------- CARD FUNCTION --------
def create_card(parent, row, column, title, notes, bg_colour, fg_colour):

    parent.rowconfigure(row, weight=1)

    card = tk.Frame(parent, bg=bg_colour, width=200, height=180)
    card.grid(row=row, column=column, padx=20, pady=20, sticky="nsew")
    card.grid_propagate(False)

    title_label = tk.Label(card, text=title, font=("Times New Roman", 17),
                           bg=bg_colour, fg=fg_colour)
    title_label.pack(pady=(10, 5))

    notes_label = tk.Label(card, text=notes, font=("Times New Roman", 14),
                           bg=bg_colour, fg=fg_colour,
                           anchor="nw", justify="left", wraplength=220)
    notes_label.pack(padx=10, pady=(0, 10), fill="both", expand=True)
for i in range(20):
    row = i // 4
    col = i % 4
    create_card(
        scrollable_frame,
        row,
        col,
        f"✦ TASK {i+1}",
        "Sample task text kuhefiuwhefi uwihgiwhgi wiueghwugh iuwehfouweh ihef iwueghi wiegh iwuegh ig iwueg eighwieguh eg woegy eg",
        "#899064",
        "#E5D7C4"
    )
root.mainloop()