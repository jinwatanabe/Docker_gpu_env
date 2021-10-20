FROM jupyter/datascience-notebook

ENV GRANT_SUDO=yes
USER root

RUN apt-get update
RUN apt-get install -y vim
RUN pip install \
		japanize-matplotlib \
		torch

COPY ./settings/jupyter_notebook_config.py .jupyter
