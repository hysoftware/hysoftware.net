FROM node:alpine
RUN apk add git
RUN mkdir /code
VOLUME [ "/code", "/code/node_modules" ]
WORKDIR /code

ENTRYPOINT ["./run.sh"]
