FROM python:3.8-slim

WORKDIR /

COPY ./requirements.txt ./req.txt

RUN pip3 install -r req.txt

RUN python3 -m spacy download ru_core_news_lg
RUN python3 -m spacy download en_core_web_lg
RUN python3 -m nltk.downloader punkt

ENV PYTHONPATH "/src"

WORKDIR /src/core

CMD ["python3", "api_component_app.py"]
