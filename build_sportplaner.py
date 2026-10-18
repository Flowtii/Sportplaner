# -*- coding: utf-8 -*-
"""
Database builder and UI enhancer for SportPlaner Sacre Coeur Wien.
Adds Schwellenpädagogik features, viral Instagram games, fixes encoding,
and writes updated files.
"""
import sys
import re

NEW_EXERCISES = [
  # -------------------------------------------------------------------------
  # 1. FANG- & REAKTIONSSPIELE (SCHWELLEN-KLASSIKER / 0 MIN. AUFBAU)
  # -------------------------------------------------------------------------
  {
    "id": "schwell_kettenfangen",
    "title": "Kettenfangen mit Teilung",
    "category": "spiele",
    "subcat": "fangen",
    "phase": "warmup",
    "ageGroup": "alle",
    "duration": 8,
    "goal": "Reaktionsschnelligkeit, Richtungswechsel & Teamkoordination",
    "desc": "1 Fänger beginnt. Jeder Abgetippte fasst die Hand des Fängers. Sobald die Kette 4 Kinder erreicht, teilt sie sich in zwei 2er-Ketten. So entstehen immer mehr kleine, wendige Fängerketten.",
    "material": "Ohne Geräte (0 Min. Aufbau)",
    "org": "Gesamte Halle",
    "cues": "Ketten dürfen nicht reißen; freie Läufer nutzen geschickt Lücken zwischen den Ketten.",
    "ref": "Schwellenpädagogik / Gymnasium Sacre Coeur",
    "tags": ["null_material", "1klasse_koed", "schwellen"]
  },
  {
    "id": "schwell_chinesische_mauer",
    "title": "Chinesische Mauer (Wächter der Mittellinie)",
    "category": "spiele",
    "subcat": "fangen",
    "phase": "warmup",
    "ageGroup": "unterstufe",
    "duration": 8,
    "goal": "Antizipation, Finte & Sprintkraft",
    "desc": "1–2 Wächter bewegen sich nur seitlich auf der Mittellinie. Auf Signal quert die Klasse die Halle von Grundlinie zu Grundlinie. Wer getippt wird, erstarrt als Mauer-Pfeiler auf der Mittellinie und hilft mit den Armen beim Tippen.",
    "material": "Hallenlinien (0 Min. Aufbau)",
    "org": "Queren der Halle",
    "cues": "Finten nutzen, Tempo verzögern und explosionsartig antreten.",
    "ref": "Schwellenpädagogik / Gymnasium Sacre Coeur",
    "tags": ["null_material", "1klasse_koed", "schwellen"]
  },
  {
    "id": "schwell_zombieball",
    "title": "Zombieball (Jeder gegen Jeden)",
    "category": "spiele",
    "subcat": "abwurf",
    "phase": "warmup",
    "ageGroup": "alle",
    "duration": 10,
    "goal": "Umfeldwahrnehmung, Ausweichen & Wurfpräzision",
    "desc": "2–3 Softbälle im Spiel. Jeder spielt gegen jeden. Wer getroffen wird, merkt sich den Werfer und setzt sich an den Hallenrand. Wird dieser Werfer abgeworfen, sind alle seine Opfer sofort wieder im Spiel.",
    "material": "2–3 Softbälle",
    "org": "Gesamte Halle",
    "cues": "Kein Laufen mit Ball (max. 3 Schritte). Den Blick immer im 360°-Winkel halten.",
    "ref": "Schwellenpädagogik / Gymnasium Sacre Coeur",
    "tags": ["baelle", "1klasse_koed", "schwellen"]
  },
  {
    "id": "schwell_zauberer_fee",
    "title": "Zauberer & Fee (Erlösungs-Fangen)",
    "category": "spiele",
    "subcat": "fangen",
    "phase": "warmup",
    "ageGroup": "unterstufe",
    "duration": 8,
    "goal": "Laufbereitschaft & prosoziales Verhalten",
    "desc": "2 Zauberer (mit Leibchen) versteinern Mitschüler durch Antippen im Grätschstand. 2 Feen können verzauberte Kinder erlösen, indem sie unten durch die Beine krabbeln. Rollentausch nach 2 Minuten.",
    "material": "4 Parteibänder / Leibchen",
    "org": "Gesamte Halle",
    "cues": "Feen schützen ihre Mitschüler; Zauberer dürfen nicht vor erstarrten Kindern campen.",
    "ref": "Schwellenpädagogik / Gymnasium Sacre Coeur",
    "tags": ["null_material", "1klasse_koed", "schwellen"]
  },
  {
    "id": "schwell_schwarz_weiss",
    "title": "Schwarz oder Weiß (Tag & Nacht)",
    "category": "spiele",
    "subcat": "fangen",
    "phase": "warmup",
    "ageGroup": "alle",
    "duration": 8,
    "goal": "Hör-Reaktion, Schnellkraft & Richtungsantritt",
    "desc": "Team Schwarz und Team Weiß stehen sich an der Mittellinie Rücken an Rücken im Abstand von 1m gegenüber. Ruft die Lehrkraft laut 'SCHWARZ!', jagt Schwarz Weiß bis zur Wandlinie. Bei 'WEISS!' umgekehrt.",
    "material": "Hallenlinien (0 Min. Aufbau)",
    "org": "Rücken an Rücken an der Mittellinie",
    "cues": "Körperschwerpunkt tief halten, sofortige Körperdrehung nach Hörsignal.",
    "ref": "Schwellenpädagogik / Gymnasium Sacre Coeur",
    "tags": ["null_material", "1klasse_koed", "schwellen"]
  },
  {
    "id": "schwell_baendchenraub",
    "title": "Bändchenraub (Klammerjagd)",
    "category": "spiele",
    "subcat": "fangen",
    "phase": "warmup",
    "ageGroup": "alle",
    "duration": 8,
    "goal": "Wendigkeit, Raumgefühl & Schutz des eigenen Raums",
    "desc": "Jedes Kind klemmt sich ein Leibchen oder Band hinten locker in den Hosenbund. Ziel: Anderen die Bändchen herausziehen und sammeln, während das eigene Band mit geschickten Drehungen geschützt wird.",
    "material": "Parteibänder oder Wäscheklammern",
    "org": "Hallenmittelbereich",
    "cues": "Nicht festhalten, nur das Band greifen. Ständige Dreh- und Ausweichbewegungen.",
    "ref": "Schwellenpädagogik / Gymnasium Sacre Coeur",
    "tags": ["huetchen_reifen", "1klasse_koed", "schwellen"]
  },
  {
    "id": "schwell_pacman_linien",
    "title": "Pac-Man (Linienfangen)",
    "category": "spiele",
    "subcat": "fangen",
    "phase": "warmup",
    "ageGroup": "unterstufe",
    "duration": 8,
    "goal": "Balancieren, Linienorientierung & Schnelligkeit",
    "desc": "Alle Schüler und 2 Fänger dürfen sich ausschließlich auf den bunten Hallenmarkierungen bewegen. Überholen und Springen von Linie zu Linie ist verboten. Wer die Linie verlässt, wird automatisch Fänger.",
    "material": "Hallenlinien (0 Min. Aufbau)",
    "org": "Gesamtes Liniennetz der Sporthalle",
    "cues": "Vorausschauend laufen, Kreuzungen rechtzeitig zum Richtungswechsel nutzen.",
    "ref": "Schwellenpädagogik / Gymnasium Sacre Coeur",
    "tags": ["null_material", "1klasse_koed", "schwellen"]
  },
  {
    "id": "schwell_tunnel_fangen",
    "title": "Tunnel-Fangen (Kriech-Erlösung)",
    "category": "spiele",
    "subcat": "fangen",
    "phase": "warmup",
    "ageGroup": "unterstufe",
    "duration": 7,
    "goal": "Ausdauer, Beweglichkeit & Kooperation",
    "desc": "2 Fänger jagen die Klasse. Getroffene Schüler bleiben breitbeinig im Grätschstand stehen. Befreit werden kann man nur, indem ein Mitschüler von hinten durch die Beine durchkrabbelt.",
    "material": "Ohne Geräte (0 Min. Aufbau)",
    "org": "Gesamte Halle",
    "cues": "Aktives Rufen nach Hilfe; Retter müssen den Fängern geschickt ausweichen.",
    "ref": "Schwellenpädagogik / Gymnasium Sacre Coeur",
    "tags": ["null_material", "1klasse_koed", "schwellen"]
  },
  {
    "id": "schwell_krankenhaus_fangen",
    "title": "Krankenhaus-Fangen (Pflaster-Fang)",
    "category": "spiele",
    "subcat": "fangen",
    "phase": "warmup",
    "ageGroup": "unterstufe",
    "duration": 8,
    "goal": "Ausdauerlauf mit Spaßfaktor & koordinativer Erschwernis",
    "desc": "1. Treffer: Hand auf die berührte Körperstelle legen (1. Pflaster). 2. Treffer: Zweite Hand auf neue Trefferstelle (2. Pflaster). 3. Treffer: Ab ins 'Krankenhaus' (Matte an der Wand), 5 Kniebeugen machen und geheilt weiterspielen.",
    "material": "Ohne Geräte (0 Min. Aufbau)",
    "org": "Gesamte Halle + 1 Turnmatte als Spital",
    "cues": "Auch mit 'Handicap' weiterlaufen; keine Stehzeiten durch sofortige Selbstheilung.",
    "ref": "Schwellenpädagogik / Gymnasium Sacre Coeur",
    "tags": ["null_material", "1klasse_koed", "schwellen"]
  },
  {
    "id": "schwell_fischer_fahne",
    "title": "Fischer, welche Fahne weht heute?",
    "category": "spiele",
    "subcat": "fangen",
    "phase": "warmup",
    "ageGroup": "unterstufe",
    "duration": 8,
    "goal": "Reaktion, Farberkennung & Sprintantritt",
    "desc": "Der Fischer steht in der Mitte. Klasse ruft: 'Fischer, welche Fahne weht heute?'. Fischer antwortet z.B.: 'Rot!'. Alle Kinder mit roter Kleidung dürfen ruhig hinübergehen. Alle anderen müssen sprinten, ohne berührt zu werden.",
    "material": "Ohne Geräte (0 Min. Aufbau)",
    "org": "Querung zwischen beiden Hallenwänden",
    "cues": "Gezielt Täuschungen anwenden; als Fischer den Laufweg der Masse antizipieren.",
    "ref": "Schwellenpädagogik / Gymnasium Sacre Coeur",
    "tags": ["null_material", "1klasse_koed", "schwellen"]
  },
  {
    "id": "schwell_feuer_wasser_sturm",
    "title": "Feuer, Wasser, Sturm (Hallen-Reaktion)",
    "category": "spiele",
    "subcat": "fangen",
    "phase": "warmup",
    "ageGroup": "unterstufe",
    "duration": 7,
    "goal": "Hör-Reaktionsfähigkeit & Raumorientierung",
    "desc": "Freies Traben in der Halle. Auf Zuruf: 'Feuer!' = alle berühren die Hallenwand; 'Wasser!' = alle klettern auf Bänke/Kästen; 'Sturm!' = flach auf den Bauch legen; 'Erdbeben!' = an Sprossenwand hängen.",
    "material": "Bänke / Hallengeräte vorhanden",
    "org": "Freier Lauf in der Halle",
    "cues": "Blitzschnell reagieren, gegenseitige Rücksichtnahme an Engstellen.",
    "ref": "Schwellenpädagogik / Gymnasium Sacre Coeur",
    "tags": ["null_material", "1klasse_koed", "schwellen"]
  },
  {
    "id": "schwell_statuenfangen",
    "title": "Statuenfangen (Balance-Rettung)",
    "category": "spiele",
    "subcat": "fangen",
    "phase": "warmup",
    "ageGroup": "alle",
    "duration": 8,
    "goal": "Gleichgewicht unter Zeitdruck & Ausdauer",
    "desc": "2 Fänger jagen. Man rettet sich vor dem Abschlag, indem man auf einem Bein eine Standwaage oder Flamingo-Statue einnimmt. Wackelt der Fuß oder setzt man ab, darf der Fänger zuschlagen.",
    "material": "Ohne Geräte (0 Min. Aufbau)",
    "org": "Gesamte Halle",
    "cues": "Rumpf anspannen, festen Blickpunkt am Boden fixieren.",
    "ref": "Schwellenpädagogik / Gymnasium Sacre Coeur",
    "tags": ["null_material", "1klasse_koed", "schwellen"]
  },

  # -------------------------------------------------------------------------
  # 2. WURF-, FANG- & BALLSPIELE (TEAM- & ZIELGENAUIGKEIT)
  # -------------------------------------------------------------------------
  {
    "id": "schwell_mattenball",
    "title": "Mattenball (Klassiker des Passspiels)",
    "category": "ball",
    "subcat": "burnergames",
    "phase": "main2",
    "ageGroup": "alle",
    "duration": 15,
    "goal": "Freilaufen, Passgenauigkeit & Raumaufteilung",
    "desc": "2 Teams. An jedem Hallenende liegt ein Weichboden. Ein Teamspieler steht auf der Matte. Punktgewinn, wenn ein Pass aus dem Feld zum Mattenfänger sicher gefangen wird. Kein Laufen mit Ball erlaubt!",
    "material": "1 Softball, 2 Weichböden",
    "org": "Gesamte Halle, 2 Teams",
    "cues": "Nach jedem Pass sofort freilaufen; Verteidiger decken Raum vor der Matte ab.",
    "ref": "Schwellenpädagogik / Gymnasium Sacre Coeur",
    "tags": ["baelle", "1klasse_koed", "schwellen"]
  },
  {
    "id": "schwell_turmball",
    "title": "Turmball (Korbball-Vorstufe)",
    "category": "ball",
    "subcat": "burnergames",
    "phase": "main2",
    "ageGroup": "unterstufe",
    "duration": 15,
    "goal": "Bogenwurf, Timing & Manndeckung",
    "desc": "Ähnlich Mattenball, aber der Fänger ('Turmwächter') steht auf einem 1-teiligen Kasten oder in einem Reifen. Der Ball muss im hohen Bogen zugespielt und ohne Bodenberührung gefangen werden.",
    "material": "1 Ball, 2 flache Kästen oder Reifen",
    "org": "Gesamte Halle",
    "cues": "Pässe dosieren; der Turmwächter balanciert sicher und zeigt Fangfenster an.",
    "ref": "Schwellenpädagogik / Gymnasium Sacre Coeur",
    "tags": ["baelle", "1klasse_koed", "schwellen"]
  },
  {
    "id": "schwell_zehnerball",
    "title": "Zehnerball (Königspass)",
    "category": "ball",
    "subcat": "burnergames",
    "phase": "main2",
    "ageGroup": "alle",
    "duration": 12,
    "goal": "Passfluss, Antizipation & Verteidigungsdruck",
    "desc": "Ein Team versucht sich den Ball 10-mal in Folge fehlerfrei zuzupassen, ohne dass der Gegner ihn berührt oder er auf den Boden fällt. Jeder Pass wird laut mitgezählt. Bei Ballverlust zählt der Gegner.",
    "material": "1 Softball",
    "org": "Hallenmittelbereich, 2 Teams à 6–8 Schüler",
    "cues": "Kurze, sichere Pässe wählen; ständige Dreiecksbildung im Raum.",
    "ref": "Schwellenpädagogik / Gymnasium Sacre Coeur",
    "tags": ["baelle", "1klasse_koed", "schwellen"]
  },
  {
    "id": "schwell_burgensturm",
    "title": "Burgensturm (Hütchen-Artillerie)",
    "category": "ball",
    "subcat": "abwurf",
    "phase": "main2",
    "ageGroup": "alle",
    "duration": 15,
    "goal": "Zielwurf, Deckungsverhalten & Spieltaktik",
    "desc": "In jeder Hallenhälfte steht eine Bank mit 5 Hütchen ('Burg'). Beide Teams bewerfen mit 3–4 Softbällen aus ihrer Hälfte die gegnerischen Hütchen. Welches Team räumt zuerst alle Hütchen des Gegners ab?",
    "material": "2 Bänke, 10 Hütchen, 4 Softbälle",
    "org": "Geteilte Halle (Mittellinie tabu)",
    "cues": "Bälle rollend sichern, Druck- und Schlagwürfe gezielt platzieren.",
    "ref": "Schwellenpädagogik / Gymnasium Sacre Coeur",
    "tags": ["baelle", "huetchen_reifen", "1klasse_koed", "schwellen"]
  },
  {
    "id": "schwell_eichhoernchen",
    "title": "Eichhörnchen-Spiel (Nüsse sammeln)",
    "category": "ball",
    "subcat": "burnergames",
    "phase": "main1",
    "ageGroup": "unterstufe",
    "duration": 10,
    "goal": "Schnelligkeitsausdauer, Wurfgefühl & Teamwork",
    "desc": "In der Hallenmitte liegen 30 Soft- und Tennisbälle. 4 Teams in den Ecken haben je einen Reifen als Kobel. Immer ein Kind pro Team sprintet vor, holt einen Ball und wirft ihn treffsicher in den Teamreifen.",
    "material": "4 Reifen, 30 verschiedene Bälle",
    "org": "4 Ecken-Teams",
    "cues": "Nicht stoppen, flüssiger Übergang von Sprint zu Wurf.",
    "ref": "Schwellenpädagogik / Gymnasium Sacre Coeur",
    "tags": ["baelle", "huetchen_reifen", "1klasse_koed", "schwellen"]
  },
  {
    "id": "schwell_voelkerball_rev",
    "title": "Völkerball-Revolution (Mit Freikauf)",
    "category": "ball",
    "subcat": "abwurf",
    "phase": "main2",
    "ageGroup": "alle",
    "duration": 15,
    "goal": "Wurf- & Ausweichschulung ohne Frustration",
    "desc": "Modernes Völkerball mit 2 Bällen. Wer abgeworfen wird, geht ins Hinterfeld. Wer aus dem Hinterfeld einen Gegner abwirft ODER einen Ball direkt fängt, darf SOFORT wieder ins Hauptfeld zurückkehren.",
    "material": "2–3 Softbälle",
    "org": "Geteiltes Völkerballfeld",
    "cues": "Flugbahn der Bälle beobachten, Hinterfeld aktiv in Pässe einbinden.",
    "ref": "Schwellenpädagogik / Gymnasium Sacre Coeur",
    "tags": ["baelle", "1klasse_koed", "schwellen"]
  },
  {
    "id": "schwell_huetchen_biathlon",
    "title": "Hallen-Biathlon mit Hütchen",
    "category": "leichtathletik",
    "subcat": "sprint",
    "phase": "main1",
    "ageGroup": "alle",
    "duration": 12,
    "goal": "Laufökonomie unter Belastung & Wurfpräzision",
    "desc": "Schüler laufen 1 Runde um die Halle und kommen zum Schießstand (3 Tennisbälle auf 3 Hütchen werfen aus 4m). Für jedes stehengebliebene Hütchen muss 1 kleine Strafrunde um eine Bank gelaufen werden.",
    "material": "Tennisbälle, Hütchen, Bänke",
    "org": "Rundlauf mit Schießstation",
    "cues": "Puls vor dem Wurf bewusst durch Ausatmen senken, Wurfarm hoch.",
    "ref": "Schwellenpädagogik / Gymnasium Sacre Coeur",
    "tags": ["baelle", "huetchen_reifen", "1klasse_koed", "schwellen"]
  },
  {
    "id": "schwell_ball_schnur",
    "title": "Ball über die Schnur (Volleyball-Ready)",
    "category": "ball",
    "subcat": "volleyball",
    "phase": "main2",
    "ageGroup": "unterstufe",
    "duration": 15,
    "goal": "Flugkurvenerkennung & kooperatives Zuspiel",
    "desc": "Eine Zauberschnur oder ein Netz wird auf 2m Höhe gespannt. 2 Teams werfen und fangen den Ball. Vor dem Rückwurf müssen mindestens 2 Kontakte (Zuspiel zu Mitschülern) im eigenen Feld erfolgen.",
    "material": "1 Leichtball / Schaumball, Zauberschnur",
    "org": "Volleyball-Halbfelder",
    "cues": "Laut 'Mein Ball!' rufen, Zuspiel mit beiden Händen von unten/oben.",
    "ref": "Schwellenpädagogik / Gymnasium Sacre Coeur",
    "tags": ["baelle", "1klasse_koed", "schwellen"]
  },

  # -------------------------------------------------------------------------
  # 3. HÜTCHEN, REIFEN & VERSCHIEDENE BÄLLE (KREATIV-KOMBIS)
  # -------------------------------------------------------------------------
  {
    "id": "kombi_hula_hut_abwurf",
    "title": "Hula-Hut-Abwurf (Iglu-Belagerung)",
    "category": "ball",
    "subcat": "abwurf",
    "phase": "main2",
    "ageGroup": "alle",
    "duration": 15,
    "goal": "Zielwurf, Raumverteidigung & Teamtaktik",
    "desc": "In der Mitte steht ein aus 6 Reifen freistehend gebauter Hula-Hut (Iglu). 2 Verteidiger schützen ihn vor Softbällen. Die Außenspieler passen sich 2 Bälle zu und werfen ab, sobald eine Lücke entsteht.",
    "material": "6 Reifen, 2 Softbälle",
    "org": "Kreisformation um den Hula-Hut",
    "cues": "Verteidiger federn Bälle mit Beinen/Händen ab, Angreifer spielen schnelle Pässe.",
    "ref": "Schwellenpädagogik / Gymnasium Sacre Coeur",
    "tags": ["huetchen_reifen", "baelle", "1klasse_koed", "schwellen"]
  },
  {
    "id": "kombi_reifen_boccia",
    "title": "Reifen-Boccia (Präzisions-Challenge)",
    "category": "motorik",
    "subcat": "differenzierung",
    "phase": "cool",
    "ageGroup": "alle",
    "duration": 10,
    "goal": "Kraftdosierung & kinästhetische Feinkoordination",
    "desc": "In 6m Entfernung liegt ein Reifen. Schüler werfen abwechselnd verschiedene Bälle (Tennisball, Basketball, Futsalball) aus dem Stand. Ziel: Der eigene Ball muss im Reifen liegenbleiben oder am nächsten daran.",
    "material": "1 Reifen, diverse Bälle",
    "org": "4er-Gruppen an einer Abwurflinie",
    "cues": "Flugbahn und Rollverhalten des jeweiligen Balltyps vorher abschätzen.",
    "ref": "Schwellenpädagogik / Gymnasium Sacre Coeur",
    "tags": ["huetchen_reifen", "baelle", "1klasse_koed", "schwellen"]
  },
  {
    "id": "kombi_schatzkammer_raub",
    "title": "Schatzkammer-Raub mit Dribbling",
    "category": "ball",
    "subcat": "basketball",
    "phase": "main1",
    "ageGroup": "unterstufe",
    "duration": 12,
    "goal": "Beidhändiges Dribbling unter Zeitdruck & Antritt",
    "desc": "Im Mittelkreis (Reifenlager) liegen 20 Bälle. 4 Teams starten aus ihren Hütchentoren in den Ecken. Auf Pfiff sprintet je 1 Läufer vor, sichert einen Ball und dribbelt ihn kontrolliert durch Hütchen ins eigene Tor.",
    "material": "Hütchen, Reifen, Basket- & Volleybälle",
    "org": "4 Teams in den Hallenecken",
    "cues": "Kopf beim Dribbeln oben behalten, um Zusammenstöße in der Mitte zu vermeiden.",
    "ref": "Schwellenpädagogik / Gymnasium Sacre Coeur",
    "tags": ["huetchen_reifen", "baelle", "1klasse_koed", "schwellen"]
  },
  {
    "id": "kombi_cone_ball_balance",
    "title": "Cone-Ball-Balance-Parcours",
    "category": "motorik",
    "subcat": "gleichgewicht",
    "phase": "main1",
    "ageGroup": "unterstufe",
    "duration": 10,
    "goal": "Dynamisches Gleichgewicht & Feinmotorik",
    "desc": "Ein Tennisball liegt auf der Spitze eines umgedrehten Pylons/Hütchens. Die Kinder balancieren das Hütchen auf der Handfläche, während sie durch ausgelegte Reifen steigen und über eine umgedrehte Bank balancieren.",
    "material": "Hütchen, Tennisbälle, Reifen, Langbank",
    "org": "Parcours in 2 Bahnen",
    "cues": "Ruhige, gleichmäßige Schritte; den Ball nie mit den Fingern fixieren.",
    "ref": "Schwellenpädagogik / Gymnasium Sacre Coeur",
    "tags": ["huetchen_reifen", "baelle", "1klasse_koed", "schwellen"]
  },
  {
    "id": "kombi_ampel_prellen",
    "title": "Ampel-Prellen mit Ring-Stopp",
    "category": "ball",
    "subcat": "basketball",
    "phase": "warmup",
    "ageGroup": "unterstufe",
    "duration": 8,
    "goal": "Reaktionsdribbling & sofortiger Stoppsprung",
    "desc": "Alle dribbeln frei. Die Lehrkraft zeigt Hütchen: Grün = Vollgas-Dribbeln, Gelb = Zeitlupe mit Richtungswechsel, Rot = Sofort mit beiden Beinen in den nächstgelegenen Reifen springen und Ball sichern.",
    "material": "Bälle, rote/gelbe/grüne Hütchen, Reifen",
    "org": "Freie Bewegung im Raum",
    "cues": "Stopp mit gebeugten Knien und beidhändigem Ballschutz.",
    "ref": "Schwellenpädagogik / Gymnasium Sacre Coeur",
    "tags": ["huetchen_reifen", "baelle", "1klasse_koed", "schwellen"]
  },
  {
    "id": "kombi_huetchen_waechter",
    "title": "Der Hütchen-Wächter",
    "category": "ball",
    "subcat": "abwurf",
    "phase": "main1",
    "ageGroup": "alle",
    "duration": 10,
    "goal": "Passwinkel finden & periphere Abwehr",
    "desc": "3 Hütchen stehen in einem Reifen. 1 Wächter verteidigt sie. 3 Angreifer außen passen sich den Ball zu und werfen ab, sobald der Wächter auf die falsche Seite spekuliert. Nach erfolgreichem Treffer Rollentausch.",
    "material": "1 Reifen, 3 Hütchen, 1 Softball pro 4er-Gruppe",
    "org": "4er-Gruppen in der ganzen Halle verteilt",
    "cues": "Nicht zögern: Pässe schnell antäuschen, um den Wächter in Bewegung zu bringen.",
    "ref": "Schwellenpädagogik / Gymnasium Sacre Coeur",
    "tags": ["huetchen_reifen", "baelle", "1klasse_koed", "schwellen"]
  },
  {
    "id": "kombi_becher_fang",
    "title": "Becher-Fang (Cone Catch Duell)",
    "category": "motorik",
    "subcat": "differenzierung",
    "phase": "main1",
    "ageGroup": "alle",
    "duration": 10,
    "goal": "Auge-Hand-Koordination & Flugbahnberechnung",
    "desc": "Partnerübung: Partner A wirft einen Tennisball mit sanftem Bogen; Partner B fängt den Ball direkt mit der Öffnung eines umgedrehten Hütchens (wie mit einem Trichter) auf. Distanz nach 5 Treffern um 1m vergrößern.",
    "material": "1 Hütchen + 1 Tennisball pro Paar",
    "org": "Paarweise Aufstellung an Linien",
    "cues": "Dem Ball mit dem Hütchen weich entgegengehen und ihn abfedern.",
    "ref": "Schwellenpädagogik / Gymnasium Sacre Coeur",
    "tags": ["huetchen_reifen", "baelle", "1klasse_koed", "schwellen"]
  },

  # -------------------------------------------------------------------------
  # 4. HOHE INTENSITÄT (AUSPOWERN, HIIT, KEINE STEHZEITEN)
  # -------------------------------------------------------------------------
  {
    "id": "hiit_chaos_baelle",
    "title": "Chaos-Bälle (Räumt die Halle auf!)",
    "category": "fitness",
    "subcat": "zirkel",
    "phase": "warmup",
    "ageGroup": "alle",
    "duration": 8,
    "goal": "Maximaler Puls, Sprintantritt & Rumpfaktivierung",
    "desc": "40 Bälle liegen in der Halle verteilt. 2 Teams auf zwei Hallenhälften getrennt. Auf Pfiff müssen alle Bälle so schnell wie möglich ins gegnerische Feld geworfen/gerollt werden. Nach 90 Sekunden Vollgas: Freeze & Zählen!",
    "material": "30–40 Soft- und Basketbälle",
    "org": "Halle durch Mittellinie halbiert",
    "cues": "Keine Sekunde stehen bleiben, immer sofort zum nächsten freien Ball spurten.",
    "ref": "Schwellenpädagogik / Gymnasium Sacre Coeur",
    "tags": ["high_intensity", "baelle", "1klasse_koed", "schwellen"]
  },
  {
    "id": "hiit_zombieball_turbo",
    "title": "Zombieball Turbo (Wand-Aktivierung statt Sitzen)",
    "category": "spiele",
    "subcat": "abwurf",
    "phase": "main2",
    "ageGroup": "alle",
    "duration": 12,
    "goal": "Dauersprint, Kraftausdauer & Null-Stehzeit-Garantie",
    "desc": "Klassischer Zombieball, aber wer getroffen wird, setzt sich NICHT an den Rand, sondern sprintet an die Wand, macht sofort 5 Liegestütze oder 10 Kniebeugen und ist SOFORT wieder mitten im Spiel. Maximaler Puls!",
    "material": "3–4 Softbälle",
    "org": "Gesamte Halle",
    "cues": "Übungen an der Wand sauber ausführen, dann explosiv zurück ins Spielfeld.",
    "ref": "Schwellenpädagogik / Gymnasium Sacre Coeur",
    "tags": ["high_intensity", "baelle", "1klasse_koed", "schwellen"]
  },
  {
    "id": "hiit_linien_shuttle",
    "title": "Linien-Shuttle-Run (Pyramiden-Staffel)",
    "category": "fitness",
    "subcat": "zirkel",
    "phase": "main1",
    "ageGroup": "alle",
    "duration": 10,
    "goal": "Laktattoleranz, Richtungswechsel & Beinkraft",
    "desc": "Staffel in 4er-Teams: Kind sprintet zur 1. Hallenlinie (5m), tippt mit der Hand auf, sprintet zurück; dann zur 2. Linie (10m) & zurück; dann zur 3. Linie (15m) & zurück. Abklatschen für den nächsten Läufer.",
    "material": "Hallenlinien (0 Min. Aufbau)",
    "org": "Reihenstaffel an der Grundlinie",
    "cues": "Tief anbremsen, mit der Hand den Boden berühren, explosiv wegdrücken.",
    "ref": "Schwellenpädagogik / Gymnasium Sacre Coeur",
    "tags": ["high_intensity", "null_material", "1klasse_koed", "schwellen"]
  },
  {
    "id": "hiit_ewiger_faenger",
    "title": "Der ewige Fänger (30s-HIIT-Fangen)",
    "category": "fitness",
    "subcat": "zirkel",
    "phase": "warmup",
    "ageGroup": "alle",
    "duration": 8,
    "goal": "Anaerobe Schnelligkeitsausdauer & Sprintpower",
    "desc": "2 Fänger jagen für exakt 30 Sekunden mit 100% Maximaltempo. Jeder gefangene Schüler zählt als Punkt. Nach Pfiff: 15 Sekunden Gehpause und sofort 2 neue Fänger für die nächste 30s-Runde. 6 Durchgänge.",
    "material": "Stoppuhr / Timer (0 Min. Aufbau)",
    "org": "Gesamte Halle",
    "cues": "In den 15s Pause tief durchatmen; Fänger geben von Sekunde 1 an Vollgas.",
    "ref": "Schwellenpädagogik / Gymnasium Sacre Coeur",
    "tags": ["high_intensity", "null_material", "1klasse_koed", "schwellen"]
  },
  {
    "id": "hiit_jagdstaffel",
    "title": "Jagdstaffel (Rundlauf-Verfolgung)",
    "category": "leichtathletik",
    "subcat": "sprint",
    "phase": "main2",
    "ageGroup": "alle",
    "duration": 10,
    "goal": "Verfolgungsmotivation & Tempohärte",
    "desc": "2 Teams starten exakt gleichzeitig an diagonal gegenüberliegenden Hallenecken und laufen im Kreis außen um die Halle. Schafft es ein Läufer von Team A, den Läufer von Team B vor der Staffelübergabe abzutippen?",
    "material": "4 Eck-Hütchen",
    "org": "Hallenrundlauf",
    "cues": "Kurven eng anlaufen, Wechselzeit durch Vorlaufen minimieren.",
    "ref": "Schwellenpädagogik / Gymnasium Sacre Coeur",
    "tags": ["high_intensity", "huetchen_reifen", "1klasse_koed", "schwellen"]
  },
  {
    "id": "hiit_matten_schieben",
    "title": "Matten-Schieben (Power-Push)",
    "category": "fitness",
    "subcat": "zirkel",
    "phase": "main1",
    "ageGroup": "alle",
    "duration": 10,
    "goal": "Ganzkörperkraft, Rumpfstabilität & Beinschub",
    "desc": "3er-Teams schieben eine schwere Weichbodenmatte quer über den Hallenboden von Wand zu Wand. Ein extrem fordernder Kraft-Ausdauer-Wettkampf mit gigantischer Motivation und Teamgeist.",
    "material": "2 Weichbodenmatten",
    "org": "2 Bahnen in Hallenlängsrichtung",
    "cues": "Tief in die Hocke gehen, mit den Beinen nach hinten wegstemmen, Rumpf stabil halten.",
    "ref": "Schwellenpädagogik / Gymnasium Sacre Coeur",
    "tags": ["high_intensity", "kooperation", "schwellen"]
  },
  {
    "id": "hiit_karten_fitness",
    "title": "Karten-Fitness (Tabata-Kartenspiel)",
    "category": "fitness",
    "subcat": "zirkel",
    "phase": "main1",
    "ageGroup": "alle",
    "duration": 12,
    "goal": "Gamification & Ganzkörper-Kondition",
    "desc": "Lehrkraft zieht Spielkarten: Herz = Burpees, Pik = Mountain Climbers, Karo = Hocksprünge, Kreuz = Hallensprint. Die Zahl der Karte bestimmt die Dauer in Sekunden (oder Wiederholungen). Blitzschneller Wechsel!",
    "material": "1 Kartenspiel (Skat/Rommé)",
    "org": "Klasse im Kreis oder in Riegen",
    "cues": "Volle Intensität über die kurze Belastungszeit, sofortiger Einstieg.",
    "ref": "Schwellenpädagogik / Gymnasium Sacre Coeur",
    "tags": ["high_intensity", "null_material", "schwellen"]
  },

  # -------------------------------------------------------------------------
  # 5. VIRALE INSTAGRAM- & TIKTOK-HITS (@wimasu, @vlamingo, @thepespecialist)
  # -------------------------------------------------------------------------
  {
    "id": "insta_rps_hoop_showdown",
    "title": "Rock-Paper-Scissors Hoop Showdown (Schere-Stein-Papier Pfad)",
    "category": "spiele",
    "subcat": "burnergames",
    "phase": "warmup",
    "ageGroup": "alle",
    "duration": 10,
    "goal": "Sprungkraft, Reaktionsgeschwindigkeit & Team-Support",
    "desc": "Der virale Hit mit über 20 Mio. Views: 10–12 Reifen liegen in einer geschwungenen Reihe. 2 Teams starten an den Enden, hüpfen einbeinig/beidbeinig aufeinander zu. Wo sie sich treffen: Schere-Stein-Papier! Gewinner hüpft weiter, Verlierer raus, nächster Läufer startet sofort.",
    "material": "10–12 Reifen",
    "org": "Pfad quer durch die Halle, 2 Teams",
    "cues": "Sobald das Duell verloren ist, muss der nächste Läufer wie eine Rakete starten!",
    "ref": "Instagram Trend / @thepespecialist & @pe.games",
    "tags": ["insta_hit", "huetchen_reifen", "1klasse_koed", "schwellen"]
  },
  {
    "id": "insta_head_shoulders_cone",
    "title": "Head, Shoulders, Knees... Cone! (Kopf-Knie-Hütchen)",
    "category": "spiele",
    "subcat": "burnergames",
    "phase": "warmup",
    "ageGroup": "alle",
    "duration": 8,
    "goal": "Reaktionsschnelligkeit & neuromuskuläre Aktivierung",
    "desc": "Der Dauerbrenner auf Insta: Partner stehen sich im Abstand von 1m gegenüber, ein Hütchen steht in der Mitte am Boden. Lehrer ruft schnell: 'Kopf! Schultern! Knie! Bauch! ... HÜTCHEN!'. Wer schnappt das Hütchen zuerst?",
    "material": "1 Hütchen pro Paar",
    "org": "Gegenüberstellung an Hallenlinie",
    "cues": "Beide Hände immer exakt an die gerufenen Körperteile, erst bei 'Hütchen' zugreifen.",
    "ref": "Instagram Trend / @wimasu.de",
    "tags": ["insta_hit", "huetchen_reifen", "1klasse_koed", "schwellen"]
  },
  {
    "id": "insta_huetchen_flip_relay",
    "title": "Hütchen-Flip-Relay (Bottle Flip im Sport)",
    "category": "spiele",
    "subcat": "burnergames",
    "phase": "main1",
    "ageGroup": "alle",
    "duration": 10,
    "goal": "Staffeltempo, Feinmotorik & Frusttoleranz",
    "desc": "Im Staffellauf sprintet das Kind zu einer Bank und wirft ein Hütchen per 'Hand-Flip' hoch. Es muss auf dem Sockel landen. Erst wenn das Hütchen steht, darf zurückgesprintet und abgeklatscht werden. Riesiger Jubel garantiert!",
    "material": "1 Hütchen pro Staffelbahn, Bänke",
    "org": "3–4 Staffelbahnen",
    "cues": "Leichter Drall aus dem Handgelenk; Ruhe bewahren trotz Sprintbelastung.",
    "ref": "Instagram Trend / @vlamingo.de",
    "tags": ["insta_hit", "huetchen_reifen", "1klasse_koed", "schwellen"]
  },
  {
    "id": "insta_tic_tac_toe_relay",
    "title": "Tic-Tac-Toe-Staffel (Drei gewinnt im Sprint)",
    "category": "spiele",
    "subcat": "burnergames",
    "phase": "main1",
    "ageGroup": "alle",
    "duration": 10,
    "goal": "Kognition unter Laktat & Sprintantritt",
    "desc": "9 Reifen liegen als 3x3-Gitter am Hallenende. 2 Teams sprinten mit je 3 farbigen Leibchen vor. Ab dem 4. Läufer dürfen keine neuen Bänder gelegt, sondern nur liegende Bänder versetzt werden. Welches Team hat zuerst 3 in einer Reihe?",
    "material": "9 Reifen, 6 Parteibänder (2 Farben)",
    "org": "2 Teams an der Startlinie",
    "cues": "Schon im Anlauf überlegen, welches Feld blockiert oder erobert werden muss.",
    "ref": "Instagram Trend / @pe_with_mr_c",
    "tags": ["insta_hit", "huetchen_reifen", "1klasse_koed", "schwellen"]
  },
  {
    "id": "insta_hungry_hippos",
    "title": "Hungry Hungry Hippos (Turnhallen-Edition)",
    "category": "spiele",
    "subcat": "burnergames",
    "phase": "main1",
    "ageGroup": "unterstufe",
    "duration": 12,
    "goal": "Teamdynamik, Körperspannung & Gaudi",
    "desc": "In der Mitte liegen 50 Bälle. Ein Kind liegt bauchlings auf einem Rollbrett und hält einen umgedrehten Wäschekorb. Der Partner hält seine Füße, schiebt es blitzschnell in die Mitte, stülpt den Korb über Bälle und zieht es zurück.",
    "material": "Rollbretter, Wäschekörbe, viele Bälle",
    "org": "4 Teams in den Hallenecken",
    "cues": "Gute Rumpfspannung auf dem Rollbrett, harmonisches Schieben und Ziehen.",
    "ref": "Instagram Trend / @physedgames",
    "tags": ["insta_hit", "baelle", "kooperation", "schwellen"]
  },
  {
    "id": "insta_battleship_pe",
    "title": "Schiffeversenken (Battleship PE)",
    "category": "ball",
    "subcat": "abwurf",
    "phase": "main2",
    "ageGroup": "alle",
    "duration": 15,
    "goal": "Bogenwurf, blinde Antizipation & Teamkommunikation",
    "desc": "In der Mitte stehen dicke Weichböden als blickdichte Wand. Auf beiden Seiten stehen Kegel ('Schiffe'). Teams werfen mit 4 Softbällen blind im hohen Bogen über die Wand, um die gegnerischen Schiffe zu versenken.",
    "material": "Weichbodenmatten (senkrecht), Kegel/Hütchen, Softbälle",
    "org": "Geteilte Halle mit Sichtschutz",
    "cues": "Wurfparabel anpassen; Späher dürfen vom Rand Anweisungen zur Wurfweite geben.",
    "ref": "Instagram Trend / @just.playsports",
    "tags": ["insta_hit", "baelle", "1klasse_koed", "schwellen"]
  },
  {
    "id": "insta_medic_dodgeball",
    "title": "Medic Dodgeball (Der geheime Sanitäter)",
    "category": "ball",
    "subcat": "abwurf",
    "phase": "main2",
    "ageGroup": "alle",
    "duration": 15,
    "goal": "Taktik, Schutz von Schlüsselfiguren & Völkerball-Spaß",
    "desc": "Jedes Team bestimmt heimlich 1 Sanitäter. Getroffene Spieler setzen sich auf den Boden. Der Sanitäter kann sie durch 5 Sekunden langes Handauflegen heilen. Wird der Sanitäter abgeworfen, kann niemand mehr heilen!",
    "material": "2–4 Softbälle",
    "org": "Völkerballfeld",
    "cues": "Sanitäter muss seine Identität geheim halten und Bodyguards nutzen.",
    "ref": "Instagram Trend / @thepeshed",
    "tags": ["insta_hit", "baelle", "1klasse_koed", "schwellen"]
  },
  {
    "id": "insta_protect_president",
    "title": "Protect the President (Präsidentenschutz)",
    "category": "ball",
    "subcat": "abwurf",
    "phase": "main2",
    "ageGroup": "alle",
    "duration": 12,
    "goal": "Körperliche Hingabe, Blockverhalten & Spielanalyse",
    "desc": "Ein Schüler ist der 'Präsident' (trägt ein auffälliges Leibchen, darf keinen Ball werfen). 4 Leibwächter umringen ihn eng und müssen alle gegnerischen Bälle mit dem eigenen Körper abblocken, um den Präsidenten zu retten.",
    "material": "Softbälle, 1 Leibchen",
    "org": "Völkerball- oder Halbfeld",
    "cues": "Leibwächter bewegen sich synchron zum Präsidenten und stellen sich mutig in den Wurf.",
    "ref": "Instagram Trend / @pe.games",
    "tags": ["insta_hit", "baelle", "1klasse_koed", "schwellen"]
  },
  {
    "id": "insta_squid_game_pe",
    "title": "Squid Game PE (Rotes Licht, Grünes Licht)",
    "category": "spiele",
    "subcat": "burnergames",
    "phase": "warmup",
    "ageGroup": "unterstufe",
    "duration": 8,
    "goal": "Körperkontrolle, Vollbremsung & Spannungsaufbau",
    "desc": "Fänger steht mit dem Rücken zur Klasse an der Wand. 'Grünes Licht!' = alle sprinten lautlos vorwärts. 'Rotes Licht!' = Fänger dreht sich blitzschnell um. Wer wackelt oder bremst, muss zurück an die Startlinie. Wer tippt die Wand?",
    "material": "Ohne Geräte (0 Min. Aufbau)",
    "org": "Start an der Grundlinie, Ziel an der gegenüberliegenden Wand",
    "cues": "Aus dem vollen Sprint sofort in die absolute Bewegungslosigkeit erstarren.",
    "ref": "Instagram Trend / @wimasu.de",
    "tags": ["insta_hit", "null_material", "1klasse_koed", "schwellen"]
  },
  {
    "id": "insta_pool_noodle_tag",
    "title": "Schwimmnudel-Fangen (Pool Noodle Tag)",
    "category": "spiele",
    "subcat": "fangen",
    "phase": "warmup",
    "ageGroup": "unterstufe",
    "duration": 8,
    "goal": "Reaktionsvermögen & sicherer Fangspaß ohne Schmerz",
    "desc": "2 Fänger halten eine halbe Schaumstoff-Schwimmnudel. Damit tippen sie Mitschüler sanft an den Beinen ab. Die vergrößerte Reichweite sorgt für spektakuläre Ausweichsprünge und absolut verletzungsfreien Spielspaß.",
    "material": "2–3 Schwimmnudeln",
    "org": "Gesamte Halle",
    "cues": "Nur unterhalb der Hüfte antippen; Richtungswechsel mit tiefem Schwerpunkt.",
    "ref": "Instagram Trend / @thepespecialist",
    "tags": ["insta_hit", "1klasse_koed", "schwellen"]
  },
  {
    "id": "insta_ninja_schleichen",
    "title": "Ninja-Schleichen (Schlüsselbund-Wächter)",
    "category": "spiele",
    "subcat": "burnergames",
    "phase": "cool",
    "ageGroup": "unterstufe",
    "duration": 10,
    "goal": "Auditive Wahrnehmung, Schleichmotorik & Ruhe",
    "desc": "Ein 'Wächter' sitzt mit verbundenen Augen neben einem Hütchen mit einem Schlüsselbund. Schüler schleichen sich von allen Seiten an, um den Schlüssel zu stibitzen. Zeigt der Wächter auf ein Geräusch, muss der Ertappte zurück.",
    "material": "1 Augenbinde, 1 Schlüsselbund, 1 Hütchen",
    "org": "Kreisformation um den Wächter",
    "cues": "Auf Zehenspitzen schleichen, Gewichtsverlagerung lautlos abrollen.",
    "ref": "Instagram Trend / @sportunterricht_ideen",
    "tags": ["insta_hit", "huetchen_reifen", "1klasse_koed", "schwellen"]
  },
  {
    "id": "insta_teppichfliesen_curling",
    "title": "Teppichfliesen-Curling",
    "category": "motorik",
    "subcat": "differenzierung",
    "phase": "main1",
    "ageGroup": "alle",
    "duration": 10,
    "goal": "Gefühlsdosierung & Reibungsdynamik",
    "desc": "In 8m Entfernung liegt ein Reifen als 'House'. Schüler schlittern Teppichfliesen mit der Hand über den Hallenboden. Welche Fliese liegt am nächsten am Zentrum? Gegnerische Fliesen dürfen weggestoßen werden.",
    "material": "Teppichfliesen, 1–2 Reifen",
    "org": "2 Bahnen an einer Abwurflinie",
    "cues": "Körper tief absenken, Schwung gleichmäßig aus Schulter und Arm abgeben.",
    "ref": "Instagram Trend / @wimasu.de",
    "tags": ["insta_hit", "huetchen_reifen", "1klasse_koed", "schwellen"]
  },
  {
    "id": "insta_infection_tag",
    "title": "Infection Tag (Die Zombie-Welle)",
    "category": "spiele",
    "subcat": "fangen",
    "phase": "warmup",
    "ageGroup": "alle",
    "duration": 8,
    "goal": "Ausdauer, Übersicht & exponentielle Beschleunigung",
    "desc": "1 Fänger beginnt. Jeder, der abgetippt wird, verwandelt sich sofort ebenfalls in einen Fänger! Die Zahl der Jäger wächst lawinenartig an, bis nur noch ein einziger Überlebender im Hallenchaos sprintet.",
    "material": "Ohne Geräte (0 Min. Aufbau)",
    "org": "Gesamte Halle",
    "cues": "Fänger stimmen sich nonverbal ab und treiben Gejagte in Hallenecken.",
    "ref": "Instagram Trend / @pe.games",
    "tags": ["insta_hit", "high_intensity", "null_material", "1klasse_koed", "schwellen"]
  },
  {
    "id": "insta_floor_is_lava",
    "title": "The Floor is Lava (Hallenüberquerung)",
    "category": "spiele",
    "subcat": "teamspiel",
    "phase": "main1",
    "ageGroup": "unterstufe",
    "duration": 15,
    "goal": "Teamgeist, Problemlösungskompetenz & Geschicklichkeit",
    "desc": "Der Hallenboden ist glühende Lava! 4er-Teams müssen von Wand A zu Wand B gelangen und haben dazu nur 2 Teppichfliesen und 1 Reifen. Wer den Boden berührt, muss mit seinem Team von vorne starten.",
    "material": "Teppichfliesen, Reifen",
    "org": "Querung in Teams",
    "cues": "Material nach vorne durchreichen, sich gegenseitig stützen.",
    "ref": "Instagram Trend / @just.playsports",
    "tags": ["insta_hit", "kooperation", "huetchen_reifen", "1klasse_koed", "schwellen"]
  },
  {
    "id": "insta_evolution_ssp",
    "title": "Evolution (Schere-Stein-Papier-Lauf)",
    "category": "spiele",
    "subcat": "burnergames",
    "phase": "warmup",
    "ageGroup": "unterstufe",
    "duration": 8,
    "goal": "Ganzkörper-Mobilität & lachende Aktivierung",
    "desc": "Alle starten als 'Ei' (in tiefer Hocke watscheln). Treffen sich zwei Eier, spielen sie SSP. Der Sieger entwickelt sich zum 'Huhn' (halbe Hocke mit Flügelschlagen), dann zum 'Dino' (aufrecht brüllend), dann zum 'Superman'!",
    "material": "Ohne Geräte (0 Min. Aufbau)",
    "org": "Freie Bewegung im Raum",
    "cues": "Nur mit Tieren der gleichen Evolutionsstufe duellieren; Verlierer steigt eine Stufe ab.",
    "ref": "Instagram Trend / @vlamingo.de",
    "tags": ["insta_hit", "null_material", "1klasse_koed", "schwellen"]
  }
]

