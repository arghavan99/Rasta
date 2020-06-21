# pull official base image
FROM python:3.8.2-alpine

# set work directory
WORKDIR /usr/src/app

# install psycopg2 dependencies
RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add postgresql-dev

RUN apt-get install -yq redis-server

RUN pip install --upgrade pip
RUN pip install -r /user/src/app/requirements.txt

# copy entrypoint-prod.sh
COPY ./entrypoint.prod.sh /usr/src/app/entrypoint.prod.sh


# copy project
COPY . /usr/src/app/


# run entrypoint.prod.sh
ENTRYPOINT ["/usr/src/app/entrypoint.prod.sh"]