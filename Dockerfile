FROM ubuntu:18.04
FROM python:3

ENV DEBIAN_FRONTEND=noninteractive

RUN apt update -y
RUN apt upgrade -y

RUN apt-get install -y python3
RUN apt-get install -y python3-pip 
RUN apt-get install -y python3-venv 
RUN apt-get install -y python-psycopg2 
RUN apt-get install -y postgresql 
RUN apt-get install -y postgresql-client 
RUN apt-get install -y postgresql-contrib 
RUN apt-get install -y postgresql-plpython

RUN pip install -r requirements.txt

FROM library/postgres
ENV POSTGRES_USER brime
ENV POSTGRES_PASSWORD panda
ENV POSTGRES_DB queensdb

RUN mkdir /eightqueens
WORKDIR /eightqueens
COPY . /eightqueens

ADD eightqueens.py /
ADD test_basic.py /
ADD main.py /

CMD [ "python", "./main.py" ]
