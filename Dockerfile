FROM python:3

ENV DEBIAN_FRONTEND=noninteractive

RUN apt update -y
RUN apt upgrade -y

RUN apt-get install -y python3
RUN apt-get install -y python3-pip 
RUN apt-get install -y python3-venv 
RUN apt-get install -y python-psycopg2 

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY ./main.py ./
COPY ./eightqueens.py  ./
CMD python main.py
