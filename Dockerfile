FROM ubuntu:18.04

RUN apt update

RUN apt-get install -y python3.6 python3-pip python3-venv python-psycopg2 postgresql

RUN pip3 install --upgrade pip

RUN mkdir /eightqueens
WORKDIR /eightqueens
COPY . /eightqueens

ADD eightqueens.py /
ADD test_basic.py /
ADD main.py /

RUN python3 -m venv env
RUN source env/bin/activate

RUN pip3 install -r requirements.txt

CMD [ "python3", "./main.py" ]
