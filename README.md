# 20211305

# 1. Lancer le TP1
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
FROM python:3.11.1
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD [ "python", "./weather.py" ]
```
- Définir le Python
- Définir l'espace de travail
- Copie des fichier données
- Installation PIP des librairy dans le requiments.txt
- Exécution par python de weather.py

# 4.Dockerhub
```
https://hub.docker.com/r/stang94/tp1
```

# 5. Rapport
```
https://drive.google.com/file/d/1FnAPyVurq9cZ-iv75zbLq1NqZ3z042LY/view?usp=sharing
```
