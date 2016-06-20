FROM hysoftware/global-dep-image

MAINTAINER Hiroaki Yamamoto

ENV node_mode production

RUN useradd -m hysoft
USER hysoft

WORKDIR /home/hysoft
RUN virtualenv venv
WORKDIR /home/hysoft/venv
RUN mkdir webapp
COPY . /home/hysoft/venv/webapp

USER root
RUN chown -R hysoft:hysoft /home/hysoft/venv/webapp
USER hysoft

WORKDIR /home/hysoft/venv/webapp
RUN . ../bin/activate && pip install -r requirements.txt && deactivate
ENV mode production

USER root
RUN ln -s /home/hysoft/venv/webapp/docker/runserver.sh /usr/bin
RUN chmod uo+rx /home/hysoft/venv/webapp/docker/runserver.sh /usr/bin/runserver.sh
RUN mkdir ./ssl
VOLUME ./ssl
USER hysoft

ENTRYPOINT ["runserver.sh"]
EXPOSE 8888
