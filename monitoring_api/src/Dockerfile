FROM python:3.10

WORKDIR /var/www/ugc_api

COPY requirements.txt requirements.txt
RUN  pip install --upgrade pip \
     && pip install -r requirements.txt
COPY . .

RUN chmod +x start.sh

ENTRYPOINT ["sh", "start.sh"]

