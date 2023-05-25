# 20211305

# 1. Lancer le TP

## TP3 :

- écrire la commande suivante pour tester :
```
curl "http://devops-20211305.westeurope.azurecontainer.io:8081/?lat=5.902785&lon=102.754175"
```



# 2. Outils
Variables d'environnement :
```
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

EXPOSE 8081

LABEL repository=efreidevops.azurecr.io/20211305

COPY . .

CMD [ "python", "./app.py" ]

```
- Définir le Python
- Définir l'espace de travail
- Copie des fichier données
- Installation PIP des librairy dans le requiments.txt
- Le label pour sélectionner le repos azur
- Exécution par python de app.py

# 4. Rapport
## TP3 :
```
https://docs.google.com/document/d/159apYKa11RuAQMbJu6l0NlmZ1NkLW5utU0TIKomKarA/edit?usp=sharing
```
