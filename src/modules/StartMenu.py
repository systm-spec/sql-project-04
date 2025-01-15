import customtkinter as ctk
import psycopg2
from customtkinter import CTkLabel, CTkFrame
from numpy.random import weibull
from psycopg import connect
from sqlalchemy.dialects.mysql import insert


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
        self.weekend_nights_frame = CTkFrame(self.main_frame)
        self.weekend_nights_frame.grid(pady=3)
        self.weekend_nights_lbl = CTkLabel(self.weekend_nights_frame, text='Nächte am Wochenende:')
        self.weekend_nights_lbl.grid()
        self.weekend_nights_entry = ctk.CTkEntry(self.weekend_nights_frame)
        self.weekend_nights_entry.grid()

        # Nächte_unter_der_Woche
        self.weekday_nights_frame = CTkFrame(self.main_frame)
        self.weekday_nights_frame.grid(pady=3)
        self.weekday_nights_lbl = CTkLabel(self.weekday_nights_frame, text='Nächte unter der Woche:')
        self.weekday_nights_lbl.grid()
        self.weekday_nights_entry = ctk.CTkEntry(self.weekday_nights_frame)
        self.weekday_nights_entry.grid()

        # Verpflegungsplan
        self.meal_plan_frame = CTkFrame(self.main_frame)
        self.meal_plan_frame.grid(pady=3)
        self.meal_plan_lbl = CTkLabel(self.meal_plan_frame, text='Verpflegungsplan:')
        self.meal_plan_lbl.grid()
        self.meal_plan_entry = ctk.CTkEntry(self.meal_plan_frame)
        self.meal_plan_entry.grid()

        # Parkplatz
        self.parking_frame = CTkFrame(self.main_frame)
        self.parking_frame.grid(pady=3)
        self.parking_lbl = CTkLabel(self.parking_frame, text='Parkplatz:')
        self.parking_lbl.grid()
        self.parking_entry = ctk.CTkEntry(self.parking_frame)
        self.parking_entry.grid()

        # Zimmertyp
        self.room_type_frame = CTkFrame(self.main_frame)
        self.room_type_frame.grid(pady=3)
        self.room_type_ntry_lbl = CTkLabel(self.room_type_frame, text='Zimmer-Typ:')
        self.room_type_ntry_lbl.grid()
        self.room_type_ntry = ctk.CTkEntry(self.room_type_frame)
        self.room_type_ntry.grid()

        # Ankunftsjahr
        self.arrival_year_frame = CTkFrame(self.main_frame)
        self.arrival_year_frame.grid(pady=3)
        self.arrival_year_lbl = CTkLabel(self.arrival_year_frame, text='Ankunftsjahr:')
        self.arrival_year_lbl.grid()
        self.arrival_year_entry = ctk.CTkEntry(self.arrival_year_frame)
        self.arrival_year_entry.grid()

        # Ankunftsmonat
        self.arrival_month_frame = CTkFrame(self.main_frame)
        self.arrival_month_frame.grid(pady=3)
        self.arrival_month_lbl = CTkLabel(self.arrival_month_frame, text='Ankunftsmonat:')
        self.arrival_month_lbl.grid()
        self.arrival_month_entry = ctk.CTkEntry(self.arrival_month_frame)
        self.arrival_month_entry.grid()

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
        self.market_segment_frame = CTkFrame(self.main_frame)
        self.market_segment_frame.grid(pady=3)
        self.market_segment_lbl = CTkLabel(self.market_segment_frame, text='Marktsegment:')
        self.market_segment_lbl.grid()
        self.market_segment_entry = ctk.CTkEntry(self.market_segment_frame)
        self.market_segment_entry.grid()

        # Wiederkehrender_Gast
        self.returning_guest_frame = CTkFrame(self.main_frame)
        self.returning_guest_frame.grid(pady=3)
        self.returning_guest_lbl = CTkLabel(self.returning_guest_frame, text='Wiederkehrender Gast:')
        self.returning_guest_lbl.grid()
        self.returning_guest_entry = ctk.CTkEntry(self.returning_guest_frame)
        self.returning_guest_entry.grid()

        # Vorherige_Stornierungen
        self.previous_cancellations_frame = CTkFrame(self.main_frame)
        self.previous_cancellations_frame.grid(pady=3)
        self.previous_cancellations_lbl = CTkLabel(self.previous_cancellations_frame, text='Vorherige Stornierungen:')
        self.previous_cancellations_lbl.grid()
        self.previous_cancellations_entry = ctk.CTkEntry(self.previous_cancellations_frame)
        self.previous_cancellations_entry.grid()

        # Vorherige_nicht_Stornierungen
        self.previous_non_cancellations_frame = CTkFrame(self.main_frame)
        self.previous_non_cancellations_frame.grid(pady=3)
        self.previous_non_cancellations_lbl = CTkLabel(self.previous_non_cancellations_frame,
                                                       text='Vorherige nicht Stornierungen:')
        self.previous_non_cancellations_lbl.grid()
        self.previous_non_cancellations_entry = ctk.CTkEntry(self.previous_non_cancellations_frame)
        self.previous_non_cancellations_entry.grid()

        # Durchschnittlicher_Zimmerpreis
        self.average_price_frame = CTkFrame(self.main_frame)
        self.average_price_frame.grid(pady=3)
        self.average_price_lbl = CTkLabel(self.average_price_frame, text='Durchschnittlicher Zimmerpreis:')
        self.average_price_lbl.grid()
        self.average_price_entry = ctk.CTkEntry(self.average_price_frame)
        self.average_price_entry.grid()

        # Buchungsstatus
        self.booking_status_frame = CTkFrame(self.main_frame)
        self.booking_status_frame.grid(pady=3)
        self.booking_status_lbl = CTkLabel(self.booking_status_frame, text='Buchungsstatus:')
        self.booking_status_lbl.grid()
        self.booking_status_entry = ctk.CTkEntry(self.booking_status_frame)
        self.booking_status_entry.grid()

        #Save_Button
        self.save_button=ctk.CTkButton(self.main_frame,text='Speichern',command=self.speichern)
        self.save_button.grid(pady=20)

