import customtkinter as ctk
from customtkinter import CTkLabel, CTkFrame
from numpy.random import weibull


class StartMenu(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # Grid-System
        self.grid_columnconfigure(0, weight=1)

        # Main-Frame
        self.main_frame = ctk.CTkFrame(self, fg_color='transparent')
        self.main_frame.grid(column=0, row=1, pady=7)

        ### TODO: Join Mock-Names into DB ###
        # First-Name
        # Last-Name

        # ID
        self.id_frame = CTkFrame(self.main_frame)
        self.id_frame.grid(pady=3)
        self.id_ntry_lbl = CTkLabel(self.id_frame, text='Id:')
        self.id_ntry_lbl.grid()
        self.id_ntry = ctk.CTkEntry(self.id_frame)
        self.id_ntry.grid()

        # Erwachsene
        self.adults_frame = CTkFrame(self.main_frame)
        self.adults_frame.grid(pady=3)
        self.adults_ntry_lbl = CTkLabel(self.adults_frame, text='Anzahl Erwachsene:')
        self.adults_ntry_lbl.grid()
        self.adults_ntry = ctk.CTkEntry(self.adults_frame)
        self.adults_ntry.grid()

        # Kinder
        self.children_frame = CTkFrame(self.main_frame)
        self.children_frame.grid(pady=3)
        self.children_ntry_lbl = CTkLabel(self.children_frame, text='Anzahl Kinder:')
        self.children_ntry_lbl.grid()
        self.children_ntry = ctk.CTkEntry(self.children_frame)
        self.children_ntry.grid()

        # Nächte_am_Wochenende
        # Nächte_unter_der_Woche
        # Verpflegungsplan
        # Parkplatz
        # Zimmertyp
        self.room_type_frame = CTkFrame(self.main_frame)
        self.room_type_frame.grid(pady=3)
        self.room_type_ntry_lbl = CTkLabel(self.room_type_frame, text='Zimmer-Typ:')
        self.room_type_ntry_lbl.grid()
        self.room_type_ntry = ctk.CTkEntry(self.room_type_frame)
        self.room_type_ntry.grid()
        # Ankunftsjahr
        # Ankunftsmonat
        # Ankunftstag
        self.arrival_date_frame = CTkFrame(self.main_frame)
        self.arrival_date_frame.grid(pady=3)
        self.arrival_date_ntry_lbl = CTkLabel(self.arrival_date_frame, text='Anreise:')
        self.arrival_date_ntry_lbl.grid()
        self.arrival_date_ntry = ctk.CTkEntry(self.arrival_date_frame)
        self.arrival_date_ntry.grid()
        # Abreisetag
        self.departure_date_frame = CTkFrame(self.main_frame)
        self.departure_date_frame.grid(pady=3)
        self.departure_date_ntry_lbl = CTkLabel(self.departure_date_frame, text='Abreise:')
        self.departure_date_ntry_lbl.grid()
        self.departure_date_ntry = ctk.CTkEntry(self.departure_date_frame)
        self.departure_date_ntry.grid()
        # Marktsegment
        # Wiederkehrender_Gast
        # Vorherige_Stornierungen
        # Vorherige_nicht_Stornierungen
        # Durchschnittlicher_Zimmerpreis
        # Buchungsstatus



