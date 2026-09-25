# SportPlaner - Gymnasium Sacre Coeur Wien
**Digitaler Unterrichtsplaner für das Unterrichtsfach Bewegung und Sport**  
*Erstellt für Mag. Florian Tintel*

---

## Kurzanleitung & Start

1. **Am PC oder Laptop:**
   - Doppelklick auf `SportPlaner_Starten.bat` oder direkt auf `SportPlaner_SacreCoeur.html`.
   - Die Anwendung öffnet sich im Standard-Webbrowser (Google Chrome, Microsoft Edge, etc.).
   - **Vollständig offline nutzbar**, keine Softwareinstallation oder Serververbindung erforderlich.

2. **Am Tablet oder Smartphone im Turnsaal:**
   - Die Datei `SportPlaner_SacreCoeur.html` kann direkt vom OneDrive oder lokal auf dem Mobilgerät geöffnet werden.

---

## Funktionsbereiche im Überblick

### 1. Stundenplaner (Strukturierte Unterrichtsplanung)
- **Unterrichtsdauer**: Einzelstunde (45–50 min) oder Doppelstunde (90–100 min).
- **Schulstufe & Klasse**: 1. bis 8. Klasse (Unterstufe und Oberstufe AHS).
- **Fachbereiche**: Leichtathletik, Große Sportspiele, Kleine Spiele & Fangen, Motorik & Koordination (nach Warwitz / Hirtz), Kraft & Kondition, Gerätturnen (Turn10) & Akrobatik, Zweikampf & Trendsport sowie Motorische Diagnostik.
- **Rahmenbedingungen**: Anpassbar nach Schülerzahl, Klassenzusammensetzung (Koedukativ, Knaben, Mädchen), Hallenverfügbarkeit (Ganzer Turnsaal, Halbfeld, Drittel, Sportplatz) und pädagogischem Schwerpunkt.
- **Aktion "Stundenbild erstellen & anzeigen"**:
  - Erstellt ein vollständiges Stundenbild mit Einstimmen/Aufwärmen, Hauptteil 1 (Technik/Stationen), Hauptteil 2 (Spielform/Wettkampf) und Schluss/Ausklang.
  - Inklusive Zeitangaben, Materialliste, Hallenorganisation, methodischen Cues und Differenzierungshinweisen.

### 2. Stundenbild & Druckansicht (Offizielles AHS-Format)
- **Direkt editierbar**: Alle Inhalte, Lernziele, Organisationsformen und Zeiten können im Browser durch Anklicken direkt angepasst werden (`contenteditable`).
- **Phasen tauschen**: Über die Schaltfläche "Tauschen" kann für jede Phase rasch eine alternative Übung aus der Datenbank eingesetzt werden.
- **DIN-A4-Druck & PDF-Export**: Über die Schaltfläche "Drucken / PDF" öffnet sich der druckoptimierte Dialog (Steuerelemente werden automatisch ausgeblendet).

### 3. Übungsdatenbank (134 kuratierte Übungen und Spiele)
- Umfassende Sammlung aus den vorhandenen Sacre-Coeur-Dateien (Leichtathletik, Basketball, Handball, Fußball, Floorball, Turn10, Wiener Parcours nach Warwitz, 50 Teamspiele, Schnelle Sportstunde).
- Filterbar nach Fachbereich, spezifischer Sportart, Stundenphase und Schulstufe.
- Jede Übung kann mit einem Klick auf "In Stunde einfügen" direkt in das aktive Stundenbild übernommen werden.

### 4. Leistungsdiagnose: Klug & Fit & Allroundschwimmer
- **Klug & Fit Referenznormen**: Motorischer Fitnesstest für Schulen mit Referenzwerten für 10- bis 18-jährige Knaben und Mädchen in allen 6 Testdisziplinen (20m Sprint, Standweitsprung, Liegestütz, Sit-ups, Rumpfvorbeuge, 8-Minuten-Lauf).
- **Normwert-Auswertung**: Sofortige Zuordnung zu Perzentilen und Notenvorschlag.
- **Österreichischer Allroundschwimmer**: Prüfungskriterien nach den offiziellen Richtlinien des BMBWF.

### 5. Hallen-Tools
- **Intervall- & Zirkeltraining-Timer**: Frei konfigurierbare Belastungs-, Pausen- und Rundenzeiten mit akustischem Signalton.
- **Elektronische Hallenpfeife**: Zweiton-Pfeifsignal (Fox-40-Frequenz) über die Lautsprecher für Start-, Stopp-, Riegenwechsel- und Schiedsrichterkommandos.
- **Zufällige Teameinteilung**: Gleichmäßige Einteilung der Schüler in 2 bis 6 Teams nach Leibchenfarben (Gelb, Blau, Rot, Grün, Weiß, Schwarz).
- **Spielplaner (Jeder gegen Jeden)**: Spielpaarungsübersicht für Klassenturniere.

### 6. Cloud-Archiv
- Strukturierte Übersicht über die im Verzeichnis `c:\Users\Florian\OneDrive - Sacre Coeur\Sport` abgelegten Originaldokumente, PDF-Unterlagen und Praxishilfen.

---

## Speichern & Sichern

- **"Im Browser speichern"**: Sichert den aktuellen Entwurf im lokalen Speicher (`localStorage`) des Webbrowsers.
- **"Als JSON sichern"**: Lädt den Stundenentwurf als strukturierte Datei herunter, die archiviert oder geteilt werden kann.
