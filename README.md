# Variante 1, Ausführung als Python Skript
Hierzu muss Python und entsprechende Pakete installiert sein und alles innerhalb der entsprechenden umgebung aufgerufen werden.

## Einmalige einrichtung der Umgebung
``` bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Vor und nach Benutzung die Umgebung aktivieren/deaktivieren
```
source .venv/bin/activate
# Nach nutzen
deactivate
```

# Variante 2: Executable erstellen mit pyinstaller
Dies erstellt ein ausführbares Sktipt. Dieses ist jedoch nur auf der Platform auf der 
es erstellt wurde zu gebrauchen
```
pyinstaller --onefile qr.py
```

# Aufruf
Entweder über das executable oder Python. Hier beispielhaft mit Python
```
python qr.py kit.edu -o qr_kit.png
```

Erstellt einen QR Code für [kit.edu](kit.edu) und speichert den QR Code in User/Documents/qr_codes/qr_kit.png

Für mehr Infos zu den Optionen:
```
python qr.py --help
```

# Hinweis
Commands hier beispielhaft für Mac. Auf Windows äquivalent