import tkinter as tk
from tkinter import ttk
from Startscherm import start
import grafiek

# Stijlen en kleuren
off_white = "#F8FAFF"
licht_grijs = "#F5F5F5"
white = "#FFFFFF"
light_blue = "#CCEDFF"
label_color = "#25265E"

large_font_style = ("Arial", 40, "bold")
small_font_style = ("Arial", 16)
digits_font_style = ("Arial", 24, "bold")
default_font_style = ("Arial", 20)

class Calculator_Standaard:
    def __init__(self, parent):
        self.parent = parent
        self.total_expression = ""
        self.current_expression = ""
        
        self.create_widgets()
        self.bind_keys()
        self.create_buttons_frame()
        self.create_digits_buttons()
        self.create_operator_buttons()
        self.create_negative_button()
        self.create_special_buttons()
        

    def create_widgets(self):
        self.create_display_frame()
        self.total_label, self.label = self.create_display_labels()

        self.digits = {
            7: (1, 1), 8: (1, 2), 9: (1, 3),
            4: (2, 1), 5: (2, 2), 6: (2, 3),
            1: (3, 1), 2: (3, 2), 3: (3, 3),
            0: (4, 2), '.': (4, 1)
        }

        self.operations = {"/": "\u00F7", "*": "\u00D7", "-": "-", "+": "+"}

        

    def create_display_frame(self):
        self.display_frame = tk.Frame(self.parent, height=221, bg=licht_grijs)
        self.display_frame.pack(expand=True, fill="both")

    def create_display_labels(self):
        total_label = tk.Label(
            self.display_frame, text=self.total_expression, anchor=tk.E,
            bg=licht_grijs, fg=label_color, padx=24, font=small_font_style
        )
        total_label.pack(expand=True, fill="both")

        label = tk.Label(
            self.display_frame, text=self.current_expression, anchor=tk.E,
            bg=licht_grijs, fg=label_color, padx=24, font=large_font_style
        )
        label.pack(expand=True, fill="both")
        return total_label, label

    def add_to_expression(self, value):
        self.current_expression += str(value)
        self.update_label()

    def create_digits_buttons(self):
        for digit, grid_value in self.digits.items():
            button = tk.Button(
                self.buttons_frame, text=str(digit), bg=white, fg=label_color,
                font=digits_font_style, borderwidth=0, command = lambda x = digit: self.add_to_expression(x)
            )
            button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)

    def append_operator(self, operator):
        self.current_expression += operator
        self.total_expression += self.current_expression
        self.current_expression = ""
        self.update_total_label()
        self.update_label()

    def create_operator_buttons(self):
        i = 0
        for operator, symbol in self.operations.items():
            button = tk.Button(
                self.buttons_frame, text=symbol, bg=off_white, 
                fg=label_color, font=default_font_style, borderwidth=0
                ,command = lambda x = operator: self.append_operator(x)
            )
            button.grid(row=i, column=4, sticky=tk.NSEW)
            i += 1

    # Zelf erbij gezet, de negatieve button
    def negative_number(self):
        self.current_expression += '-'
        self.update_label()

    def create_negative_button(self):
        button = tk.Button(self.buttons_frame, text = "(-)", bg = off_white, fg = label_color, font= default_font_style, borderwidth = 0
                           , command = self.negative_number)
        button.grid(row = 4,column=3, sticky= tk.NSEW  )



    def bind_keys(self):
        root.bind("<Return>", lambda event: self.evaluate())

        for key in self.digits:
            root.bind(str(key), lambda event, digit=key: self.add_to_expression(digit))

        for key in self.operations:
            root.bind(key, lambda event, operator=key: self.append_operator(operator))
    
    def create_special_buttons(self):
        self.create_clear_button()
        self.create_equals_button()
        self.create_square_button()
        self.create_sqrt_button()

    def clear(self):
        self.current_expression = ""
        self.total_expression =""
        self.update_label()
        self.update_total_label()

    def create_clear_button(self):
        button = tk.Button(
            self.buttons_frame, text="C", bg=off_white, 
            fg=label_color, font=default_font_style, borderwidth=0
            ,command = self.clear)
        button.grid(row=0, column=1, sticky=tk.NSEW)

    def square(self):
        self.current_expression = str(eval(f"{self.current_expression} ** 2 "))
        self.update_label()

    def create_square_button(self):
        button = tk.Button(
            self.buttons_frame, text="x\u00b2", bg=off_white, 
            fg=label_color, font=default_font_style, borderwidth=0
            ,command = self.square)
        button.grid(row=0, column=2, sticky=tk.NSEW)

    def sqrt(self):
        self.current_expression = str(eval(f"{self.current_expression} ** 0.5 "))
        self.update_label()
        
    def create_sqrt_button(self):
        button = tk.Button(
            self.buttons_frame, text="\u221ax", bg=off_white, 
            fg=label_color, font=default_font_style, borderwidth=0
            ,command = self.sqrt)
        button.grid(row=0, column=3, sticky=tk.NSEW)


    def evaluate(self):
        self.total_expression += self.current_expression
        self.update_total_label()

        try:
            self.current_expression = str(eval(self.total_expression))

            self.total_expression = ""

        except Exception as e:
            self.current_expression = "Error"

        finally:

            self.update_label()

    def create_equals_button(self):
        button = tk.Button(
            self.buttons_frame, text="=", bg=light_blue, fg=label_color,
            font=default_font_style, borderwidth=0, command = self.evaluate
        )
        button.grid(row=4, column=4, columnspan=1, sticky=tk.NSEW)

    def create_buttons_frame(self):
        self.buttons_frame = tk.Frame(self.parent)
        self.buttons_frame.pack(expand=True, fill="both")

        for x in range(5):
            self.buttons_frame.rowconfigure(x, weight=1)
            self.buttons_frame.columnconfigure(x, weight=1)
            
    def update_total_label(self):
        expression = self.total_expression
        for operator, symbol in self.operations.items():
            expression = expression.replace(operator, f" {symbol} ")
        self.total_label.config(text = expression)
    
    def update_label(self):
        self.label.config(text = self.current_expression[:11]) # Zorgt voor de afronding op 11