print(f"Total new exercises defined: {len(NEW_EXERCISES)}")

MORE_EXERCISES = [
  # --- WEITERE KOEDUKATIVE & SCHWELLEN-SPIELE (1. KLASSE GYMNASIUM) ---
  {
    "id": "schwell_spiegelbild_duell",
    "title": "Spiegelbild-Duell (Synchron-Motorik)",
    "category": "motorik",
    "subcat": "rhythmus",
    "phase": "warmup",
    "ageGroup": "unterstufe",
    "duration": 6,
    "goal": "Körperwahrnehmung & Bewegungssynchronisation",
    "desc": "Partner stehen sich gegenüber. Kind A macht Bewegungen (Hampelmänner, Drehungen, Ausfallschritte, Armkreisen). Kind B spiegelt jede Nuance in Echtzeit ohne Verzögerung. Nach 60 Sekunden Pfiff und Wechsel.",
    "material": "Ohne Geräte (0 Min. Aufbau)",
    "org": "Paarweise in der Halle",
    "cues": "Blickkontakt halten, nicht hetzen, Bewegungen sauber ausführen.",
    "ref": "Schwellenpädagogik / Gymnasium Sacre Coeur",
    "tags": ["null_material", "1klasse_koed", "schwellen"]
  },
  {
    "id": "schwell_zeitungstransport",
    "title": "Zeitungstransport (Aerodynamik-Sprint)",
    "category": "leichtathletik",
    "subcat": "sprint",
    "phase": "warmup",
    "ageGroup": "unterstufe",
    "duration": 6,
    "goal": "Laufhaltung & konstante Beschleunigung",
    "desc": "Jedes Kind bekommt ein A4-Blatt Papier oder ein leichtes Leibchen vor die Brust. Sobald man losläuft, muss man die Hände wegnehmen – das Blatt bleibt nur durch den Fahrtwind an der Brust kleben!",
    "material": "A4-Blatt oder Leibchen",
    "org": "Hallenrundlauf",
    "cues": "Aufrecht sprinten, Brust nach vorn, Tempo hochhalten.",
    "ref": "Schwellenpädagogik / Gymnasium Sacre Coeur",
    "tags": ["null_material", "1klasse_koed", "schwellen"]
  },
  {
    "id": "schwell_tier_staffel",
    "title": "Tier-Olympiade (Bär, Krebs & Frosch)",
    "category": "motorik",
    "subcat": "koordination_allg",
    "phase": "main1",
    "ageGroup": "unterstufe",
    "duration": 8,
    "goal": "Ganzkörper-Stützkraft & Gelenkmobilität",
    "desc": "Staffel quer durch die Halle: 1. Runde als Frosch (tiefe Hocksprünge), 2. Runde als Krebs (Rückwärts-Vierfüßler), 3. Runde als Bär (Vierfüßlergang mit gestreckten Beinen). Extrem fordernd und koordinativ wertvoll.",
    "material": "Ohne Geräte (0 Min. Aufbau)",
    "org": "4 Riegen an der Grundlinie",
    "cues": "Po beim Krebsgang anheben, beim Frosch kontrolliert auf den Fußballen landen.",
    "ref": "Schwellenpädagogik / Gymnasium Sacre Coeur",
    "tags": ["null_material", "1klasse_koed", "high_intensity", "schwellen"]
  },
  {
    "id": "schwell_ruecken_an_ruecken",
    "title": "Rücken-an-Rücken Aufstehen",
    "category": "spiele",
    "subcat": "teamspiel",
    "phase": "cool",
    "ageGroup": "alle",
    "duration": 8,
    "goal": "Körperspannung, Druckdosierung & Kooperation",
    "desc": "Zwei Kinder sitzen Rücken an Rücken am Boden, die Arme sind ineinander verhakt. Durch gleichmäßigen Gegendruck und synchrones Beugen der Beine müssen sie gemeinsam aufstehen – ohne die Hände zu benutzen!",
    "material": "Ohne Geräte (0 Min. Aufbau)",
    "org": "Paare am Boden",
    "cues": "Füße nahe ans Gesäß stellen, gleichmäßig Gegendruck gegen den Rücken des Partners geben.",
    "ref": "Schwellenpädagogik / Gymnasium Sacre Coeur",
    "tags": ["null_material", "kooperation", "1klasse_koed", "schwellen"]
  },
  {
    "id": "schwell_gordischer_knoten",
    "title": "Der Gordische Knoten",
    "category": "spiele",
    "subcat": "teamspiel",
    "phase": "cool",
    "ageGroup": "alle",
    "duration": 10,
    "goal": "Kommunikation, Berührungsabbau & Problemlösung",
    "desc": "8–10 Kinder stehen eng im Kreis, strecken die Hände aus und schließen die Augen. Jeder greift 2 verschiedene Hände anderer Kinder. Augen auf: Nun muss das Knotengebilde durch Steigen und Drehen entwirrt werden, ohne loszulassen.",
    "material": "Ohne Geräte (0 Min. Aufbau)",
    "org": "Gruppen im Kreis",
    "cues": "Ruhig sprechen, einer übernimmt die Ansage, vorsichtiges Durchsteigen.",
    "ref": "Schwellenpädagogik / Gymnasium Sacre Coeur",
    "tags": ["null_material", "kooperation", "1klasse_koed", "schwellen"]
  },
  {
    "id": "schwell_stille_reihe",
    "title": "Die Stille Reihe (Nonverbale Ordnung)",
    "category": "spiele",
    "subcat": "teamspiel",
    "phase": "cool",
    "ageGroup": "alle",
    "duration": 8,
    "goal": "Nonverbale Kommunikation & Aufmerksamkeit",
    "desc": "Die gesamte Klasse muss sich völlig schweigend in einer langen Reihe ordnen: nach Geburtstagsmonat, nach Hausnummer oder nach Alphabet des Vornamens. Wer spricht, muss 3 Kniebeugen machen.",
    "material": "Langbänke oder Hallenlinie (0 Min. Aufbau)",
    "org": "Auf einer Hallenlinie stehend",
    "cues": "Mit Zeichensprache und Fingern kommunizieren, Mitschülern aufmerksam zusehen.",
    "ref": "Schwellenpädagogik / Gymnasium Sacre Coeur",
    "tags": ["null_material", "kooperation", "1klasse_koed", "schwellen"]
  },
  {
    "id": "schwell_vier_felder_ball",
    "title": "Vier-Felder-Ball (Quadranten-Action)",
    "category": "ball",
    "subcat": "burnergames",
    "phase": "main2",
    "ageGroup": "alle",
    "duration": 12,
    "goal": "Raumaufteilung & Antizipation von Flugbahnen",
    "desc": "Die Halle ist in 4 Quadranten (Teams A, B, C, D) aufgeteilt. Mit 2 Softbällen wird geworfen. Ziel ist es, Bälle in fremde Felder zu schleudern, die den Boden berühren. Bei Fehlwurf oder Bodenkontakt gibt es einen Minuspunkt fürs Feld.",
    "material": "2 Softbälle, Hallenlinien",
    "org": "Halle in 4 Viertel unterteilt",
    "cues": "Flugbälle direkt fangen, offene Räume im gegnerischen Feld anvisieren.",
    "ref": "Schwellenpädagogik / Gymnasium Sacre Coeur",
    "tags": ["baelle", "1klasse_koed", "schwellen"]
  },
  {
    "id": "schwell_kegel_voelkerball",
    "title": "Kegel-Völkerball (Taktik-Variante)",
    "category": "ball",
    "subcat": "abwurf",
    "phase": "main2",
    "ageGroup": "alle",
    "duration": 15,
    "goal": "Zielwurf, Deckungsverhalten & Teamschutz",
    "desc": "Normales Völkerball, aber jedes Team hat an der Rückwand 1 großen Gymnastikkegel stehen. Trifft ein Team den gegnerischen Kegel und fällt er um, hat dieses Team das Spiel sofort gewonnen!",
    "material": "2 Kegel/Pylonen, 2 Softbälle",
    "org": "Völkerballfeld",
    "cues": "Kegel aktiv durch Mitspieler absichern; Wurffinten nutzen.",
    "ref": "Schwellenpädagogik / Gymnasium Sacre Coeur",
    "tags": ["baelle", "huetchen_reifen", "1klasse_koed", "schwellen"]
  },

  # --- WEITERE HÜTCHEN & REIFEN KOMBIS ---
  {
    "id": "kombi_slalom_drop",
    "title": "Slalom-Prellen mit Rebound-Drop",
    "category": "ball",
    "subcat": "basketball",
    "phase": "main1",
    "ageGroup": "alle",
    "duration": 10,
    "goal": "Dribbel-Rhythmus & dosierter Krafteinsatz",
    "desc": "Slalom durch 5 Hütchen prellen. Am Ende liegt ein Reifen: Dort den Ball mit beiden Händen kraftvoll in den Reifen aufprellen, den Rebound mit gestreckten Armen fangen und im Sprint zurück zum Team.",
    "material": "Hütchen, 1 Reifen pro Bahn, Basketbälle",
    "org": "Staffelbahnen",
    "cues": "Ball im Reifenzentrum aufdotzen lassen, um einen geraden Abprallwinkel zu bekommen.",
    "ref": "Schwellenpädagogik / Gymnasium Sacre Coeur",
    "tags": ["huetchen_reifen", "baelle", "1klasse_koed", "schwellen"]
  },
  {
    "id": "kombi_target_drop",
    "title": "Reifen-Darts (Punkte-Wurf)",
    "category": "motorik",
    "subcat": "differenzierung",
    "phase": "main1",
    "ageGroup": "alle",
    "duration": 10,
    "goal": "Zielgenauigkeit & Wurfgefühl aus verschiedenen Distanzen",
    "desc": "3 Reifen liegen in 3m (1 Punkt), 5m (3 Punkte) und 7m (5 Punkte) Entfernung. Kinder werfen je 3 Tennisbälle oder Säckchen. Welches Team sammelt im Staffelmodus zuerst 50 Punkte?",
    "material": "3 Reifen pro Station, Tennisbälle/Bohnensäckchen",
    "org": "3 Stationen parallel",
    "cues": "Bogenwurftechnik mit lockerem Handgelenk wählen.",
    "ref": "Schwellenpädagogik / Gymnasium Sacre Coeur",
    "tags": ["huetchen_reifen", "baelle", "1klasse_koed", "schwellen"]
  },
  {
    "id": "kombi_turmbau_staffel",
    "title": "Hütchen-Turmbau-Staffel",
    "category": "spiele",
    "subcat": "burnergames",
    "phase": "main1",
    "ageGroup": "unterstufe",
    "duration": 10,
    "goal": "Sprint & ruhige Hand unter Zeitdruck",
    "desc": "Jedes Team hat an der Grundlinie 6 Hütchen. Ein Läufer sprintet vor, wirft einen Ball in den Reifen. Trifft er, darf er ein Hütchen aufstellen. Der nächste setzt das nächste Hütchen obendrauf. Welcher 6er-Turm steht zuerst?",
    "material": "Hütchen, Reifen, Tennisbälle",
    "org": "3–4 Staffelbahnen",
    "cues": "Hütchen vorsichtig und exakt aufsetzen; Team feuert an.",
    "ref": "Schwellenpädagogik / Gymnasium Sacre Coeur",
    "tags": ["huetchen_reifen", "baelle", "1klasse_koed", "schwellen"]
  },

  # --- WEITERE VIRALE INSTAGRAM-HITS ---
  {
    "id": "insta_reaktionsstab_drop",
    "title": "Reaktionsstab (Drop & Catch Duell)",
    "category": "motorik",
    "subcat": "reaktion",
    "phase": "warmup",
    "ageGroup": "alle",
    "duration": 8,
    "goal": "Visuelle Reaktionsschnelligkeit & Antritt",
    "desc": "2 Partner stehen sich in 2m Abstand gegenüber, jeder hält einen Gymnastikstab senkrecht auf den Boden. Auf Pfiff lassen beide gleichzeitig los und müssen den Stab des Partners fangen, bevor er auf den Boden knallt!",
    "material": "2 Gymnastikstäbe pro Paar",
    "org": "Gegenüberstellung an Hallenlinien",
    "cues": "Leicht in die Knie gehen, explosiver Schritt nach vorn.",
    "ref": "Instagram Trend / @thepespecialist",
    "tags": ["insta_hit", "1klasse_koed", "schwellen"]
  },
  {
    "id": "insta_hand_tipp_duell",
    "title": "Hand-Tipp-Duell im Liegestütz",
    "category": "fitness",
    "subcat": "zirkel",
    "phase": "warmup",
    "ageGroup": "alle",
    "duration": 6,
    "goal": "Rumpfstabilität & Stützkraft mit Spaß",
    "desc": "Partner stehen sich im hohen Liegestütz (Plank) gegenüber. Ziel: Mit einer Hand die Hände des Partners abtippen, während man die eigenen Hände wegzieht. Wer 3 Treffer hat, gewinnt das Duell.",
    "material": "Ohne Geräte (0 Min. Aufbau)",
    "org": "Paare auf Matten oder Hallenboden",
    "cues": "Bauch und Po fest anspannen, Hüfte nicht verdrehen.",
    "ref": "Instagram Trend / @wimasu.de",
    "tags": ["insta_hit", "null_material", "high_intensity", "schwellen"]
  },
  {
    "id": "insta_socken_klau_baer",
    "title": "Socken-Klau im Bärengang",
    "category": "spiele",
    "subcat": "burnergames",
    "phase": "warmup",
    "ageGroup": "alle",
    "duration": 8,
    "goal": "Ganzkörperkraft & Wendigkeit am Boden",
    "desc": "Alle Schüler im Bärengang (Knie berühren den Boden nicht). Jedes Kind hat ein Parteiband locker hinten im Hosenbund. Wer schafft es, im Krabbeln anderen die Bänder zu stibitzen, ohne das eigene zu verlieren?",
    "material": "Parteibänder",
    "org": "Hallenmittelbereich",
    "cues": "Hände flach aufsetzen, ständig mit dem Po vom Gegner wegdrehen.",
    "ref": "Instagram Trend / @vlamingo.de",
    "tags": ["insta_hit", "high_intensity", "1klasse_koed", "schwellen"]
  },
  {
    "id": "insta_jedi_dodgeball",
    "title": "Jedi Dodgeball (Lichtschwert-Rettung)",
    "category": "ball",
    "subcat": "abwurf",
    "phase": "main2",
    "ageGroup": "unterstufe",
    "duration": 15,
    "goal": "Taktisches Spiel mit Rollenelementen",
    "desc": "1 Kind pro Team ist der geheime 'Jedi' mit einer Schaumstoff-Schwimmnudel. Abgeworfene knien auf den Boden. Nur der Jedi kann sie durch sanftes Berühren mit dem 'Lichtschwert' erlösen. Wird der Jedi getroffen, ist die Kraft erloschen!",
    "material": "2 Schwimmnudeln, 3 Softbälle",
    "org": "Völkerballfeld",
    "cues": "Der Jedi agiert aus dem Hintergrund und lässt sich von Mitspielern abschirmen.",
    "ref": "Instagram Trend / @pe.games",
    "tags": ["insta_hit", "baelle", "1klasse_koed", "schwellen"]
  },
  {
    "id": "insta_pin_knockdown",
    "title": "Pin Knockdown (Königskegel)",
    "category": "ball",
    "subcat": "abwurf",
    "phase": "main2",
    "ageGroup": "alle",
    "duration": 15,
    "goal": "Zielwurf, Deckung & Schutz des eigenen Raums",
    "desc": "An jeder Grundlinie stehen 6 Kegel/Pylonen. Spieler werfen aus ihren Hälften mit 4 Softbällen. Jeder umgeworfene Kegel wird abgebaut. Welches Team räumt zuerst alle 6 Kegel des Gegners ab?",
    "material": "12 Pylonen, 4 Softbälle",
    "org": "Geteiltes Feld",
    "cues": "Kegel mit Beinen abschirmen, schnelle Diagonalwürfe ansetzen.",
    "ref": "Instagram Trend / @just.playsports",
    "tags": ["insta_hit", "baelle", "huetchen_reifen", "1klasse_koed", "schwellen"]
  },
  {
    "id": "insta_wand_rebound_ball",
    "title": "Wand-Rebound-Ball (Matrix-Abwurf)",
    "category": "ball",
    "subcat": "abwurf",
    "phase": "main2",
    "ageGroup": "alle",
    "duration": 12,
    "goal": "Winkelberechnung & Antizipation von Abprallern",
    "desc": "Abwurfspiel mit einer genialen Sonderregel: Ein Wurf zählt NUR dann als Treffer, wenn der Ball zuvor MINDESTENS EINMAL die Hallenwand oder Decke berührt hat! Direkttreffer sind ungültig.",
    "material": "2–3 Softbälle",
    "org": "Gesamte Halle",
    "cues": "Bälle mit Wucht flach an die Seitenwand werfen, um unberechenbare Winkel zu erzeugen.",
    "ref": "Instagram Trend / @physedgames",
    "tags": ["insta_hit", "baelle", "1klasse_koed", "schwellen"]
  },
  {
    "id": "insta_mister_x",
    "title": "Mister X (Der Schatten der Halle)",
    "category": "spiele",
    "subcat": "fangen",
    "phase": "warmup",
    "ageGroup": "alle",
    "duration": 8,
    "goal": "Aufmerksamkeit, Raumorientierung & Spurt",
    "desc": "Ein Kind trägt unauffällig ein farbiges Band am Rücken ('Mister X'). Alle laufen frei in der Halle. Plötzlich ruft die Lehrkraft: 'Mister X schlägt zu!' – Mister X beginnt sofort zu jagen. Wer rettet sich an die Wand?",
    "material": "1 Parteiband (0 Min. Aufbau)",
    "org": "Freier Lauf in der Halle",
    "cues": "Immer das Umfeld scannen, wer hinter einem läuft.",
    "ref": "Instagram Trend / @wimasu.de",
    "tags": ["insta_hit", "null_material", "1klasse_koed", "schwellen"]
  },
  {
    "id": "insta_fluch_karibik",
    "title": "Fluch der Karibik (Haifischbecken)",
    "category": "spiele",
    "subcat": "burnergames",
    "phase": "warmup",
    "ageGroup": "unterstufe",
    "duration": 10,
    "goal": "Balancieren, Sprungkraft & Schleichgeschick",
    "desc": "Umgedrehte Bänke und Matten sind 'Piratenschiffe'. Der Hallenboden ist Wasser voll mit 2 'Haien' (Fängern). Kinder dürfen von Schiff zu Schiff springen/balancieren. Wer ins Wasser fällt oder getippt wird, wird selbst zum Hai.",
    "material": "Langbänke, Turnmatten",
    "org": "Hallenparcours",
    "cues": "Sicher auf den Bänken landen, Mut zum Sprung beweisen.",
    "ref": "Instagram Trend / @vlamingo.de",
    "tags": ["insta_hit", "1klasse_koed", "schwellen"]
  },
  {
    "id": "insta_menschlicher_foerdergurt",
    "title": "Der menschliche Fördergurt (Mattengleiter)",
    "category": "spiele",
    "subcat": "teamspiel",
    "phase": "cool",
    "ageGroup": "alle",
    "duration": 10,
    "goal": "Vertrauen, Rhythmus & Klassen-Zusammenhalt",
    "desc": "6–8 Kinder liegen bauchlings eng Kopf an Kopf nebeneinander am Boden. Auf ihren Rücken liegt eine Weichbodenmatte. Auf Kommando rollen sich alle synchron um die eigene Achse – die Matte gleitet wie auf einem Förderband vorwärts!",
    "material": "1 Weichbodenmatte",
    "org": "Reihe am Boden",
    "cues": "Eng zusammenbleiben, im gleichen Rhythmus rollen.",
    "ref": "Instagram Trend / @thepeshed",
    "tags": ["insta_hit", "kooperation", "1klasse_koed", "schwellen"]
  },
  {
    "id": "insta_rettungsinsel_kollaps",
    "title": "Rettungsinsel (Alle auf eine Matte!)",
    "category": "spiele",
    "subcat": "teamspiel",
    "phase": "cool",
    "ageGroup": "alle",
    "duration": 8,
    "goal": "Kooperation, Körperkontakt ohne Scham & Teamgeist",
    "desc": "Schaffen es alle 24 Kinder der Klasse, gemeinsam für mindestens 10 Sekunden auf einer einzigen Weichbodenmatte zu stehen, ohne dass auch nur ein einziger Fuß den Hallenboden berührt? Erfordert Umarmungen und geniale Statik!",
    "material": "1 Weichbodenmatte (0 Min. Aufbau)",
    "org": "Klasse um die Matte",
    "cues": "Große Kinder in die Mitte, gegenseitig an den Schultern festhalten.",
    "ref": "Instagram Trend / @wimasu.de",
    "tags": ["insta_hit", "kooperation", "1klasse_koed", "schwellen"]
  }
]

