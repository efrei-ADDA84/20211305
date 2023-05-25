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
