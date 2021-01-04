FROM python:3.7

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV FLASK_APP=model_server.py

CMD flask run --host=0.0.0.0
