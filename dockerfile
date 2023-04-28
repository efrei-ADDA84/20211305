FROM python:3.11.1
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
RUN pip install flask
COPY . .
CMD [ "python", "./weatherTP2.py" ]
