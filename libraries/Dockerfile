FROM gcr.io/kaggle-images/python:latest

RUN apt-get update
RUN apt-get install vim -y

RUN pip install -U pip && \
        pip install fastprogress japanize-matplotlib

COPY ./settings/jupyter_notebook_config.py /root/.jupyter/jupyter_notebook_config.py