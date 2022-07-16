# pull official base image
FROM python:latest

# copy project and set work directory
RUN mkdir /server/
WORKDIR /server/

# set environment variables
ENV PYTHONUNBUFFERED 1

# copy project
COPY . .

# install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
