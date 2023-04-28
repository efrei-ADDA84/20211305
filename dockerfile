FROM python:3.11.1-slim-buster
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8081
COPY . .
CMD [ "python", "./app.py" ]
