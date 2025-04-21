import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import sympy as sp
from placeholder import PlaceholderEntry

# Stijlen en kleuren
off_white = "#F8FAFF"
licht_grijs = "#F5F5F5"
white = "#FFFFFF"
light_blue = "#CCEDFF"
label_color = "#25265E"
active_graph_color = "#FF9999"  
button_active_color = "#90EE90"  

large_font_style = ("Arial", 40, "bold")
small_font_style = ("Arial", 16)
digits_font_style = ("Arial", 24, "bold")
default_font_style = ("Arial", 20)

def plot_functie(functies):
    root = tk.Tk()
    root.geometry("1380x880")
    root.title("Grafische Rekenmachine")
    root.resizable(False, False)

    # Frames instellen
    mainFrame = tk.Frame(root, width=680, height=720)
    mainFrame.grid(row=0, column=0, sticky="nsew")

    rightFrame = tk.Frame(root, width=400, height=720)
    rightFrame.grid(row=0, column=1, sticky="nsew")

    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=4)
    root.grid_columnconfigure(1, weight=1)

    # Matplotlib figuur en assen
    fig, ax = plt.subplots()
    # Canvas aan Tkinter koppelen
    canvas = FigureCanvasTkAgg(fig, master=mainFrame)
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    zero_mode = tk.BooleanVar(value=False)  # Houdt bij of de zero-modus actief is
    kleuren = ["cyan", "red", "pink", "green", "yellow", "purple"]
    lijnen = []  # Om referentie naar de plotlijnen te bewaren
    bol_marker = None

    # Voeg de toolbar toe onder de grafiek
    
    def create_toolbar():
        ''' Fucntie dat de toolbar toevoegt'''
        toolbar_frame = tk.Frame(mainFrame)  # Frame voor de toolbar
        toolbar_frame.pack(fill=tk.X, side=tk.TOP)  # Toolbar frame onder de grafiek
        toolbar = NavigationToolbar2Tk(canvas, toolbar_frame)
        toolbar.update()  
        toolbar.pack(fill=tk.X)
    
    def create_title_label(frame):
        title_label = tk.Label(
            frame, text="Bewerkingen", bg=licht_grijs, fg=label_color,
            font=large_font_style
        )
        title_label.grid(row=0, column=0, pady=10)

    def create_nulpunt_button(frame):
        button = tk.Button(frame, text='zero', bg=white, fg=label_color,
                        font=digits_font_style, borderwidth=0, padx=10, pady=10, width=1, command=toggle_zero_mode)
        button.grid(row=1, column=0, sticky=tk.NSEW, pady=5, padx=10)  
        return button

    def create_value_button(frame):
        button = tk.Button(frame, text='value', bg=white, fg=label_color,
                            font=digits_font_style, borderwidth=0, padx=10, pady=10, width=1, command=calculate_value)
        button.grid(row=2, column=0, sticky=tk.NSEW, pady=5, padx=10)

    def create_return_to_home(frame):
        button = tk.Button(frame, text='⬅️', bg=light_blue, fg=label_color,
                        font=digits_font_style, borderwidth=0, padx=10, pady=10, width=1, command=root.destroy)
        button.grid(row=10, column=0, sticky=tk.NSEW, pady=5, padx=10)  

    def create_clear_graph(frame):
        button = tk.Button(frame, text='DELETE', bg=light_blue, fg=label_color,
                        font=digits_font_style, borderwidth=0, padx=10, pady=10, width=1, command=clear_plot)
        button.grid(row = 9, column=0, sticky=tk.NSEW, pady=10, padx=10)  

    def create_intersect_button(frame):
        button = tk.Button(frame, text='INTERSECT', bg=white, fg=label_color,
                        font=digits_font_style, borderwidth=0, padx=10, pady=10, width=1, command = intersect)
        button.grid(row = 5, column=0, sticky=tk.NSEW, pady=10, padx=10)  


    def clear_plot():
        """Verwijder alle punten en lijnen van de grafiek, maar behoud de functies."""
        ax.cla()  
        ax.grid(True)  
        bol_marker = None  # Reset de marker
        plotter()  
        canvas.draw()

    def toggle_zero_mode():
        counter_kleur = 0
        """Schakelt de nulpuntenmodus in/uit en verandert de kleuren"""
        if zero_mode.get():
            counter_kleur = 0 #Zodat wanneer er weer op zero gedrukt wordt, opnieuw alle kleuren gereset worden
            zero_mode.set(False)
            zero_button.config(bg=white)  
            #De grafiek_kleuren herstellen
            for lijn in lijnen:
                lijn.set_color("blue")  
                counter_kleur += 1

        else:
            zero_mode.set(True)
            zero_button.config(bg=button_active_color)  # Knop groen maken
            for lijn in lijnen:
                lijn.set_color(active_graph_color)  # Grafiek rood maken
            
            
        canvas.draw()

    def calc_zero(event, x_list, y_list, functies):  
        """Markeert de nulpunten als zero-mode actief is anders geeft aan dat er geen nulpunten zijn"""

        if not zero_mode.get():
            return  # Alleen uitvoeren als zero-mode actief is
        
        for y in functies.values():
            if "np" in y:
                y = y.replace("np.", "")
            
            x = sp.symbols('x')
            expr = sp.sympify(y)
            oplossing = sp.solve(expr, x)

            #  alleen de reële oplossingen
            reele_oplossingen = [sol.evalf() for sol in oplossing if sol.is_real]
            
            if not reele_oplossingen:
                # Geen reële nulpunten
                ax.text(0.5, 0.5, "Geen reële nulpunten gevonden", ha='center', va='center', fontsize=12, color='red', transform=ax.transAxes)
            else:
                for i in reele_oplossingen:
                    ax.scatter(i, 0, color="red", zorder=3)
                    ax.text(i, 0, f"({i:.2f}, {0})", fontsize=10, verticalalignment='bottom')
            
            canvas.draw()

    def update_marker(x_value, y_value): 
        """Update de marker op de grafiek bij een nieuwe invoer voor de y_waarde"""
        bol_marker = ax.scatter(x_value, y_value, color="red", zorder=5)
        ax.text(x_value, y_value, f"({x_value:.2f}, {y_value:.2f})", fontsize=10, verticalalignment='bottom')
        canvas.draw()

    def calculate_value(): 
        ''' berekent de overeenkomstige y_waarde wanneer de x_waarde wordt ingevoerd.'''
        x_value_str = x_entry.get().strip()
        if not x_value_str:
            result_label.config(text="Voer een geldige x-waarde in.")
            return
        
        try:
            x_value = float(x_value_str)
            for key, f in functies.items():
                f = f.replace('X', 'x')
                
                y_value = eval(f, {"__builtins__": {}}, {"x": x_value, "np": np})
                result_label.config(text=f"y = {y_value:.2f} voor x = {x_value}")
                update_marker(x_value, y_value)
                
        
        except ValueError:
            result_label.config(text="Voer een geldige numerieke x-waarde in.")

    def intersect():
        ''' Berekent het snijpunt tussen twee functies'''
        fout_label.config(text="")
        try:
            functie_1 = functies[functie_1_invoer.get().strip()]
            functie_2 = functies[functie_2_invoer.get().strip()]
        
        except:
            fout_label.config(text = "Foute invoer! Controleer je formules of geef beide functies in!")
            return

        x = sp.Symbol('x')

        try:
            functie_1 = sp.sympify(functie_1)
            functie_2 = sp.sympify(functie_2)
        except sp.SympifyError:
            # Als er een fout is bij het omzetten van de string naar een sympy-expressie
            fout_label.config(text = "Oeps, er is een onbekende fout opgetreden!")
            return

        #Berkent met sympy alle oplossingen van de nulwaarden
        oplossingen_x = sp.solve(functie_1 - functie_2, x)
        if not oplossingen_x:
            fout_label.config(text = "Er zijn geen snijpunten gevonden.")
            return
        # Maakt een lijst van coördinaten (x, y) door elke gevonden x-waarde in te vullen in functie_1 om zo de bijhorende y-waarde te bepalen.
        snijpunten = [(x_val, functie_1.subs(x, x_val)) for x_val in oplossingen_x]
        #Voegt de snijpunten toe als scatters op de grafiek
        for x,y in snijpunten:
            ax.scatter(x, y, color="red", zorder=3)
            ax.text(x,y, f"({x:.2f}, {y:.2f})", fontsize=10, verticalalignment='bottom')
            canvas.draw()

    def plotter():
        counter = 0 # Houdt bij welke kleur er gebruikt moet worden voor elke functie
        
        x_list = np.linspace(-100, 100, 10000)
        
        for key, f in functies.items():
            f = f.replace('X', 'x')  # Vervang hoofdletter X door kleine x
            
            
            # Berekent de bijhorende y-waarden voor de functie f
            # eval voert de string f uit als een Python-expressie
            # geeft alleen toegang tot x_list en numpy (np)
            y_list = eval(f, {"__builtins__": {}}, {"x": x_list, "np": np})

            lijn, = ax.plot(x_list, y_list, label= f"{key}{f}", color= kleuren[counter])
            lijnen.append(lijn)  # Bewaar referentie naar de lijn
            counter += 1
        ax.set_ylim(-20, 20)  # Zet limiet op de y-as
        ax.set_xlim(-20, 20)  # Zet limiet op de x-as
        ax.legend(loc="lower right")
        ax.grid(True)

        return x_list, y_list

        

    create_toolbar()
    create_title_label(rightFrame)
    zero_button = create_nulpunt_button(rightFrame)
    create_value_button(rightFrame)
    create_return_to_home(rightFrame)
    create_clear_graph(rightFrame)
    create_intersect_button(rightFrame)
    x_list, y_list = plotter()

    # Invoer voor x-waarde
    x_entry = PlaceholderEntry(rightFrame, placeholder="Voer x-waarde in:", font=digits_font_style, bg=licht_grijs, fg=label_color)
    x_entry.grid(row=3, column=0, sticky=tk.NSEW, pady=20, padx=10)

    # Label om resultaat te tonen van de value
    result_label = tk.Label(rightFrame, text="y = ?", bg=licht_grijs, fg=label_color, font=small_font_style)
    result_label.grid(row=4, column=0, pady=10)


    #intersect
    functie_1_invoer = PlaceholderEntry(rightFrame, placeholder="Functie 1: bv x1=", font=digits_font_style, bg=licht_grijs, fg=label_color)
    functie_1_invoer.grid(row=6, column=0, sticky=tk.NSEW, pady=10, padx=10)

    functie_2_invoer = PlaceholderEntry(rightFrame, placeholder="Functie 2: bv x2=", font=digits_font_style, bg=licht_grijs, fg=label_color)
    functie_2_invoer.grid(row=7, column=0, sticky=tk.NSEW, pady=10, padx=10)

    fout_label = tk.Label(rightFrame, text="", bg=licht_grijs, fg=label_color, font=small_font_style)
    fout_label.grid(row=8, column=0, pady=20)


    
    fig.canvas.mpl_connect("button_press_event", lambda event: calc_zero(event, x_list, y_list, functies))

    canvas.draw()

    root.mainloop()