class Calculator_graphic:
    def __init__(self, parent):
        self.parent = parent
        self.current_function = ''
        #Variable om de functies te kunnen doorgeven voor grafiek
        self.total_expression= ''
        self.current_expression = ""
        self.dic_functies = {}
        #dictonarie voor de opgeslagen functies
        self.create_widgets()
        #functie: maakt de knoppen aan 
        self.bind_keys()
        #Geeft de knoppen een commando

    def create_widgets(self):
        ''' maakt de verschillende knoppen aan
        - de cijfers
        - de operators
        - zelf toegevoegde knoppen: 'x', 'gonio', 
          'haakjes', 'macht', 'PLOT'''
        self.create_display_frame()
        self.total_label, self.label = self.create_display_labels() 

        self.digits = {
            7: (3, 1), 8: (3, 2), 9: (3, 3),
            4: (4, 1), 5: (4, 2), 6: (4, 3),
            1: (5, 1), 2: (5, 2), 3: (5, 3),
            0: (6, 2), '.': (6, 1)
        }

        self.operations = {"/": "\u00F7", "*": "\u00D7", "-": "-", "+": "+"}

        self.create_buttons_frame()
        self.create_digits_buttons()
        self.create_operator_buttons()
        self.create_negative_button()
        self.create_special_buttons() 
        self.create_x_button()
        self.create_gonionmetrische_buttons()
        self.create_haakjes_buttons()
        self.create_macht_button()
        self.create_functions()
        self.create_plot_button()

    def create_buttons_frame(self):
        ''' Maakt het frame voor de knoppen van de rekenmachine'''
        self.buttons_frame = tk.Frame(self.parent)
        self.buttons_frame.pack(expand=True, fill="both")

        for x in range(7):
            self.buttons_frame.rowconfigure(x, weight=1)

        for x in range(5):
            self.buttons_frame.columnconfigure(x, weight=1)
        

    def create_display_frame(self):
        ''' maakt het frame voor de display, dus bovenste en onderste (total en current label)'''
        self.display_frame = tk.Frame(self.parent, height=221, bg=licht_grijs)
        self.display_frame.pack(expand=True, fill="both")

    def create_display_labels(self):
        ''' maakt de total label en de current label'''
        total_label = tk.Label(
            self.display_frame, text=self.total_expression, anchor=tk.E,
            bg=licht_grijs, fg=label_color, padx=24, font=small_font_style
        )
        total_label.pack(expand=True, fill="both")

        label = tk.Label(
            self.display_frame, text=self.current_expression, anchor=tk.E,
            bg=licht_grijs, fg=label_color, padx=24, font=large_font_style
        )
        label.pack(expand=True, fill="both")
        return total_label, label

    def add_to_expression(self, value):
        ''' voegt cijfers toe aan de current_expression en ook aan de current_function'''
        self.current_function += str(value) 
        #nummers toevoegen aan functie
        self.current_expression += str(value)
        self.update_label()

    def create_digits_buttons(self):
        ''' maakt de cijfers van de rekenmachine'''
        for digit, grid_value in self.digits.items():
            button = tk.Button(
                self.buttons_frame, text=str(digit), bg=white, fg=label_color,
                font=digits_font_style, borderwidth=0, command = lambda x = digit: self.add_to_expression(x)
            )
            button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)


    def funtions(self, functie):
        ''' voegt de voorzetsels van de functies toe aan de current_expression'''
        self.current_expression += functie
        self.update_label()


    def create_functions(self):
        ''' maakt de functie variables aan '''
        lijst = {'x1=': (0,0),'x2=': (1,0),'x3=':(2,0),'x4=':(3,0),'x5=':(4,0), 'x6=':(5,0), 'x7=' : (6,0)}

        for function, plaats in lijst.items():
            button = tk.Button(self.buttons_frame, text = function, 
                               command = lambda x = function: self.funtions(x), bg = white, 
                               fg = label_color, font = digits_font_style, borderwidth=0)
            
            button.grid(row=plaats[0], column=plaats[1], sticky=tk.NSEW)

    def append_operator(self, operator):
        #functie dat opperator toevoegd aan current expression
        #Heb stuk code weggelaten dat wanneer operator wordt ingedrukt naar total expression ging
        self.current_function += operator
        self.current_expression += operator
        self.update_label()

    def create_operator_buttons(self):
        i = 0
        rij = 2
        for operator, symbol in self.operations.items():
            button = tk.Button(
                self.buttons_frame, text=symbol, bg=off_white, 
                fg=label_color, font=default_font_style, borderwidth=0
                ,command = lambda x = operator: self.append_operator(x)
            )
            button.grid(row=rij, column=4, sticky=tk.NSEW)
            i += 1
            rij +=1

    # Nieuwe knoppen, zelf erbij gezet
    def negative_number(self):
        ''' de negatie button, voegt een '-' toe aan de functies'''
        self.current_function += '-'
        self.current_expression += '-'
        self.update_label()

    def create_negative_button(self):
        button = tk.Button(self.buttons_frame, text = "(-)", bg = off_white, 
                           fg = label_color, font= default_font_style, borderwidth = 0
                           , command = self.negative_number)
        button.grid(row = 6,column=3, sticky= tk.NSEW  )

    def plot_functie(self):
        ''' de plot knop die de grafiek.py bestand oproept 
        voor de grafieken te plotten'''
        grafiek.plot_functie(self.dic_functies)


    def create_plot_button(self):
        
        button = tk.Button(self.buttons_frame, text = 'PLOT', command = self.plot_functie, bg = off_white, 
                           fg = label_color, font= default_font_style,borderwidth = 0 )
        button.grid(row = 0 , column= 1 , sticky = tk.NSEW)

    def bind_x(self):
        ''' functie die de x variable definieert'''
        self.current_function += 'x'
        self.current_expression += 'x'
        self.update_label()

    def create_x_button(self):
        button = tk.Button(self.buttons_frame, text = 'X', command = self.bind_x, bg = off_white, fg = label_color, font= default_font_style
                           ,borderwidth = 0 )
        button.grid(row = 1 , column= 1 , sticky = tk.NSEW)

    def bind_haakjes(self, haakje):
        ''' functie die haakjes toevoegt'''
        self.current_function += haakje
        self.current_expression += haakje
        self.update_label()

    def create_haakjes_buttons(self):
        button1 = tk.Button(self.buttons_frame, text = '\u208d', command = lambda x = '(': self.bind_haakjes(x), bg = off_white, fg = label_color, font = default_font_style
                            , borderwidth= 0)
        button1.grid(row = 1 , column=2 , sticky= tk.NSEW)
    
        button2 = tk.Button(self.buttons_frame, text = '\u208e', command = lambda x = ')': self.bind_haakjes(x), bg = off_white, fg = label_color, font = default_font_style
                            , borderwidth= 0)
        button2.grid(row = 1 , column= 3 , sticky= tk.NSEW)


    def bind_macht(self):
        ''' functie dat staat voor de macht'''
        self.current_function += '**'
        self.current_expression += '**'
        self.update_label()

    def create_macht_button(self):
        button = tk.Button(self.buttons_frame, text = '^', command = self.bind_macht , bg = off_white, fg = label_color, font = default_font_style
                            , borderwidth= 0)
        button.grid(row = 1 , column= 4 , sticky= tk.NSEW)


    def bind_goniometrie(self, gonio):
        ''' voegt via numpy goniometrische functies toe'''
        self.current_function += f'np.{gonio}'
        #voeg np van de module numpy toe
        self.current_expression += gonio
        self.update_label()
        

    def create_gonionmetrische_buttons(self):
        functies = {"sin(": (0,2), "cos(": (0,3), "tan(": (0,4)}
        for gonio , grid_value in functies.items():
            button = tk.Button(self.buttons_frame, text = gonio, command = lambda x = gonio: self.bind_goniometrie(x), bg = off_white, fg = label_color, font= default_font_style
                           ,borderwidth = 0 )
            button.grid(row = (grid_value[0]), column= grid_value[1], sticky=tk.NSEW)


    def bind_keys(self):
        root.bind("<Return>", lambda event: self.evaluate())
        for key in self.digits:
            root.bind(str(key), lambda event, digit=key: self.add_to_expression(digit))

        for key in self.operations:
            root.bind(key, lambda event, operator=key: self.append_operator(operator))
    
    def create_special_buttons(self):
        self.create_clear_button()
        self.create_equals_button()
        self.create_square_button()
        self.create_sqrt_button()

    def clear(self):
        ''' knop dat alles verwijdert (clear)'''
        self.current_function = ''
        self.current_expression = ""
        self.total_expression =""
        self.update_label()
        self.update_total_label()

    def create_clear_button(self):
        button = tk.Button(
            self.buttons_frame, text="C", bg=off_white, 
            fg=label_color, font=default_font_style, borderwidth=0
            ,command = self.clear)
        button.grid(row=2, column=1, sticky=tk.NSEW)

    def square(self):
        ''' macht van twee'''
        self.current_function += '**2'
        self.current_expression += '**2'
        self.update_label()

    def create_square_button(self):
        button = tk.Button(
            self.buttons_frame, text="x\u00b2", bg=off_white, 
            fg=label_color, font=default_font_style, borderwidth=0
            ,command = self.square)
        button.grid(row=2, column=2, sticky=tk.NSEW)

    def sqrt(self):
        ''' vierkantswortel via Numpy, wel zelf haakjes ervoor zetten'''
        self.current_function += f'np.sqrt'
        #Verplicht zelf haakjes te gebruiken
        self.current_expression += "\u221a"
        self.update_label()
        
    def create_sqrt_button(self):
        button = tk.Button(
            self.buttons_frame, text="\u221ax", bg=off_white, 
            fg=label_color, font=default_font_style, borderwidth=0
            ,command = self.sqrt)
        button.grid(row=2, column=3, sticky=tk.NSEW)


    def evaluate(self):
        ''' de functie die niet evalueert maar die de functie gaat opslaan in de dictonarie met alle functies'''
        self.total_expression = ''
        #maakt total_expression terug leeg
        self.total_expression += self.current_expression 
        self.update_total_label()

        self.dic_functies[self.current_expression[:3]] = self.current_function
        self.current_function = ''
        self.current_expression = ''
        self.update_label()   
        
        

    def create_equals_button(self):
        button = tk.Button(
            self.buttons_frame, text="=", bg=light_blue, fg=label_color,
            font=default_font_style, borderwidth=0, command = self.evaluate
        )
        button.grid(row=6, column=4, columnspan=1, sticky=tk.NSEW)
            
    def update_total_label(self):
        expression = self.total_expression
        for operator, symbol in self.operations.items():
            expression = expression.replace(operator, f" {symbol} ")
        self.total_label.config(text = expression)
    
    def update_label(self):
        self.label.config(text = self.current_expression)

