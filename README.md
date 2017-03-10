# OfficeScript
Python3 Skipt, das einen Login auf  [Campus Sachsen](https://campussachsen.tu-dresden.de/) ausführt um das Office Abo zu verlängern

Zur Eingabe der Logindaten das Skript einmalig von Konsole/Terminal aufrufen (`python3 OfficeScript.py`), ggf. an geeignetem Ort (z.B. `/usr/local/bin/`) speichern und zum Autostart hinzufügen  
Zum Löschen der Logindaten mit Parameter `-deleteLogin` aufrufen

benötigt Firefox  
benötigt Keyring und Selenium:
> pip3 install -U keyring  
> pip3 install -U selenium

Damit Selenium funktioniert, muss [geckodriver](https://github.com/mozilla/geckodriver) im PATH sein  
dazu z.B.  [von hier downloaden](https://github.com/mozilla/geckodriver/releases) und nach `/usr/local/bin` kopieren
