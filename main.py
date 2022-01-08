import json
from tkinter import *
from tkinter import filedialog, colorchooser
from windows import set_dpi_awareness


THEME_FONT_MENU = ("Segoe UI", 18, "normal")
THEME_FONT_CANVAS = ("Segoe UI", 22, "normal")


class TextEditor:

    def __init__(self):
        self.window = Tk()
        self.window.title("Darknote")
        self.window.config(width=1024, height=768)
        self.window.resizable(True, True)
        set_dpi_awareness()

        self.default_settings = {}
        self.load_default_configuration()

        self.textarea = Text(bg=self.default_settings["background-color"],
                             fg=self.default_settings["font-color"],
                             insertbackground="#eee",
                             font=THEME_FONT_CANVAS)
        self.textarea.pack(expand=True, fill="both")
        self.textarea.focus()

        self.menu = Menu(self.window)
        self.file_menu = Menu(self.menu, tearoff=0)
        self.file_menu.add_command(label="New", command=self.clear_file, font=THEME_FONT_MENU)
        self.file_menu.add_command(label="Open", command=self.open_file, font=THEME_FONT_MENU)
        self.file_menu.add_command(label="Save", command=self.save_file, font=THEME_FONT_MENU)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Quit", command=self.window.quit, font=THEME_FONT_MENU)
        self.menu.add_cascade(label="File", menu=self.file_menu)

        self.settings_menu = Menu(self.menu, tearoff=0)
        self.settings_menu.add_command(label="Change text color", command=self.change_text_color, font=THEME_FONT_MENU)
        self.settings_menu.add_command(label="Change background color", command=self.change_background_color, font=THEME_FONT_MENU)

        self.menu.add_cascade(label="Settings", menu=self.settings_menu)

        self.window.config(menu=self.menu)
        self.window.wm_protocol("WM_DELETE_WINDOW", self.on_destroy)
        self.window.mainloop()

    def load_default_configuration(self):
        try:
            with open("config.txt", "r") as file:
                self.default_settings = json.load(file)
        except FileNotFoundError:
            self.default_settings = {
                "font-color": "#eee",
                "background-color": "#000"
            }
            with open("config.txt", "w") as file:
                json.dump(self.default_settings, file)

    def change_text_color(self):
        color = colorchooser.askcolor(title="Font Color")[1]
        self.default_settings["font-color"] = color
        self.textarea.config(fg=color)

    def change_background_color(self):
        color = colorchooser.askcolor(title="Font Color")[1]
        self.default_settings["background-color"] = color
        self.textarea.config(bg=color)

    def clear_file(self):
        self.textarea.delete("1.0", "end")
        self.textarea.focus()

    def open_file(self):
        filepath = filedialog.askopenfilename()
        with open(filepath, "rb") as file:
            file_text = file.read()
            self.textarea.delete("1.0", "end")
            self.textarea.insert("1.0", file_text)
        self.textarea.focus()

    def save_file(self):
        text = self.textarea.get("1.0", "end-1c")
        filepath = filedialog.asksaveasfilename(filetypes=[("txt file", ".txt")], defaultextension=".txt")
        with open(filepath, "w") as file:
            file.write(text)
        self.textarea.focus()

    def on_destroy(self):
        with open("config.txt", "w") as file:
            json.dump(self.default_settings, file)
            self.window.destroy()


TextEditor()