FROM python:3

RUN mkdir -p /app 

ADD . /app/

WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["./launchTests.sh"]