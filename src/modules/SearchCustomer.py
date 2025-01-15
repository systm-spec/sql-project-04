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
        self.content_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.content_frame.grid(column=0, row=1)

    # Fn um den search_var zu ändern und ihn zu casten
    def set_text(self):
        self.search_var_int = int(self.search_var.get())
        workload = find_by_id(self.search_var_int)
        print("--------------\n",workload["first_name"])
        if not workload.empty:
            self.render_fields(workload)
        else:
            print(workload, "RENDER STOPPED")

    def render_fields(self, workload):
        self.counter = 0
        for item in workload.columns:
            temp_lbl = ctk.CTkLabel(self.content_frame, text=item, bg_color="#3f3f46")
            temp_lbl.grid(column=0, row=self.counter, sticky="nswe")
            temp_content = ctk.CTkLabel(self.content_frame, text=workload[item].values[0], width=320, fg_color="#3f3f46")
            temp_content.grid(column=1, row=self.counter)
            self.counter += 1