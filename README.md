# Fernet Encryptie Demo

Een klein Python-project dat laat zien hoe je een tekst symmetrisch kunt versleutelen en weer kunt ontsleutelen.

## Wat doet het?

1. Het script vraagt je om een geheime tekst.
2. Het genereert een willekeurige sleutel.
3. De tekst wordt versleuteld met die sleutel.
4. De versleutelde tekst, ook wel de token genoemd, wordt getoond.
5. Het token wordt weer ontsleuteld en de originele tekst wordt getoond.

## Vereisten

- Python 3.8 of hoger
- De bibliotheek [`cryptography`](https://pypi.org/project/cryptography/)

## Installatie

```bash
pip install cryptography
```

## Gebruik

Sla het script op als `main.py` (of een andere naam) en voer het uit:

```bash
python main.py
```

Het versleutelde bericht ziet er elke keer anders uit, ook bij dezelfde invoer. Dat komt doordat bij elke versleuteling 
een nieuwe sleutel en een tijdstempel worden gebruikt.


## Belangrijk om te weten

- **De sleutel wordt niet opgeslagen.** Hij bestaat alleen zolang het script draait. Zonder de sleutel kun je een token nooit meer ontsleutelen.
- **Symmetrische encryptie:** dezelfde sleutel wordt gebruikt om te versleutelen en te ontsleutelen. Houd de sleutel dus geheim.
- Als de sleutel of het token niet klopt, geeft `decrypt` een `cryptography.fernet.InvalidToken`-fout.
- Dit project is bedoeld om van te leren. Gebruik het niet ongewijzigd voor het beschermen van echt gevoelige gegevens. Daarvoor heb je onder meer veilig sleutelbeheer nodig.

## Link naar Github repo
https://github.com/Lucas-1054292/EncryptionLucasR 