class Programmeur():
    def __init__(self, parent):
        self.parent = parent
        self.total_expression = ""
        self.current_expression = ""
        
        self.create_widgets()
        self.create_buttons_frame()
        self.create_digits_buttons()
        self.create_special_buttons()
        self.bind_keys()
        

    def create_widgets(self):
        ''' Algemene functie voor de widgets, callt subfuncties op via deze functie maakt het leesbaarder'''
        self.create_display_frame()
        self.total_label, self.label = self.create_display_labels()

        self.digits = {
            7: (1, 1), 8: (1, 2), 9: (1, 3),
            4: (2, 1), 5: (2, 2), 6: (2, 3),
            1: (3, 1), 2: (3, 2), 3: (3, 3),
            0: (4, 2), '': (4, 1), ' ': (4, 3)
        }
    
    def bind_keys(self):
        ''' accepteert toetsenbordinput via deze functie '''
        for key in self.digits:
            if str(key).strip() != "":
                root.bind(str(key), lambda event, digit=key: self.add_to_expression(digit))

    def create_display_frame(self):
        ''' frame voor de displays'''
        self.display_frame = tk.Frame(self.parent, height=221, bg=licht_grijs)
        self.display_frame.pack(expand=True, fill="both")

    def create_display_labels(self):
        ''' maakt total_label = 'uitkomst' en label = 'current_label'''
        total_label = tk.Label(
            self.display_frame, text=self.total_expression, anchor=tk.E,
            bg=licht_grijs, fg=label_color, padx=24, font=small_font_style
        )
        total_label.pack(expand=True, fill="both")

        label = tk.Label(
            self.display_frame, text=self.current_expression, anchor=tk.E,
            bg=licht_grijs, fg=label_color, padx=24, font=large_font_style
        )
        label.pack(expand=True, fill="both")
        return total_label, label
    
    def create_digits_buttons(self):
        ''' functie dat buttons voor de rekenmachine toevoegd. Bevat: cijfers 0-9'''
        for digit, grid_value in self.digits.items():
            button = tk.Button(
                self.buttons_frame, text=str(digit), bg=white, fg=label_color,
                font=digits_font_style, borderwidth=0 , command = lambda x = digit: self.add_to_expression(x)
            )
            button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)

    def add_to_expression(self, value):
        ''' voegt cijfers toe aan de current_expression variable'''
        self.current_expression += str(value)
        self.update_label()

    def create_special_buttons(self):
        ''' algeme functie dat de speciale knoppen toevoegt die behoren tot de rekenmachine van de programmeur'''
        self.create_clear_button()
        self.create_binair_button()
        self.create_decimaal_button()

    def binary_to_decimal(self):
        ''' functie dat current_expression (binair getal) omzet naar decimale getallen '''
        self.total_expression = ""
        self.total_expression += str(self.current_expression)
        self.update_total_label()
        try:
            self.current_expression =  int(self.current_expression , 2)
        
        except ValueError:
            self.current_expression = "Hey, that's not a binary number!"

        
        finally:
            self.update_label()

    def create_decimaal_button(self):
        ''' knop dat functie binary_to_decimal oproept'''
        button = tk.Button(
            self.buttons_frame, text="DECI", bg=light_blue, fg=label_color,
            font=default_font_style, borderwidth=0, command = self.binary_to_decimal
        )
        button.grid(row=0, column=2 ,sticky=tk.NSEW)

    def decimal_to_binary(self):
        ''' zet decimale getallen om naar binaire getallen'''
        self.total_expression = ""
        self.total_expression += str(self.current_expression)
        self.update_total_label()

        try:
            self.current_expression = bin(int(self.current_expression))[2:]
            
        
        except ValueError:
            self.current_expression = "That doesn't look like a number to me!"

        finally:
            self.update_label()



    def create_binair_button(self):
        ''' knop dat functie decimal_to_binary oproept'''
        button = tk.Button(
            self.buttons_frame, text="BIN", bg=light_blue, fg=label_color,
            font=default_font_style, borderwidth=0, command = self.decimal_to_binary
        )
        button.grid(row=0, column=3 ,sticky=tk.NSEW)

    def clear(self):
        '''functie dat de expressie wist'''
        self.current_expression = ""
        self.total_expression =""
        self.update_label()
        self.update_total_label()

    def create_clear_button(self):
        button = tk.Button(
            self.buttons_frame, text="C", bg=off_white, 
            fg=label_color, font=default_font_style, borderwidth=0
            ,command = self.clear
            )
        button.grid(row=0, column=1, sticky=tk.NSEW)

    def create_buttons_frame(self):
        self.buttons_frame = tk.Frame(self.parent)
        self.buttons_frame.pack(expand=True, fill="both")

        for x in range(5):
            self.buttons_frame.rowconfigure(x, weight=1)

        for y in range(4):
            self.buttons_frame.columnconfigure(y, weight=1)

    def update_total_label(self):
        expression = self.total_expression
        self.total_label.config(text = expression)
    #functies die total_label en label updaten. deze functies worden opgeroepen wanneer de label moeten up-ge-date worden

    def update_label(self):
        self.label.config(text = self.current_expression) 
        
