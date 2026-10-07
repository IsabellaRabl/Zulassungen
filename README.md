# Zulassungen

## Ziel

Machbarkeitstest: Sind Pandera (für tabellarische Verifikation) und Pydantic (für nicht-tabellarische/verschachtelte Metadaten) zusammen mit Pandas geeignet, um Performance mit Typsicherheit sicherzustellen.

Fazit: Kernmechanik nachgewiesen, im Prototyp umsetzbar.

## Tools

| Tool | Genutzt für | Warum |
| --- | --- | --- |
| Pandera | Tabellarische Daten (demographics, merged_results) | Vektorisiert, deklarative Schemas, unterstützt zeilenübergreifende Regeln (``@pa.dataframe_check``)|
| Pydantic | Nicht-tabellarische / verschachtelte Daten (JSON-Metadaten) | für beliebig verschachtelte Objekte geeignet, unterstützt zeitübergreifende Typcheckts (``ConfigDict(validate_assignment=True)``) |
| kombiniert | Cross-Validation (Pandera-geprüfte CSV und Pydantic-geprüfterJSON) |  |



## Erklärung der ``main`` Abschnitte

#### 1. Demographics einlesen + validieren (Pandera)

Pandera prüft beim Einlesen jede Spalte gegen Typ und Plausibilität (age zwischen 0–120, gender nur M/F, alle numerischen Größen >0).

#### 1.1. Validation nach Mutation (Pandera)

Pandera erkennt nachträgliche Änderungen an einer bereits validierten Tabelle ***nicht*** automatisch.

$\Rightarrow$ Erneuter expliziter Aufruf von ``.validate`` nötig zw. Verarbeitungsschritten. (Performance noch nicht klar, ggf. auf relevante Verarbeitungsschritte beschränken)

#### 2. Buckets

Reine Pandas-Transformation (``.apply()``) auf bereits validierten Daten. Kein Pandera/Pydantic-Schritt.

#### 3. JSON validieren (Pydantic)

Das Metadata-Modell prüft die Struktur der JSON-Datei bei der Erstellung.

#### 3.1. Validation des Metadata-Modells (Pydantic)

Im Gegensatz zu Pandera (s. 1.1) kann mit ``model_config = ConfigDict(validate_assignment=True)`` in Pydantic automatisch bei jeder späteren Zuweisung validiert werden. Fehlerhafte Eingaben werden direkt bei der Zuweisung abgelehnt.

#### 4. Cross-Validation CSV↔JSON

Prüft, dass die Observer-IDs, die in der Pandera-validierten CSV vorkommen, auch tatsächlich im Pydantic-validierten JSON-Mapping existieren.

#### 5. Merged Results validieren (Pandera)

Neben den normalen Spalten-Checks läuft hier Kardinalitätsregel über die Kombination mehrerer Zeilen/Spalten hinweg ("genau eine Messung pro Study+Observer+Parameter") mit ``@pa.dataframe_check``.

#### 6. Mittelwert über Observer

Reines Pandas ``groupby().mean()`` auf validierten Daten.