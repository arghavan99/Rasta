# pull official base image
FROM python:3.8.2-alpine

# set work directory
WORKDIR /usr/src/app

# install psycopg2 dependencies
RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add postgresql-dev
RUN pip install psycopg2

RUN pip install --upgrade pip

RUN apk --update add \
    build-base \
    jpeg-dev \
    zlib-dev

RUN pip install gunicorn

COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r /usr/src/app/requirements.txt

# copy entrypoint-prod.sh
COPY ./entrypoint.prod.sh /usr/src/app/entrypoint.prod.sh


# copy project
COPY . /usr/src/app/


# run entrypoint.prod.sh
ENTRYPOINT ["/usr/src/app/entrypoint.prod.sh"]
