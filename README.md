# 20211305

# 1. Lancer le TP

## TP1 :
- ouvrir un terminal
- écrire la commande suivante :
```
docker run --env LAT="31.2504" --env LONG="-99.2506" --env API_KEY=9e518e1b1b5a0288918557d8a16255bb stang94/tp1:latest
```

# 2. Outils
Librairies:
```
import os
import requests (ver 2.28.1)
```

Variables d'environnement :
```
LAT = os.getenv('LAT')
LONG = os.getenv('LONG')
API_KEY = os.getenv('API_KEY')
```

# 3. Dockerfile
```
FROM python:3.11.1-slim-buster

ENV VIRTUAL_ENV=/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir --requirement requirements.txt

COPY . .

CMD [ "python", "weather.py" ]
```
- Définir le Python
- Définir l'espace de travail
- Copie des fichier données
- Installation PIP des librairy dans le requiments.txt
- Exécution par python de weather.py

# 4.Dockerhub
## TP1 :
```
https://hub.docker.com/r/stang94/tp1
```

# 5. Rapport
## TP1 :
```
https://docs.google.com/document/d/1G7k5I8tQJMG45H0EFz8JQwBW7AOB18A1WDniFVgOajM/edit#
```