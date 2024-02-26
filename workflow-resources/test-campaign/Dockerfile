FROM python:3.12-alpine

COPY requirements.txt .

RUN pip install -r requirements.txt

RUN mkdir -p /app 

ADD . /app/

WORKDIR /app

ENTRYPOINT ["./launchTests.sh"]