FROM ubuntu:18.04

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

# FROM library/postgres
# ENV POSTGRES_USER brime
# ENV POSTGRES_PASSWORD panda
# ENV POSTGRES_DB queensdb
USER postgres
RUN /etc/init.d/postgresql start &&\
    psql --command "CREATE USER brime WITH SUPERUSER PASSWORD 'panda';" &&\
    createdb -O brime queensdb

EXPOSE 5432

USER root
RUN mkdir /eightqueens
WORKDIR /eightqueens
COPY . /eightqueens

ADD eightqueens.py /
ADD test_basic.py /
ADD main.py /

FROM python:3
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY ./main.py ./
COPY ./eightqueens.py  ./
CMD python main.py
