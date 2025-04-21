import tkinter as tk



class PlaceholderEntry(tk.Entry):
    def __init__(self, master=None, placeholder="Placeholder", color="gray", *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.placeholder = placeholder
        self.placeholder_color = color
        self.default_color = self["fg"]

        self.insert(0, self.placeholder)
        self.config(fg=self.placeholder_color)

        self.bind("<FocusIn>", self._clear_placeholder)
        self.bind("<FocusOut>", self._add_placeholder)

    def _clear_placeholder(self, event):
        if self.get() == self.placeholder:
            self.delete(0, tk.END)
            self.config(fg=self.default_color)

    def _add_placeholder(self, event):
        if not self.get():
            self.insert(0, self.placeholder)
            self.config(fg=self.placeholder_color)