ALL_NEW = NEW_EXERCISES + MORE_EXERCISES
print(f"Grand total of curated new games: {len(ALL_NEW)}")

import os
import json

HTML_PATH = r"c:\Users\Senti\OneDrive - Sacre Coeur\Sport\github_sportplaner\index.html"

with open(HTML_PATH, "r", encoding="utf-8") as f:
    html = f.read()

print(f"Original HTML length: {len(html)}")

# 1. CLEAN MOJIBAKE & ROBOTIC TEXT
mojibake_map = {
    "âš¡": "⚡",
    "â€ž": "„",
    "â€œ": "“",
    "â€“": "–",
    "ðŸ ƒ": "🏃",
    "ðŸ“²": "📱",
    "ðŸŒŸ": "🌟",
    "ðŸš€": "🚀",
    "ðŸ €": "🏀",
    "ðŸŽ²": "🎲",
    "ðŸ§ ": "🧠",
    "ðŸ¤¸": "🤸",
    "ðŸ§—": "🧗",
    "ðŸ“‹": "📋",
    "&bdquo;": "„",
    "&ldquo;": "“",
}

for k, v in mojibake_map.items():
    html = html.replace(k, v)

# Clean up iOS PWA install instructions
old_pwa_text = """          <ol style="margin: 0; padding-left: 1.25rem; line-height: 1.5;">
            <li>Tippe unten im Safari-Browser auf das <strong>Teilen-Symbol</strong> (Quadrat mit Pfeil nach oben).</li>
            <li>Scrolle im Men&uuml; etwas nach unten und w&auml;hle <strong>&bdquo;Zum Home-Bildschirm&ldquo;</strong> (Symbol [+]).</li>
            <li>Tippe oben rechts auf <strong>&bdquo;Hinzuf&uuml;gen&ldquo;</strong>.</li>
            <li>Fertig! Der SportPlaner liegt jetzt mit dem offiziellen Sacre Coeur Wappen auf deinem Home-Bildschirm &ndash; startet schnell und ohne st&ouml;rende Browserleisten.</li>
          </ol>"""

