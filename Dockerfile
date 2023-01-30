
FROM node:18.5.0-alpine

WORKDIR /usr/src/app

COPY package*.json ./

RUN npm install --only=production

COPY ./data ./data

COPY ./data ./data

COPY ./public ./public

COPY ./views ./views

COPY ./index.js ./

CMD npm start


