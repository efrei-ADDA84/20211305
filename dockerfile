FROM python:3.11.1-alpine3.15


RUN pip install --no-cache-dir --upgrade pip setuptools wheel


ENV VIRTUAL_ENV=/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"


WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


COPY . .


RUN pip install --no-cache-dir bandit
RUN bandit -r . -x venv


CMD [ "python", "weather.py" ]