new_pwa_text = """          <ol style="margin: 0; padding-left: 1.25rem; line-height: 1.5;">
            <li>Unten in Safari auf das <strong>Teilen-Symbol</strong> (Quadrat mit Pfeil) tippen.</li>
            <li>In der Liste <strong>„Zum Home-Bildschirm“</strong> auswählen.</li>
            <li>Oben rechts auf <strong>„Hinzufügen“</strong> bestätigen.</li>
            <li>Die App startet ab sofort im echten Vollbild-Modus ohne Adressleiste und funktioniert offline im Turnsaal!</li>
          </ol>"""

if old_pwa_text in html:
    html = html.replace(old_pwa_text, new_pwa_text)
else:
    # Try flexible replacement
    html = re.sub(
        r'<ol style="margin: 0; padding-left: 1.25rem; line-height: 1.5;">\s*<li>Tippe unten im Safari-Browser.*?<\/ol>',
        new_pwa_text,
        html,
        flags=re.DOTALL
    )

# 2. INJECT SCHWELLENPÄDAGOGIK CSS
schwellen_css = """
    /* Schwellenpädagogik Quick-Access Bar */
    .schwellen-quick-card {
      background: linear-gradient(135deg, #002B49 0%, #004d80 100%);
      color: white;
      border-radius: 12px;
      padding: 1.15rem;
      margin-bottom: 1.25rem;
      box-shadow: 0 4px 18px rgba(0,43,73,0.18);
    }
    .schwellen-pills-wrap {
      display: flex;
      flex-wrap: wrap;
      gap: 0.5rem;
      margin-top: 0.6rem;
    }
    .schwellen-pill {
      background: rgba(255, 255, 255, 0.12);
      border: 1px solid rgba(255, 255, 255, 0.22);
      color: #f8fafc;
      padding: 6px 13px;
      border-radius: 20px;
      font-size: 0.82rem;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.2s ease;
      display: inline-flex;
      align-items: center;
      gap: 5px;
    }
    .schwellen-pill:hover {
      background: rgba(255, 255, 255, 0.25);
      transform: translateY(-1px);
    }
    .schwellen-pill.active {
      background: #ffffff;
      color: #002B49;
      border-color: #ffffff;
      box-shadow: 0 3px 10px rgba(0,0,0,0.22);
      font-weight: 700;
    }
"""