class Options:
    def __init__(self, parent):
        self.parent = parent
        self.create_title_frame()
        self.create_options_frame()
        self.options = [
            ("STANDAARD", self.switch_to_standaard),
            ("GRAFISCH", self.switch_to_graphic),
            ("PROGRAMMEUR", self.switch_to_programmer)
        ]
        self.create_title_label()
        self.create_options_buttons()

    def create_title_frame(self):
        self.title_frame = tk.Frame(self.parent, height=50, bg=licht_grijs)
        self.title_frame.pack(fill="x")

    def create_options_frame(self):
        self.options_frame = tk.Frame(self.parent, bg=licht_grijs)
        self.options_frame.pack(expand=True, fill="both")
        
    def create_title_label(self):
        title_label = tk.Label(
            self.title_frame, text="Options", bg=licht_grijs, fg=label_color,
            font=large_font_style
        )
        title_label.pack(pady=10)

    def switch_to_standaard(self):
        self.switch_calculator("STANDAARD")

    def switch_to_graphic(self):
        self.switch_calculator("GRAFISCH")

    def switch_to_programmer(self):
        self.switch_calculator("PROGRAMMEUR")

    def switch_calculator(self, option):
        for widget in mainFrame.winfo_children():
            widget.destroy()
        if option == "STANDAARD":
            Calculator_Standaard(mainFrame)
        elif option == "GRAFISCH":
            Calculator_graphic(mainFrame)

        elif option == "PROGRAMMEUR":
            Programmeur(mainFrame)
            

    def create_options_buttons(self):
        button_count = len(self.options)

        # Dynamisch aanpassen van rijenconfiguratie
        for i in range(button_count):
            self.options_frame.rowconfigure(i, weight=1)
        self.options_frame.columnconfigure(0, weight=1)

        # Knoppen toevoegen
        for idx, (option_text, action) in enumerate(self.options):
            button = tk.Button(
                self.options_frame, text=option_text, command=action, bg=white, fg=label_color,
                font=digits_font_style, borderwidth=0, padx=10, pady=10, width=1
            )
            button.grid(row=idx, column=0, sticky=tk.NSEW, pady=5, padx=10)

    
            

    
#Functie van startscherm wordt opgeroepen
start()
    
# Hoofdvenster

root = tk.Tk()
root.geometry("1380x720")
root.title("Grafische Rekenmachine")

# Frames opstellen
mainFrame = ttk.Frame(root, width=680, height=720)
mainFrame.grid(row=0, column=0, sticky="nsew")

rightFrame = ttk.Frame(root, width=400, height=720)
rightFrame.grid(row=0, column=1, sticky="nsew")

# Grid instellingen
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=4)
root.grid_columnconfigure(1, weight=1)

#calculators toevoegen via opties
opt = Options(rightFrame)

root.mainloop()
