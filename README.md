# 20211305

# 1. Lancer le TP

## TP2 :
- ouvrir un terminal
- écrire la commande suivante pour déployer le conteneur (test fait avec windows, donc je ne sais pas comment ca va se passer avec linux)
```
docker run -p 8081:8081 --env API_KEY=9e518e1b1b5a0288918557d8a16255bb stang94/tp2:latest
````
- écrire la commande suivante pour tester :
```
curl "http://localhost:8081/?lat=5.902785&lon=102.754175"
```

# 2. Outils
Librairies:
```
import os
import requests (ver 2.28.1)
```

Pour le TP2 on utilise ca pour le déploiement flask
```
from flask import Flask,request
from dotenv import load_dotenv
```

Variables d'environnement :
```
LAT = os.getenv('LAT')
LONG = os.getenv('LONG')
API_KEY = os.getenv('API_KEY')
```
<br>

Le .env est laissé dans le github car c'est pour le TP, mais en entreprise il est toujours enlevé avant push

.env :
```
API_KEY = "9e518e1b1b5a0288918557d8a16255bb"
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

EXPOSE 8081

COPY . .

CMD [ "python", "./app.py" ]
```
- Définir le Python
- Définir l'espace de travail
- Copie des fichier données
- Installation PIP des librairy dans le requiments.txt
- Exécution par python de app.py

# 4.Dockerhub
## TP2 :
```
https://hub.docker.com/r/stang94/tp2
```
# 5. Rapport
## TP2 :
```
https://docs.google.com/document/d/1SXV67yKEIDb_Uj9HgDAwTruUlqChXwAvY70YAWMqTwA/edit#
```
