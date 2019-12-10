FROM ubuntu:18.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt update
RUN apt upgrade -y

RUN apt-get install -y python3.6 python-pip python3-venv python-psycopg2 postgresql postgresql-client postgresql-contrib postgresql-plpython

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

RUN python3 -m venv env
RUN source env/bin/activate

RUN pip install -r requirements.txt

CMD [ "python3", "./main.py" ]
