-- Datenbank erstellen
CREATE DATABASE hoteldb;

-- Tabelle entfernen, falls sie existiert
DROP TABLE IF EXISTS hotelgaeste;

-- Tabelle erstellen
CREATE TABLE IF NOT EXISTS hotelgaeste
(
    ID                             TEXT,
    Erwachsene                     INT,
    Kinder                         INT,
    Nächte_am_Wochenende           INT,
    Nächte_unter_der_Woche         INT,
    Verpflegungsplan               TEXT,
    Parkplatz                      INT,
    Zimmertyp                      TEXT,
    lead_time                      INT,
    Ankunftsjahr                   INT,
    Ankunftsmonat                  INT,
    Ankunftstag                    INT,
    Marktsegment                   TEXT,
    Wiederkehrender_Gast           INT,
    Vorherige_Stornierungen        INT,
    Vorherige_nicht_Stornierungen  INT,
    Durchschnittlicher_Zimmerpreis FLOAT,
    no_of_special_requests         INT,
    Buchungsstatus                 TEXT
);

-- Vorhandene csv importieren
COPY hotelgaeste
    FROM './Hotel Reservations.csv'
    DELIMITER ','
    CSV HEADER;


SELECT *
FROM hotelgaeste;

-- unnötige Spalten löschen
ALTER TABLE hotelgaeste
    DROP COLUMN lead_time;

ALTER TABLE hotelgaeste
    DROP COLUMN no_of_special_requests;

SELECT *
FROM hotelgaeste;