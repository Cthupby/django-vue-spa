# pull official base image
FROM python:3.10-slim

# set work directory
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN set -x \
&& apt-get update \
&& apt-get -y install sudo \
&& apt-get -y update \
&& sudo apt-get update -y \
&& apt-get -y install libpq-dev gcc \
&& pip install --upgrade pip \
&& apt-get autoremove --purge -y && apt-get clean \
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . /app
