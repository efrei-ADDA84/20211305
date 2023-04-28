# 20211305

# 1. Lancer les TP

TP1 :
- ouvrir un terminal
- écrire la commande suivante :
```
docker run --env LAT="31.2504" --env LONG="-99.2506" --env API_KEY=9e518e1b1b5a0288918557d8a16255bb stang94/tp1:latest
```

TP2 :
- ouvrir un terminal
- écrire la commande suivante pour déployer le conteneur
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

# 3. Dockerfile
```
FROM python:3.11.1-slim-buster
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8081
COPY . .
CMD [ "python", "./XXX.py" ]
```
- Définir le Python
- Définir l'espace de travail
- Copie des fichier données
- Installation PIP des librairy dans le requiments.txt
- Exécution par python de XXX.py, changer XXX par "weather" pour le TP1 et "app" pour le TP2

# 4.Dockerhub
TP1 :
```
https://hub.docker.com/r/stang94/tp1
```

TP2 :
```
https://hub.docker.com/r/stang94/tp2
```

# 5. Rapport
TP1 :
```
https://drive.google.com/file/d/1FnAPyVurq9cZ-iv75zbLq1NqZ3z042LY/view?usp=sharing
```

TP2 :
```
```
