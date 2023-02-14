FROM python:3.9

ENV PYTHONUNBUFFERED 1

RUN apt-get update -y && apt-get upgrade -y

RUN apt-get install libsasl2-dev python-dev libldap2-dev libssl-dev -y

RUN pip install -U pip

RUN mkdir -p /usr/src/app

WORKDIR /usr/src/app

COPY . .

RUN pip install -r requirements.txt

RUN chmod 777 bryin_run.sh

ENTRYPOINT [ "./bryin_run.sh"]
