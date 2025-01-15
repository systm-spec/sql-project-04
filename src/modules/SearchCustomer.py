import customtkinter as ctk

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
        self.search_entry = ctk.CTkEntry(self.search_frame, height=28, width=280)
        self.search_entry.grid(ipadx=3, ipady=4, column=0, row=0)

        # Search-Button
        self.search_btn = ctk.CTkButton(self.search_frame, fg_color="transparent", corner_radius=2, text="Search")
        self.search_btn.grid(ipadx=3, ipady=4, column=1, row=0)