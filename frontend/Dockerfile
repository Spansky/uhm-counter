FROM node:12-alpine
ENV APP_HOME /ui
WORKDIR $APP_HOME

COPY package.json package-lock.json $APP_HOME/

RUN npm install