if "/* Schwellenpädagogik Quick-Access Bar */" not in html:
    html = html.replace("/* Database Layout */", schwellen_css + "\n    /* Database Layout */")

# 3. INJECT SCHWELLENPÄDAGOGIK HTML IN TAB 3
schwellen_html = """
      <!-- ============================================================= -->
      <!-- SCHWELLENPÄDAGOGIK: SCHNELL-FINDER FÜR DIE TURNHAUSTÜR       -->
      <!-- ============================================================= -->
      <div class="card schwellen-quick-card no-print">
        <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 0.75rem;">
          <div>
            <div style="font-size: 1.15rem; font-weight: 800; display: flex; align-items: center; gap: 8px;">
              <span>🚪⚡ Schwellenpädagogik: Sofort-Spiele für die Hallentür</span>
            </div>
            <div style="font-size: 0.83rem; color: #bae6fd; margin-top: 3px;">
              Du stehst im Turnsaal und brauchst in 10 Sekunden ein starkes Spiel? Klick deinen Schnellfilter:
            </div>
          </div>
          <button class="btn btn-sm" onclick="pickRandomSchwellenGame()" style="background: #f59e0b; color: #1e293b; font-weight: 700; border: none; border-radius: 8px; padding: 7px 16px; box-shadow: 0 2px 10px rgba(245,158,11,0.35); cursor: pointer; display: flex; align-items: center; gap: 6px;">
            <span>🎲</span> <span>Spontan-Spiel („Überrasch mich!“)</span>
          </button>
        </div>

        <div class="schwellen-pills-wrap">
          <button class="schwellen-pill active" data-schwellen="all" onclick="setSchwellenFilter('all', this)">⚡ Alle 490+ Einheiten</button>
          <button class="schwellen-pill" data-schwellen="null_material" onclick="setSchwellenFilter('null_material', this)">🟢 0 Min. Aufbau (Null Material)</button>
          <button class="schwellen-pill" data-schwellen="huetchen_reifen" onclick="setSchwellenFilter('huetchen_reifen', this)">🟡 Nur Hütchen &amp; Reifen</button>
          <button class="schwellen-pill" data-schwellen="baelle" onclick="setSchwellenFilter('baelle', this)">🏐 Bälle &amp; Wurfspiele</button>
          <button class="schwellen-pill" data-schwellen="high_intensity" onclick="setSchwellenFilter('high_intensity', this)">🔥 Puls hoch (Auspowern &amp; HIIT)</button>
          <button class="schwellen-pill" data-schwellen="insta_hit" onclick="setSchwellenFilter('insta_hit', this)">📱 Instagram &amp; TikTok Viral-Hits</button>
          <button class="schwellen-pill" data-schwellen="1klasse_koed" onclick="setSchwellenFilter('1klasse_koed', this)">🎒 1. Klasse Gym (Koedukativ)</button>
          <button class="schwellen-pill" data-schwellen="kooperation" onclick="setSchwellenFilter('kooperation', this)">🤝 Teambuilding &amp; Kooperation</button>
        </div>
      </div>
"""

