FROM python:3.9-slim

RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /usr/src/app

WORKDIR /usr/src/app

VOLUME ["/usr/src/app"]

EXPOSE 443

CMD [ "bash" ]
