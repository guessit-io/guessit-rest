FROM tiangolo/uwsgi-nginx-flask:python3.6-alpine3.7
LABEL maintainer="Rémi Alvergnat <toilal.dev@gmail.com>"

ENV UWSGI_INI /guessit-rest/guessitrest/uwsgi.ini

RUN mkdir /guessit-rest && mv /app /guessit-rest/guessitrest
COPY / /guessit-rest
RUN cd /guessit-rest && pip3 install -e .

WORKDIR /guessit-rest/guessitrest