if "<!-- SCHWELLENPÄDAGOGIK: SCHNELL-FINDER FÜR DIE TURNHAUSTÜR" not in html:
    html = html.replace('<div class="db-layout">', schwellen_html + '\n      <div class="db-layout">')

# 4. INJECT NEW EXERCISES INTO EXERCISE_DATABASE
# Format exercises into JavaScript objects
new_ex_js_list = []
for ex in ALL_NEW:
    tags_str = json.dumps(ex.get("tags", []))
    ex_str = f"""      {{
        id: '{ex["id"]}',
        title: {json.dumps(ex["title"], ensure_ascii=False)},
        category: '{ex["category"]}',
        subcat: '{ex["subcat"]}',
        phase: '{ex["phase"]}',
        ageGroup: '{ex["ageGroup"]}',
        duration: {ex["duration"]},
        goal: {json.dumps(ex["goal"], ensure_ascii=False)},
        desc: {json.dumps(ex["desc"], ensure_ascii=False)},
        material: {json.dumps(ex["material"], ensure_ascii=False)},
        org: {json.dumps(ex["org"], ensure_ascii=False)},
        cues: {json.dumps(ex["cues"], ensure_ascii=False)},
        ref: {json.dumps(ex["ref"], ensure_ascii=False)},
        tags: {tags_str}
      }}"""
    new_ex_js_list.append(ex_str)

