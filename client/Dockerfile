# BUILD STAGE
FROM node:lts-alpine as build-stage

# set work directory
WORKDIR /client

# copy dependencies
COPY package*.json ./

# copy project
COPY . .

# install dependencies and build Vue application
RUN npm install \
&& npm run build

# PRODUCTION STAGE
FROM nginx:1.24-alpine as production-stage

# Copy built app
COPY --from=build-stage /client/dist /usr/share/nginx/html
EXPOSE 8080
CMD ["nginx", "-g", "daemon off;"]
