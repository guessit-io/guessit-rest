FROM tiangolo/uwsgi-nginx-flask:python3.10
LABEL maintainer="Rémi Alvergnat <toilal.dev@gmail.com>"

COPY / /guessit-rest
RUN cd /guessit-rest && pip3 install -e .

ENV UWSGI_INI /guessit-rest/guessitrest/uwsgi.ini
WORKDIR /guessit-rest/guessitrest


