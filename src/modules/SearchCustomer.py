import customtkinter as ctk
from src.controller.find import find_by_id

class SearchCustomer(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)


        # Grid-System
        self.grid_columnconfigure(0, weight=1)

        # Search-Frame
        self.search_frame = ctk.CTkFrame(self, fg_color="#808080")
        self.search_frame.grid(column=0, row=0)
        self.search_frame.grid_columnconfigure(0, weight=2)
        self.search_frame.grid_columnconfigure(1, weight=1)

        # Search-Bar
        self.search_var = ctk.StringVar()
        self.search_entry = ctk.CTkEntry(self.search_frame, height=28, width=280, textvariable=self.search_var, placeholder_text="Suchbegriff eingeben")
        self.search_entry.grid(ipadx=3, ipady=4, column=0, row=0)

        # Search-Button
        self.search_btn = ctk.CTkButton(self.search_frame, fg_color="transparent", corner_radius=2, text="Search",
                                        command=self.set_text)
        self.search_btn.grid(ipadx=3, ipady=4, column=1, row=0)

        # Content-Frame
        self.content_frame = ctk.CTkFrame(self, fg_color="#808080")
        self.content_frame.grid(column=0, row=1)
        self.test_lbl = ctk.CTkLabel(self.content_frame, text="placeholder")
        self.test_lbl.grid(ipadx=4, ipady=4)

    # Fn um den search_var zu ändern und ihn zu casten
    def set_text(self):
        self.search_var_int = int(self.search_var.get())
        workload = find_by_id(self.search_var_int)
        print("--------------\n",workload["first_name"])