FROM python:3.10.11-slim-buster

RUN apt update && apt install -y git

RUN mkdir /home/app
WORKDIR /home/app

RUN pip install pynguin w3lib scrapy mutatest sybil testfixtures sphinx_rtd_theme coverage botocore

COPY tests/requirements.txt .
RUN pip install -r requirements.txt
RUN rm requirements.txt
