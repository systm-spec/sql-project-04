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
    FROM 'C:\Users\Admin\Documents\sql-project-04\Hotel_Reservations.csv'
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

-- Spalten hinzufügen

ALTER TABLE hotelgaeste
    ADD COLUMN nachname      TEXT,
    ADD COLUMN vorname       TEXT,
    ADD COLUMN Ankunftsdatum DATE,
    ADD COLUMN Abreisedatum  DATE;


CREATE TABLE mock_names
(
    first_name TEXT,
    last_name  TEXT
);

COPY mock_names
    FROM 'C:\Users\Admin\Documents\sql-project-04\src\config\init\Kunden.csv'
    DELIMITER ','
    HEADER CSV;

SELECT *
FROM mock_names;


INSERT INTO hotelgaeste (vorname, nachname)
SELECT first_name, last_name
FROM mock_names;

SELECT *
FROM hotelgaeste;