def speichern(self):
    try:
        connection=psycopg2.connect(
            host='localhost',
            database='hoteldb',
            user='postgres',
            password='Datacraft'
        )
        cursor=connection.cursor()

        erwachsene = self.adults_ntry.get()
        kinder = self.children_ntry.get()
        nächte_am_wochenende = self.weekend_nights_entry.get()
        nächte_unter_der_woche = self.weekday_nights_entry.get()
        verpflegungsplan = self.meal_plan_entry.get()
        parkplatz = self.parking_entry.get()
        zimmertyp = self.room_type_ntry.get()
        ankunftsjahr = self.arrival_year_entry.get()
        ankunftsmonat = self.arrival_month_entry.get()
        ankunftstag = self.arrival_day_entry.get()
        marktsegment = self.market_segment_entry.get()
        wiederkehrender_gast = self.returning_guest_entry.get()
        vorherige_stornierungen = self.previous_cancellations_entry.get()
        vorherige_nicht_stornierungen = self.previous_non_cancellations_entry.get()
        durchschnittlicher_zimmerpreis = self.average_price_entry.get()
        buchungsstatus = self.booking_status_entry.get()


        insert_query = """
           INSERT INTO hotelgaeste (
               erwachsene, kinder, nächte_am_wochenende, nächte_unter_der_woche,
               verpflegungsplan, parkplatz, zimmertyp, ankunftsjahr, ankunftsmonat,
               ankunftstag, marktsegment, wiederkehrender_gast, vorherige_stornierungen,
               vorherige_nicht_stornierungen, durchschnittlicher_zimmerpreis, buchungsstatus
           ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
           """
        cursor.execute(insert_query, (
            erwachsene, kinder, nächte_am_wochenende, nächte_unter_der_woche,
            verpflegungsplan, parkplatz, zimmertyp, ankunftsjahr, ankunftsmonat,
            ankunftstag, marktsegment, wiederkehrender_gast, vorherige_stornierungen,
            vorherige_nicht_stornierungen, durchschnittlicher_zimmerpreis, buchungsstatus
        ))

        connection.commit()
        cursor.close()
        connection.close()

        print("Erfolgreich gespeichert!")

    except Exception as e:
        print("Fehler:", e)







