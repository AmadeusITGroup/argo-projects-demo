FROM python:3.8.16

COPY requirements.txt .

RUN pip install -r requirements.txt

RUN mkdir -p /app 

ADD . /app/

WORKDIR /app

ENTRYPOINT ["./launchTests.sh"]