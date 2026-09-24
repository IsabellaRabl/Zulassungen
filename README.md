# Zulassungen

## Offene Fragen

1. Bei ``pd.read_csv`` beim einlesen von z.B. demographics_example.txt kommt es darauf an, ob die einzelnen Keys mit , oder ; getrennt wurden. Beide Fälle relevant? ggf. Check einbauen.

## Notizen

#### 1. Demographics einlesen + validieren (Pandera)

Pandera prüft beim Einlesen jede Spalte gegen Typ und Plausibilität (age zwischen 0–120, gender nur M/F, alle numerischen Größen >0). -> Typsicherheit + Plausibilität

#### 2. Buckets

Reine Pandas-Transformation (``.apply()``) auf bereits validierten Daten. Kein Pandera/Pydantic-Schritt

#### 3. JSON validieren (Pydantic)

Das Metadata-Modell prüft die Struktur der JSON-Datei.

#### 4. Cross-Validation CSV↔JSON

Prüfen, dass die Observer-IDs, die in der Pandera-validierten CSV vorkommen, auch tatsächlich im Pydantic-validierten JSON-Mapping existieren.

#### 5. Merged Results validieren (Pandera)

Neben den normalen Spalten-Checks läuft hier Kardinalitätsregel über mehrere Zeilen/Spalten hinweg ("genau eine Messung pro Study+Observer+Parameter").

#### 6. Mittelwert über Observer

Reines Pandas ``groupby().mean()`` auf validierten Daten.