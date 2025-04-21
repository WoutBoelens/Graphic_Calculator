import tkinter as tk


off_white = "#F8FAFF"
licht_grijs = "#F5F5F5"
white = "#FFFFFF"
light_blue = "#CCEDFF"
label_color = "#25265E"

large_font_style = ("Arial", 40, "bold")
small_font_style = ("Arial", 16)
digits_font_style = ("Arial", 24, "bold")
default_font_style = ("Arial", 20)

midnight_blue = "#1C2E4A"
low_color = "#C8CDDB"
ivory = "#BDC4D4"
deep_navy = "#0F1A2B"

def start():
    venster = tk.Tk()
    venster.title("Grafische Rekenmachine")
    venster.geometry("1380x720")

    def create_total_frame():
        total_frame = tk.Frame(venster, bg=ivory)
        total_frame.pack(expand=True, fill="both")
        return total_frame

    def create_low_frame():
        low_frame = tk.Frame(venster, height=300, bg=low_color)
        low_frame.pack(fill="x")
        return low_frame

    total_frame = create_total_frame()
    low_frame = create_low_frame()

    title_label = tk.Label(total_frame, text="Grafische Rekenmachine",
                            font=large_font_style, bg=ivory, fg=label_color)
    title_label.pack(pady=100)

    def create_start_button():
        startknop = tk.Button(total_frame, text='START', font=default_font_style,
                               fg='white', bg=midnight_blue, borderwidth=1, width=10,
                               command=lambda: [venster.destroy()])
        startknop.pack()

    label_1 = tk.Label(low_frame, text='①', font=default_font_style,
                        bg=low_color, fg=label_color)
    label_1_inst = tk.Label(low_frame, text='Geef je functie in', font=small_font_style,
                            fg=label_color, bg=low_color)
    label_2 = tk.Label(low_frame, text='➁', font=default_font_style,
                        bg=low_color, fg=label_color)
    label_2_inst = tk.Label(low_frame, text='Plot de grafiek', font=small_font_style,
                            fg=label_color, bg=low_color)
    label_3 = tk.Label(low_frame, text='③', font=default_font_style,
                        bg=low_color, fg=label_color)
    label_3_inst = tk.Label(low_frame, text="Analyseer de grafiek", font= small_font_style,
                            fg=label_color, bg=low_color)


    low_frame.grid_columnconfigure(0, weight=1)
    low_frame.grid_columnconfigure(1, weight=1)
    low_frame.grid_columnconfigure(2, weight=1)

    label_1.grid(column=0, row=0, pady=10)
    label_1_inst.grid(column=0, row=1)
    label_2.grid(column=1, row=0, pady=10)
    label_2_inst.grid(column=1, row=1)
    label_3.grid(column=2, row=0, pady=10)
    label_3_inst.grid(column=2, row=1)

    create_start_button()

    venster.mainloop()

