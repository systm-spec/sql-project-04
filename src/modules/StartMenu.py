import customtkinter as ctk

class StartMenu(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        # Grid-System
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure((0,1), weight=1)

        # Label-Frame
        self.title_lbl_frame = ctk.CTkFrame(self, fg_color="#808080")
        self.title_lbl_frame.grid(column=0, row=0)
        self.title_lbl_frame.grid_columnconfigure(0, weight=0)
        # Label
        self.title_lbl = ctk.CTkLabel(self.title_lbl_frame, text="RPG GAME", fg_color="gray14", text_color="#EFEFEF",font=("Inter", 24))
        self.title_lbl.grid(padx=2, pady=2, ipadx=140, ipady=20)

        # Buttons-frame
        self.title_btn_frame = ctk.CTkFrame(self)
        self.title_btn_frame.grid(column=0, row=1)
        # Buttons
        self.start_btn = ctk.CTkButton(self.title_btn_frame, fg_color="transparent", corner_radius=2, text="Start")
        self.start_btn.grid(ipadx=3, ipady=4, column=0, row=0)
        self.quit_btn = ctk.CTkButton(self.title_btn_frame, fg_color="transparent", corner_radius=2, text="Quit")
        self.quit_btn.grid(ipadx=3, ipady=4, column=1, row=0)