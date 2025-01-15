import customtkinter as ctk
from modules.StartMenu import StartMenu
from modules.SearchCustomer import SearchCustomer
from util.windows import check_for_windows
from PIL import Image
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
        self.geometry("1280x720")
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("config/theme/custom.json")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.bind("<Escape>", lambda a: self.destroy())

        # START WINDOW ###
        self.start_menu_frame = SearchCustomer(master=self, fg_color="transparent")
        self.start_menu_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

        #### CREATION WINDOW ###
        #self.start_character_frame = ConfigWrapper(self, fg_color="transparent")
        #self.start_character_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")


# MAIN
check_for_windows()
app = App()

# END
app.mainloop()