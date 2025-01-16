import customtkinter as ctk
from modules.CreateCustomer import CreateCustomer
from modules.SearchCustomer import SearchCustomer
from util.windows import check_for_windows
import os
import sys

# src als Root-Verzeichnis hinzufügen, falls nicht bereits vorhanden
src_path = os.path.join(os.path.dirname(__file__), 'src')
if src_path not in sys.path:
    sys.path.append(src_path)

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Hotel-App")
        self.geometry("1280x900")
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("config/theme/custom.json")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.bind("<Escape>", lambda a: self.destroy())

        # SearchCustomer ###
        self.start_menu_frame = SearchCustomer(master=self, fg_color="transparent")
        self.start_menu_frame.grid(row=0, column=0)

        ##### CreateCustomer ###
        #self.start_character_frame = CreateCustomer(self, fg_color="transparent", width=820)
        #self.start_character_frame.grid(row=0, column=0, sticky="nswe")


# MAIN
check_for_windows()
app = App()

# END
app.mainloop()