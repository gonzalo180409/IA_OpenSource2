#dockerfile for building the image
FROM ubuntu:lunar
RUN apt-get update -y
RUN apt-get install -y
RUN apt-get install -y python3.10
RUN apt-get install wget -y
RUN wget https://bootstrap.pypa.io/get-pip.py
RUN python3.10 get-pip.py
RUN pip install poetry
COPY ./ProyIA Proy
WORKDIR /Proy
RUN poetry install
WORKDIR /Proy/main
EXPOSE 8070

