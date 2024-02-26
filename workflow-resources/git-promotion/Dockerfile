FROM python:3.8.16

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . app/

WORKDIR app/

RUN mkdir -p clone && chmod -R 777 clone

RUN git config --system --add safe.directory "/app/clone"

ENTRYPOINT ["python3", "promote.py"]