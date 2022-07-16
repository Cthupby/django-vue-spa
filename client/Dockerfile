# pull official base image
FROM node:lts-alpine

# install server
RUN npm install -g http-server

# set work directory
RUN mkdir /client/
WORKDIR /client/

# copy dependencies
COPY package*.json ./

# install dependencies
RUN npm install

# copy project
COPY . .
