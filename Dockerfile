FROM alpine
MAINTAINER Rémi Alvergnat <toilal.dev@gmail.com>

RUN apk --update add python py-pip ca-certificates && rm -rf /var/cache/apk/*

COPY / /root/guessit-rest/

WORKDIR /root/guessit-rest/

RUN pip install -e .

EXPOSE 5000

CMD guessit-rest

