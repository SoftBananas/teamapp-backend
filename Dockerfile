FROM python:3.12

RUN mkdir /teamapp

WORKDIR /teamapp

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN chmod a+x docker/*.sh