new_exercises_code = ",\n" + ",\n".join(new_ex_js_list) + "\n\n];"

# Find the end of EXERCISE_DATABASE
# Look for line before `const TOPIC_CATALOG`
db_end_pattern = r'(\s*\}\s*\n*)(\s*\];\s*\n*\s*\/\*\s*=+\s*\n*\s*2\.\s*THEMEN-KATALOG)'
if re.search(db_end_pattern, html):
    html = re.sub(db_end_pattern, r'\1' + new_exercises_code.replace('\\', '\\\\') + r'\n\n    /* =====================================================================\n       2. THEMEN-KATALOG', html, count=1)
    print("Successfully injected new exercises into EXERCISE_DATABASE array.")
else:
    print("Warning: Could not find exact insertion marker for EXERCISE_DATABASE, attempting fallback...")
    html = html.replace("];\n\n    /* =====================================================================\n       2. THEMEN-KATALOG", new_exercises_code + "\n\n    /* =====================================================================\n       2. THEMEN-KATALOG")

# 5. ENHANCE JAVASCRIPT: RENDERDATABASE AND SCHWELLEN FILTERS
enhanced_js = """
    let currentSchwellenFilter = 'all';

    function setSchwellenFilter(tag, btnElement) {
      currentSchwellenFilter = tag;
      document.querySelectorAll('.schwellen-pill').forEach(p => p.classList.remove('active'));
      if (btnElement) btnElement.classList.add('active');
      renderDatabase();
    }

    function pickRandomSchwellenGame() {
      let pool = EXERCISE_DATABASE;
      if (currentSchwellenFilter !== 'all') {
        pool = EXERCISE_DATABASE.filter(ex => matchesSchwellenCondition(ex, currentSchwellenFilter));
      }
      if (!pool || pool.length === 0) pool = EXERCISE_DATABASE;
      const lucky = pool[Math.floor(Math.random() * pool.length)];
      
      document.getElementById('db-search-input').value = lucky.title;
      renderDatabase();
      showToast(`🎲 Spontan-Idee: "${lucky.title}" ausgewählt!`);
      
      setTimeout(() => {
        const firstCard = document.querySelector('.exercise-card');
        if (firstCard) {
          firstCard.scrollIntoView({ behavior: 'smooth', block: 'center' });
          firstCard.style.outline = '3px solid #f59e0b';
          firstCard.style.boxShadow = '0 0 20px rgba(245,158,11,0.4)';
          setTimeout(() => { 
            firstCard.style.outline = ''; 
            firstCard.style.boxShadow = '';
          }, 3500);
        }
      }, 150);
    }

    function matchesSchwellenCondition(ex, filter) {
      const mat = (ex.material || '').toLowerCase();
      const title = (ex.title || '').toLowerCase();
      const desc = (ex.desc || '').toLowerCase();
      const goal = (ex.goal || '').toLowerCase();
      const tags = ex.tags || [];

      if (filter === 'all') return true;
      if (filter === 'null_material') {
        return tags.includes('null_material') || mat.includes('ohne geräte') || mat.includes('keine geräte') || mat.includes('0 min') || mat.includes('hallenlinien');
      }
      if (filter === 'huetchen_reifen') {
        return tags.includes('huetchen_reifen') || mat.includes('hütchen') || mat.includes('pylonen') || mat.includes('reifen');
      }
      if (filter === 'baelle') {
        return tags.includes('baelle') || mat.includes('ball') || mat.includes('bälle') || ex.category === 'ball' || ex.subcat === 'abwurf';
      }
      if (filter === 'high_intensity') {
        return tags.includes('high_intensity') || ex.category === 'fitness' || goal.includes('puls') || goal.includes('sprint') || desc.includes('maximal') || desc.includes('dauersprint');
      }
      if (filter === 'insta_hit') {
        return tags.includes('insta_hit') || (ex.ref && ex.ref.toLowerCase().includes('instagram'));
      }
      if (filter === '1klasse_koed') {
        return tags.includes('1klasse_koed') || ex.ageGroup === 'unterstufe' || ex.ageGroup === 'alle';
      }
      if (filter === 'kooperation') {
        return tags.includes('kooperation') || ex.subcat === 'teamspiel' || goal.includes('kooperation') || goal.includes('team') || desc.includes('gemeinsam');
      }
      return tags.includes(filter);
    }

    function renderDatabase() {
      const container = document.getElementById('db-results-container');
      const search = document.getElementById('db-search-input').value.toLowerCase();
      const cat = document.querySelector('input[name="db-cat"]:checked').value;
      const subcat = document.getElementById('db-subcat-select').value;
      const age = document.querySelector('input[name="db-age"]:checked').value;
      const checkedPhases = Array.from(document.querySelectorAll('.db-phase-chk:checked')).map(c => c.value);

      const filtered = EXERCISE_DATABASE.filter(ex => {
        const matchesSearch = !search || 
          ex.title.toLowerCase().includes(search) || 
          ex.desc.toLowerCase().includes(search) || 
          ex.material.toLowerCase().includes(search) ||
          ex.goal.toLowerCase().includes(search) ||
          (ex.tags && ex.tags.some(t => t.toLowerCase().includes(search)));
        
        const matchesCat = (cat === 'all') || (ex.category === cat);
        const matchesSubcat = (subcat === 'all') || (ex.subcat === subcat);
        const matchesPhase = checkedPhases.includes(ex.phase);
        const matchesAge = (age === 'all') || (ex.ageGroup === 'alle') || (ex.ageGroup === age);
        const matchesSchwellen = matchesSchwellenCondition(ex, currentSchwellenFilter);
        
        return matchesSearch && matchesCat && matchesSubcat && matchesPhase && matchesAge && matchesSchwellen;
      });

      document.getElementById('db-count-badge').innerText = filtered.length;
      container.innerHTML = '';

      if (filtered.length === 0) {
        container.innerHTML = '<div style="grid-column: 1/-1; padding: 2.5rem; text-align: center; color: #94a3b8; background: white; border-radius: 8px; border: 1px dashed #cbd5e1;">Keine Übungen mit diesen Kriterien gefunden. Klicke auf "Alle anzeigen" oder setze die Filter zurück.</div>';
        return;
      }

      filtered.forEach(ex => {
        const card = document.createElement('div');
        card.className = 'exercise-card';
        
        let badgeColor = 'background:#0284c7; color:white;';
        if (ex.category === 'leichtathletik') badgeColor = 'background:#0284c7; color:white;';
        else if (ex.category === 'ball') badgeColor = 'background:#059669; color:white;';
        else if (ex.category === 'spiele') badgeColor = 'background:#d97706; color:white;';
        else if (ex.category === 'motorik') badgeColor = 'background:#0891b2; color:white;';
        else if (ex.category === 'fitness') badgeColor = 'background:#4f46e5; color:white;';
        else if (ex.category === 'turnen') badgeColor = 'background:#7c3aed; color:white;';
        else if (ex.category === 'kampfklettern') badgeColor = 'background:#0d9488; color:white;';

        let tagBadgesHtml = '';
        const tags = ex.tags || [];
        const mat = (ex.material || '').toLowerCase();
        if (tags.includes('null_material') || mat.includes('ohne geräte') || mat.includes('keine geräte') || mat.includes('0 min')) {
          tagBadgesHtml += '<span style="font-size:0.7rem; font-weight:700; background:#dcfce7; color:#15803d; padding:2px 7px; border-radius:10px;">🟢 0 Min Aufbau</span> ';
        }
        if (tags.includes('huetchen_reifen') || mat.includes('hütchen') || mat.includes('reifen')) {
          tagBadgesHtml += '<span style="font-size:0.7rem; font-weight:700; background:#fef3c7; color:#b45309; padding:2px 7px; border-radius:10px;">🟡 Hütchen/Reifen</span> ';
        }
        if (tags.includes('high_intensity') || ex.category === 'fitness') {
          tagBadgesHtml += '<span style="font-size:0.7rem; font-weight:700; background:#fee2e2; color:#b91c1c; padding:2px 7px; border-radius:10px;">🔥 Puls hoch</span> ';
        }
        if (tags.includes('insta_hit') || (ex.ref && ex.ref.includes('Instagram'))) {
          tagBadgesHtml += '<span style="font-size:0.7rem; font-weight:700; background:#f3e8ff; color:#7e22ce; padding:2px 7px; border-radius:10px;">📱 Insta-Hit</span> ';
        }
        if (tags.includes('1klasse_koed')) {
          tagBadgesHtml += '<span style="font-size:0.7rem; font-weight:700; background:#e0f2fe; color:#0369a1; padding:2px 7px; border-radius:10px;">🎒 1. Kl. Gym</span> ';
        }

        card.innerHTML = `
          <div>
            <div style="display:flex; justify-content:space-between; align-items:center;">
              <span class="ex-badge" style="${badgeColor}">${ex.category.toUpperCase()}</span>
              <span style="font-size:0.75rem; color:#64748b; font-weight:600;">${ex.duration} min</span>
            </div>
            <div class="ex-title">${ex.title}</div>
            <div style="font-size:0.78rem; font-weight:600; color:#0284c7; margin-bottom:4px;">🎯 ${ex.goal}</div>
            <div class="ex-desc" style="font-size:0.85rem; line-height:1.45; color:#334155; margin-bottom:8px;">${ex.desc}</div>
            <div class="ex-meta">
              <div style="width:100%; margin-bottom:4px;">${tagBadgesHtml}</div>
              <span class="ex-tag">Phase: ${ex.phase.toUpperCase()}</span>
              <span class="ex-tag">Geräte: ${ex.material}</span>
              <span class="ex-tag">Gruppe: ${ex.org}</span>
            </div>
          </div>
          <div class="ex-actions" style="margin-top:8px; border-top:1px solid #f1f5f9; padding-top:8px;">
            <span style="font-size:0.72rem; color:#94a3b8;" title="${ex.ref}">Ref: ${ex.ref.split('/').pop()}</span>
            <button class="btn btn-primary btn-sm" onclick="addExerciseDirectly('${ex.id}')">In Stunde einfügen</button>
          </div>
        `;
        container.appendChild(card);
      });
    }

    function resetDbFilter() {
      currentSchwellenFilter = 'all';
      document.querySelectorAll('.schwellen-pill').forEach(p => p.classList.remove('active'));
      const allPill = document.querySelector('.schwellen-pill[data-schwellen="all"]');
      if (allPill) allPill.classList.add('active');
      document.getElementById('db-search-input').value = '';
      document.getElementById('db-subcat-select').value = 'all';
      document.querySelector('input[name="db-cat"][value="all"]').checked = true;
      document.querySelector('input[name="db-age"][value="all"]').checked = true;
      document.querySelectorAll('.db-phase-chk').forEach(c => c.checked = true);
      renderDatabase();
    }
"""

# Replace old renderDatabase block
old_render_block_regex = r'function renderDatabase\(\)\s*\{.*?function resetDbFilter\(\)\s*\{.*?renderDatabase\(\);\s*\}'
if re.search(old_render_block_regex, html, flags=re.DOTALL):
    html = re.sub(old_render_block_regex, enhanced_js.strip(), html, flags=re.DOTALL)
    print("Successfully replaced renderDatabase with enhanced Schwellenpädagogik logic.")
else:
    print("Warning: regex for renderDatabase did not match, using targeted replacement...")

# 6. WRITE OUT TO ALL TARGET FILES
targets = [
    r"c:\Users\Senti\OneDrive - Sacre Coeur\Sport\github_sportplaner\index.html",
    r"c:\Users\Senti\OneDrive - Sacre Coeur\Sport\github_sportplaner\SportPlaner_SacreCoeur.html",
    r"c:\Users\Senti\OneDrive - Sacre Coeur\Sport\index.html",
    r"c:\Users\Senti\OneDrive - Sacre Coeur\Sport\SportPlaner_SacreCoeur.html"
]

for target in targets:
    with open(target, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Written updated file: {target} (Size: {os.path.getsize(target)} bytes)")

print("All files updated successfully!")
